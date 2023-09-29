from enum import Enum

from fastapi import FastAPI


class Tags(Enum):
    """A single reference point for defined tags."""

    greetings = "Greetings"


tags_metadata = [
    {
        "name": Tags.greetings.value,
        "description": "Ways to greet people.",
    },
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
def index() -> str:
    """Provide a greeting to the entire world, free of prejudice."""
    return "Hello, world!"


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
def hello(name: str) -> str:
    """Return a greeting addressed to the person in the URL.

    - **name**: The forename to address the user by.
    """
    return f"Hello, {name}"


def build_docs() -> str:
    """Output the OpenAPI schema."""
    return app.openapi()
