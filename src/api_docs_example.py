from enum import Enum

from fastapi import FastAPI


class Tags(Enum):
    """A single reference point for defined tags."""

    greetings = "greetings"


# Disable docs so they're not publicly exposed.
app = FastAPI(
    title="Example API",
    summary="Provides a simple API to greet people, or entire planets.",
    version="1.0",
)


@app.get("/", summary="Greet the world in general.", tags=[Tags.greetings])
def index() -> str:
    """Provide a greeting to the entire world, free of prejudice."""
    return "Hello, world!"


@app.get("/hello/{name}", summary="Greet a specific person.", tags=[Tags.greetings])
def hello(name: str) -> str:
    """Return a greeting addressed to the person in the URL.

    - **name**: The forename to address the user by.
    """
    return f"Hello, {name}"


def build_docs() -> str:
    """Output the OpenAPI schema."""
    return app.openapi()
