TITLE: Basic FastAPI Application Setup
DESCRIPTION: Example showing how to create a basic FastAPI application with GET endpoints for root and items routes using path parameters and query parameters.

LANGUAGE: Python
CODE:
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

----------------------------------------

TITLE: Basic FastAPI Application Setup
DESCRIPTION: Example of a simple FastAPI application with two endpoints: a root endpoint and an item endpoint with path and query parameters.

LANGUAGE: Python
CODE:
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

----------------------------------------

TITLE: Creating Basic FastAPI Application in Python
DESCRIPTION: Minimal FastAPI application that defines a single GET endpoint returning a JSON response. Shows the core pattern of importing FastAPI, creating an app instance, and defining a path operation.

LANGUAGE: python
CODE:
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

----------------------------------------

TITLE: Installing FastAPI with Standard Dependencies
DESCRIPTION: Command to install FastAPI with its standard optional dependencies using pip.

LANGUAGE: bash
CODE:
pip install "fastapi[standard]"

----------------------------------------

TITLE: Configuring CORS Middleware in FastAPI
DESCRIPTION: Example shows how to set up CORS middleware in a FastAPI application with custom allowed origins, methods, and headers. Demonstrates importing CORSMiddleware, defining allowed origins, and adding middleware to the FastAPI app.

LANGUAGE: python
CODE:
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

----------------------------------------

TITLE: Creating a basic FastAPI application in Python
DESCRIPTION: This snippet shows how to create a simple FastAPI application with two endpoints: a root endpoint and an item endpoint with path and query parameters.

LANGUAGE: Python
CODE:
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

----------------------------------------

TITLE: Synchronous FastAPI Route Definition
DESCRIPTION: Alternative implementation of the root endpoint using a synchronous function instead of async. Demonstrates that FastAPI supports both sync and async route handlers.

LANGUAGE: python
CODE:
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

----------------------------------------

TITLE: Setting Response Status Code in FastAPI
DESCRIPTION: Shows how to set HTTP status codes for FastAPI path operations using both direct integer codes and status constants.

LANGUAGE: python
CODE:
from fastapi import FastAPI, status

app = FastAPI()

@app.get("/items/", status_code=status.HTTP_201_CREATED)
async def create_item():
    return {"name": "item", "id": 1}

----------------------------------------

TITLE: Running FastAPI Development Server
DESCRIPTION: Command line instructions for starting a FastAPI development server with a main.py file. Shows server startup output including documentation URLs and process information.

LANGUAGE: console
CODE:
$ fastapi dev main.py

  FastAPI  Starting development server 🚀

             Searching for package file structure from directories
             with __init__.py files
             Importing from /home/user/code/awesomeapp

   module  🐍 main.py

     code  Importing the FastAPI app object from the module with
             the following code:

             from main import app

      app  Using import string: main:app

   server  Server started at http://127.0.0.1:8000
   server  Documentation at http://127.0.0.1:8000/docs

----------------------------------------

TITLE: Creating a Dependency Function in Python for FastAPI
DESCRIPTION: Defines a common_parameters function that serves as a dependency for FastAPI route handlers. It processes query parameters for pagination and filtering.

LANGUAGE: Python
CODE:
def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

----------------------------------------

TITLE: Basic Response Model with Type Annotations
DESCRIPTION: Example showing how to declare response types using Python type annotations on path operation functions.

LANGUAGE: python
CODE:
def read_items() -> List[Item]:
    return ["Portal gun", "Plumbus"]

----------------------------------------

TITLE: Basic FastAPI Application Example
DESCRIPTION: A simple FastAPI application with two routes, demonstrating basic usage and type hints

LANGUAGE: Python
CODE:
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

----------------------------------------

TITLE: Declaring Query Parameters in FastAPI
DESCRIPTION: This snippet shows how to declare query parameters in a FastAPI route function. The parameters 'skip' and 'limit' are automatically interpreted as query parameters.

LANGUAGE: python
CODE:
async def read_item(skip: int = 0, limit: int = 10):

----------------------------------------

TITLE: Creating a Database Session Dependency with Yield in FastAPI
DESCRIPTION: This snippet demonstrates how to create a dependency that yields a database session and closes it after the response is sent. It uses a try-finally block to ensure proper cleanup.

LANGUAGE: Python
CODE:
def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()

----------------------------------------

TITLE: Password Form Data Handling in FastAPI
DESCRIPTION: Demonstrates handling username and password form data using OAuth2PasswordRequestForm dependency in FastAPI. Shows user lookup and authentication logic.

LANGUAGE: Python
CODE:
if not user_dict:
    raise HTTPException(
        status_code=400, detail="Incorrect username or password"
    )

----------------------------------------

TITLE: Using Context Managers in Dependencies with Yield in FastAPI
DESCRIPTION: This example demonstrates how to use context managers within a FastAPI dependency that uses yield. It shows the proper way to manage resources using 'with' statements inside the dependency.

LANGUAGE: Python
CODE:
class MySuperContextManager:
    def __init__(self):
        self.db = DBSession()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()

async def get_db():
    with MySuperContextManager() as db:
        yield db

----------------------------------------

TITLE: Basic Async FastAPI Route Example
DESCRIPTION: Demonstrates the basic pattern for creating an asynchronous path operation function in FastAPI using async/await syntax.

LANGUAGE: Python
CODE:
@app.get('/')
async def read_results():
    results = await some_library()
    return results

----------------------------------------

TITLE: Raising HTTPException in FastAPI
DESCRIPTION: Demonstrates how to raise an HTTPException with a 404 status code when an item is not found

LANGUAGE: python
CODE:
from fastapi import HTTPException

if item_id not in items:
    raise HTTPException(status_code=404, detail="Item not found")

----------------------------------------

TITLE: Implementing User Authentication with OAuth2
DESCRIPTION: Creates a dependency for getting the current user using OAuth2 token authentication. Includes a fake utility function for token validation and user retrieval.

LANGUAGE: python
CODE:
def fake_decode_token(token):
    return User(
        username=token + "fakedecoded",
        email="john@example.com",
        full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

----------------------------------------

TITLE: Session Dependency Implementation
DESCRIPTION: Creates a FastAPI dependency that provides database session management for requests.

LANGUAGE: python
CODE:
from typing import Annotated
from sqlmodel import Session

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

----------------------------------------

TITLE: Importing FastAPI Class in Python
DESCRIPTION: This code snippet demonstrates how to import the FastAPI class directly from the fastapi module. This is the primary way to start using FastAPI in your Python projects.

LANGUAGE: python
CODE:
from fastapi import FastAPI

----------------------------------------

TITLE: PATCH Request Partial Update in FastAPI
DESCRIPTION: Implementation of partial updates using PATCH method in FastAPI. Shows how to use Pydantic's exclude_unset and model_copy for handling partial updates while preserving existing data.

LANGUAGE: Python
CODE:
stored_item_model = Item(**stored_item_data)
update_data = item.dict(exclude_unset=True)
updated_item = stored_item_model.copy(update=update_data)
stored_item_data = jsonable_encoder(updated_item)

----------------------------------------

TITLE: Configuring OAuth2 Password Bearer in FastAPI
DESCRIPTION: This snippet shows how to set up OAuth2 password bearer authentication in a FastAPI application. It defines a token URL and creates a dependency for token validation.

LANGUAGE: python
CODE:
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

----------------------------------------

TITLE: FastAPI Route with Request Body
DESCRIPTION: Demonstrates how to declare a FastAPI route that accepts a request body using the Pydantic model.

LANGUAGE: python
CODE:
@app.post("/items/")
async def create_item(item: Item):
    return item

----------------------------------------

TITLE: Main FastAPI Application Configuration
DESCRIPTION: Shows how to set up the main FastAPI application and include multiple routers with their configurations

LANGUAGE: Python
CODE:
from fastapi import Depends, FastAPI
from .dependencies import get_query_token
from .routers import items, users
from .internal import admin

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

----------------------------------------

TITLE: Python Type Declarations with Pydantic
DESCRIPTION: Demonstrates basic Python type declarations and Pydantic model usage. Shows how to define typed variables and create Pydantic models with validated fields.

LANGUAGE: python
CODE:
from datetime import date

from pydantic import BaseModel

# Declare a variable as a str
# and get editor support inside the function
def main(user_id: str):
    return user_id


# A Pydantic model
class User(BaseModel):
    id: int
    name: str
    joined: date

----------------------------------------

TITLE: FastAPI Application with Request Body
DESCRIPTION: Advanced example demonstrating PUT endpoint with request body validation using Pydantic models, including path parameters and JSON request/response handling.

LANGUAGE: Python
CODE:
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

----------------------------------------

TITLE: Creating FastAPI HTTP Middleware with Process Time Tracking
DESCRIPTION: Implementation of a FastAPI middleware that measures request processing time and adds it as a custom X-Process-Time header. The middleware processes both incoming requests and outgoing responses, demonstrating the complete request-response cycle handling.

LANGUAGE: python
CODE:
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)

----------------------------------------

TITLE: Basic APIRouter Implementation in FastAPI
DESCRIPTION: Example of implementing an APIRouter in a users module with basic path operations. Shows how to import and create an APIRouter instance.

LANGUAGE: Python
CODE:
from fastapi import APIRouter

router = APIRouter()

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}

@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}

----------------------------------------

TITLE: Defining a List Field in a Pydantic Model
DESCRIPTION: Demonstrates how to define a list field in a Pydantic model without specifying the type of list elements.

LANGUAGE: Python
CODE:
tags: list

----------------------------------------

TITLE: Basic Path Parameter Implementation in FastAPI
DESCRIPTION: Demonstrates how to declare basic path parameters in FastAPI using Python format string syntax.

LANGUAGE: python
CODE:
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

----------------------------------------

TITLE: Declaring Model Attributes with Field
DESCRIPTION: Demonstrates how to use Field to declare model attributes with validation and metadata. Shows implementation of a Pydantic model with Field validators for title and description fields.

LANGUAGE: python
CODE:
title: str = Field(min_length=1, max_length=50, description="Title of the item")
description: str | None = Field(
    default=None, title="The description of the item", max_length=300
)

----------------------------------------

TITLE: Extended FastAPI Application Example
DESCRIPTION: Advanced FastAPI application example with multiple endpoints and error handling

LANGUAGE: python
CODE:
from typing import Annotated
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

@app.get("/items/")
async def read_items(x_token: Annotated[str | None, Header()] = None):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    return {"item": "Foo", "rating": 42}

@app.post("/items/")
async def create_item(item: dict, x_token: Annotated[str | None, Header()] = None):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if not item:
        raise HTTPException(status_code=400, detail="Invalid item")
    return {"item": item, "rating": 42}

----------------------------------------

TITLE: Configuring TrustedHostMiddleware in FastAPI
DESCRIPTION: Illustrates the use of TrustedHostMiddleware to validate the Host header in incoming requests, protecting against HTTP Host Header attacks.

LANGUAGE: Python
CODE:
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
)

----------------------------------------

TITLE: Declaring Dependencies in FastAPI Route Handlers using Python
DESCRIPTION: Demonstrates how to use the Depends function to inject dependencies into FastAPI route handlers. The example shows two routes using the common_parameters dependency.

LANGUAGE: Python
CODE:
@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons

@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons

----------------------------------------

TITLE: Basic Path Parameter Implementation in FastAPI
DESCRIPTION: Demonstrates how to declare basic path parameters in FastAPI using Python format string syntax.

LANGUAGE: python
CODE:
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

----------------------------------------

TITLE: Implementing WebSocket endpoint in FastAPI
DESCRIPTION: Demonstrates how to create a WebSocket endpoint in FastAPI, including receiving and sending messages.

LANGUAGE: python
CODE:
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

----------------------------------------

TITLE: Implementing WebSocket endpoint in FastAPI
DESCRIPTION: Demonstrates how to create a WebSocket endpoint in FastAPI, including receiving and sending messages.

LANGUAGE: python
CODE:
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

----------------------------------------

TITLE: Combining Path, Query, and Request Body Parameters
DESCRIPTION: Shows how to handle path parameters, query parameters, and request body all in one FastAPI route.

LANGUAGE: python
CODE:
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

----------------------------------------

TITLE: Custom Exception Handler Implementation
DESCRIPTION: Example of implementing a custom exception handler for a UnicornException

LANGUAGE: python
CODE:
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."}
    )

----------------------------------------

TITLE: Implementing TimedRoute for Response Time Tracking in FastAPI
DESCRIPTION: This code defines a TimedRoute class that extends APIRoute to add timing information to the response. It measures the time taken to generate the response and adds an X-Response-Time header with the duration in milliseconds.

LANGUAGE: python
CODE:
class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = time.time()
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            response.headers["X-Response-Time"] = str(duration)
            return response

        return custom_route_handler

----------------------------------------

TITLE: Basic FastAPI Test Setup
DESCRIPTION: Example showing how to set up basic tests using TestClient with FastAPI

LANGUAGE: python
CODE:
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

----------------------------------------

TITLE: Combining Path Parameters and Request Body
DESCRIPTION: Demonstrates how to use both path parameters and request body in a single FastAPI route.

LANGUAGE: python
CODE:
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

----------------------------------------

TITLE: Secure Username/Password Verification with Timing Attack Protection
DESCRIPTION: Implementation of secure credential verification using the secrets module to prevent timing attacks. Includes proper error handling and HTTP 401 responses for invalid credentials.

LANGUAGE: python
CODE:
from fastapi import Depends, FastAPI, HTTPBasic, HTTPBasicCredentials, HTTPException
from fastapi.security import HTTPBasicCredentials
import secrets

app = FastAPI()
security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"stanleyjobson"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"swordfish"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

----------------------------------------

TITLE: Defining Lifespan Events with Async Context Manager in FastAPI
DESCRIPTION: This snippet demonstrates how to create an async context manager for handling lifespan events in a FastAPI application. It simulates loading and unloading a machine learning model during startup and shutdown.

LANGUAGE: Python
CODE:
from contextlib import asynccontextmanager

from fastapi import FastAPI

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class Model:
    def __init__(self):
        self.data = {"key": "value"}

    def predict(self, x):
        return self.data

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    model = Model()
    app.state.model = model
    yield
    # Clean up the ML models and release the resources
    app.state.model = None

app = FastAPI(lifespan=lifespan)

----------------------------------------

TITLE: Importing FastAPI Request Parameter Functions
DESCRIPTION: This snippet demonstrates how to import all the special request parameter functions directly from the fastapi module. These functions include Query, Path, Body, Cookie, Header, Form, and File.

LANGUAGE: python
CODE:
from fastapi import Body, Cookie, File, Form, Header, Path, Query

----------------------------------------

TITLE: Securing FastAPI Endpoint with User Authentication
DESCRIPTION: Demonstrates how to protect an API endpoint by requiring user authentication through dependency injection of the current user.

LANGUAGE: python
CODE:
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

----------------------------------------

TITLE: Implementing GzipRequest Class for Decompressing Request Bodies in Python
DESCRIPTION: This snippet defines a custom GzipRequest class that overrides the body() method to decompress gzip-compressed request bodies when the appropriate header is present. It allows handling both compressed and uncompressed requests seamlessly.

LANGUAGE: python
CODE:
class GzipRequest(Request):
    async def body(self) -> bytes:
        if not hasattr(self, "_body"):
            body = await super().body()
            if "gzip" in self.headers.getlist("Content-Encoding"):
                body = gzip.decompress(body)
            self._body = body
        return self._body

----------------------------------------

TITLE: Creating Basic Hero Model with SQLModel
DESCRIPTION: Defines a basic Hero table model with SQLModel including id, name, secret_name and age fields.

LANGUAGE: python
CODE:
from typing import Optional
from sqlmodel import Field, SQLModel

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

----------------------------------------

TITLE: Defining a Class as a Dependency in FastAPI
DESCRIPTION: This snippet shows how to define a class 'CommonQueryParams' to be used as a dependency in FastAPI. It includes query parameters for q, skip, and limit.

LANGUAGE: Python
CODE:
class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

----------------------------------------

TITLE: Securing FastAPI Endpoint with User Authentication
DESCRIPTION: Demonstrates how to protect an API endpoint by requiring user authentication through dependency injection of the current user.

LANGUAGE: python
CODE:
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

----------------------------------------

TITLE: User Model with Password Input/Output
DESCRIPTION: Demonstrates handling sensitive data by using separate input and output models for user data with passwords.

LANGUAGE: python
CODE:
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

----------------------------------------

TITLE: User Model with Password Input/Output
DESCRIPTION: Demonstrates handling sensitive data by using separate input and output models for user data with passwords.

LANGUAGE: python
CODE:
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None