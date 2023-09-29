from enum import Enum
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer


class Tags(Enum):
    """A single reference point for defined tags."""

    greetings = "Greetings"


tags_metadata = [
    {
        "name": Tags.greetings.value,
        "description": "Ways to greet people.",
    },
]

permitted_origins = [
    "http://localhost:7007",
]

# Disable docs so they're not publicly exposed.
app = FastAPI(
    title="Example API",
    summary="Provides a simple API to greet people, or entire planets.",
    version="1.0",
    openapi_tags=tags_metadata,
    servers=[
        {
            "url": "https://hello.example.org",
            "description": "Production",
        },
        {
            "url": "https://staging-hello.example.org",
            "description": "Staging",
        },
        {
            "url": "http://localhost:8000",
            "description": "Local Development",
        },
    ],
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=permitted_origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

auth_scheme = HTTPBearer(bearerFormat="Token")


@app.get(
    "/v1/",
    summary="Greet the world in general.",
    tags=[Tags.greetings],
    responses={
        200: {
            "description": "A global greeting",
            "content": {"application/json": {"example": "Hello, world!"}},
        },
    },
)
def index(token: Annotated[str, Depends(auth_scheme)]) -> str:
    """Provide a greeting to the entire world, free of prejudice."""
    if token:
        return "Hello, world!"

    return JSONResponse(status_code=403)


@app.get(
    "/v1/hello/{name}",
    summary="Greet a specific person.",
    tags=[Tags.greetings],
    responses={
        200: {
            "description": "A greeting",
            "content": {"application/json": {"example": "Hello, Jon"}},
        },
    },
)
def hello(name: str, token: Annotated[str, Depends(auth_scheme)]) -> str:
    """Return a greeting addressed to the person in the URL.

    - **name**: The forename to address the user by.
    """
    if token:
        return f"Hello, {name}"

    return JSONResponse(status_code=403)


def build_docs() -> str:
    """Output the OpenAPI schema."""
    return app.openapi()
