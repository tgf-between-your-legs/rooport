# FastAPI: Security & Authentication Basics

Implementing basic security measures and authentication patterns in FastAPI.

## Core Concept: Protecting API Endpoints

Securing an API involves verifying the identity of the client (Authentication) and controlling what actions the authenticated client is allowed to perform (Authorization). FastAPI provides tools and leverages dependency injection to implement various security schemes.

**Key Security Areas:**

*   **Authentication:** Verifying who the user is (e.g., via username/password, API keys, tokens like JWT or OAuth2).
*   **Authorization:** Determining if the authenticated user has permission to perform the requested action.
*   **Data Validation:** Preventing invalid or malicious data injection (handled well by Pydantic).
*   **HTTPS:** Encrypting communication between client and server.
*   **Rate Limiting:** Preventing abuse by limiting request frequency.
*   **Input Sanitization:** Although Pydantic handles validation, be mindful of how data is used (e.g., in raw SQL queries if ORM is bypassed).
*   **Dependency Security:** Keeping framework and libraries updated.

## Authentication with OAuth2 Password Bearer Flow (Example)

FastAPI provides utilities in `fastapi.security` to help implement standard security schemes like OAuth2 with Password Flow (username/password exchange for a bearer token).

**1. Setup (`security.py` or similar):**

```python
# security.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt # Using python-jose for JWT handling
from passlib.context import CryptContext # For password hashing
from datetime import datetime, timedelta, timezone
from typing import Optional
from typing_extensions import Annotated
import os # For secret key

# --- Configuration ---
# Load from environment variables in a real app!
SECRET_KEY = os.environ.get("SECRET_KEY", "your-fallback-secret-key") # KEEP THIS SECRET!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# --- Password Hashing ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# --- JWT Token Handling ---
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def decode_token(token: str) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        if username is None:
            raise credentials_exception
        # Could add more checks here (e.g., token expiry already checked by jwt.decode)
        # In a real app, fetch user from DB based on username/id in payload
        # For this example, just return the payload
        return payload # Contains 'sub' (username) and 'exp'
    except JWTError:
        raise credentials_exception

# --- OAuth2 Scheme ---
# This defines how FastAPI gets the token (from Authorization: Bearer <token> header)
# tokenUrl should point to your login endpoint
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --- Dependency to Get Current User ---
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    payload = await decode_token(token)
    # In a real app: fetch user from DB using payload.get("sub")
    user = {"username": payload.get("sub"), "email": "user@example.com"} # Fake user
    if user is None:
         raise HTTPException(status_code=404, detail="User not found")
    return user # Return user object/dict

async def get_current_active_user(current_user: Annotated[dict, Depends(get_current_user)]):
    # Add checks here if needed (e.g., is_active flag)
    # if not current_user.get("is_active"):
    #     raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

```

**2. Login Endpoint (`main.py` or `routers/auth.py`):**

```python
# main.py (or routers/auth.py)
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated
import security # Import your security utilities
import schemas # Import your Pydantic models

app = FastAPI() # Or APIRouter

# --- Token Endpoint ---
@app.post("/token", response_model=schemas.Token) # Define a Token schema in schemas.py
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    # In a real app: fetch user from DB by form_data.username
    # user = get_user_from_db(form_data.username)
    # Fake user check:
    if form_data.username != "testuser": # or not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # hashed_password = user.hashed_password
    hashed_password = security.get_password_hash("password") # Example hashed password

    # Verify password
    if not security.verify_password(form_data.password, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create JWT token
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

```

**3. Protecting Endpoints (`main.py` or router files):**

```python
# main.py (or router files)
@app.get("/users/me", response_model=schemas.UserResponse)
# Use the dependency to get the current user
# This automatically requires a valid Bearer token via oauth2_scheme
async def read_users_me(
    current_user: Annotated[schemas.User, Depends(security.get_current_active_user)]
):
    # If token is invalid or missing, get_current_active_user raises HTTPException
    # If valid, current_user contains the user data/object
    return current_user

@app.get("/items/protected")
# You can add dependencies directly to path operations or routers
async def read_protected_items(current_user: Annotated[dict, Depends(security.get_current_active_user)]):
    return [{"item": "Portal Gun", "owner": current_user["username"]}]

```

## Authorization

Authorization (checking *permissions*) is typically handled *after* authentication.

*   **Inside Path Operations:** Check user roles or permissions within the path operation function after getting the `current_user` via dependency injection.
*   **In Dependencies:** Create dependencies that check for specific roles or permissions and raise `HTTPException(status.HTTP_403_FORBIDDEN)` if the check fails. Apply these dependencies to relevant path operations or routers.

```python
# Example Permission Dependency
async def require_admin(current_user: Annotated[dict, Depends(security.get_current_active_user)]):
    # In real app, check user.role or user.permissions
    if current_user.get("username") != "admin": # Simplified check
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    return current_user

@app.delete("/admin/delete-everything")
async def delete_everything(admin_user: Annotated[dict, Depends(require_admin)]):
    # This endpoint requires admin privileges via the dependency
    return {"message": f"Everything deleted by {admin_user['username']}"}
```

FastAPI's security tools and dependency injection make implementing authentication (like OAuth2 Bearer Tokens) and authorization straightforward. Define security schemes, create dependencies to verify credentials/tokens and check permissions, and apply these dependencies to your path operations or routers. Always handle secrets securely and use robust password hashing.