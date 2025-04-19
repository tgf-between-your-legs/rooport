# FastAPI: Authentication & Security

Implementing authentication and basic security patterns in FastAPI.

## Core Concepts

*   **Authentication (AuthN):** Verifying the identity of a user or client making a request.
*   **Authorization (AuthZ):** Determining if an authenticated user has permission to perform a specific action or access a resource.
*   **Security Schemes:** Standard ways to pass authentication credentials (e.g., HTTP Basic, Bearer tokens like JWT/OAuth2, API Keys). FastAPI provides utilities for these via `fastapi.security`.

## Authentication with Dependency Injection

FastAPI typically handles authentication using its dependency injection system (`Depends`).

1.  **Define Security Scheme:** Import and instantiate a security scheme class from `fastapi.security` (e.g., `OAuth2PasswordBearer`, `HTTPBasic`, `APIKeyHeader`). This tells FastAPI how to find the credentials in the request (e.g., in the `Authorization` header) and makes it show up correctly in the OpenAPI docs.
2.  **Create Dependency Function:** Write a dependency function (often `async def`) that takes the security scheme instance as its *own* dependency. This function contains the logic to:
    *   Receive the credentials extracted by the security scheme (e.g., the token string).
    *   Validate the credentials (e.g., decode and verify a JWT, look up an API key in the database, verify username/password).
    *   Fetch the corresponding user data if validation succeeds.
    *   Raise `HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, ...)` if validation fails or credentials are missing.
    *   Return the authenticated user data (e.g., user model/dict) if validation succeeds.
3.  **Inject Dependency:** Add the dependency function to path operations that require authentication using `Depends`.

**Example: OAuth2 Password Bearer (JWT)**

```python
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated # Use Annotated for Python 3.9+
from pydantic import BaseModel
import jwt # Assume PyJWT is installed: pip install pyjwt
from passlib.context import CryptContext # Assume passlib is installed: pip install passlib[bcrypt]

# --- Configuration ---
SECRET_KEY = "your-secret-key" # Load from env vars in real app!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # Points to the /token endpoint

app = FastAPI()

# --- Pydantic Models ---
class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel): # Simplified user model
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User): # Model including hashed password
    hashed_password: str

# --- Simulated DB ---
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": pwd_context.hash("secret"), # Store hashed password
        "disabled": False,
    }
}

# --- Helper Functions ---
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username: str) -> UserInDB | None:
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return UserInDB(**user_dict)
    return None

# --- Dependency for Current User ---
async def get_current_active_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
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
        token_data = TokenData(username=username)
    except jwt.PyJWTError:
        raise credentials_exception

    user = get_user(username=token_data.username)
    if user is None or user.disabled:
        raise credentials_exception
    return User(**user.model_dump()) # Return user model without password

CurrentUserDep = Annotated[User, Depends(get_current_active_user)]

# --- Token Endpoint ---
@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = get_user(username=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password) or user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Create JWT token (implement create_access_token function)
    # access_token = create_access_token(data={"sub": user.username}, expires_delta=...)
    access_token = jwt.encode({"sub": user.username}, SECRET_KEY, algorithm=ALGORITHM) # Simplified
    return {"access_token": access_token, "token_type": "bearer"}

# --- Protected Endpoint ---
@app.get("/users/me")
async def read_users_me(current_user: CurrentUserDep):
    # If dependency runs without raising exception, user is authenticated
    return current_user

@app.get("/items/")
async def read_items(current_user: CurrentUserDep): # Require auth for this endpoint
    return [{"item_id": "Foo", "owner": current_user.username}]

```

## Authorization

*   Authorization logic (checking roles or permissions) is typically implemented *within* the dependency function (`get_current_active_user` or a separate dependency that depends on it) or directly in the path operation function after receiving the authenticated user.
*   You can create dependencies that check for specific roles or permissions and raise `HTTPException(status_code=status.HTTP_403_FORBIDDEN)` if the check fails.

## Other Security Considerations

*   **HTTPS:** Always use HTTPS in production.
*   **Input Validation:** Use Pydantic models to validate all incoming data (path/query parameters, request bodies).
*   **Rate Limiting:** Implement rate limiting (often via middleware or a reverse proxy like Nginx) to prevent abuse.
*   **CORS:** Configure `CORSMiddleware` correctly to restrict which origins can access your API.
*   **Secrets Management:** Never hardcode secrets (`SECRET_KEY`, database passwords, API keys). Use environment variables and secure deployment practices.
*   **Dependencies:** Keep FastAPI and all dependencies updated.

*(Refer to the official FastAPI Security documentation: https://fastapi.tiangolo.com/tutorial/security/)*