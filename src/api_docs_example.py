from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

API_VERSION = "1.0"

# Disable docs so they're not publicly exposed.
app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/")
def index() -> str:
    """Return the index page."""
    return "Hello, world!"


@app.get("/hello/{name}")
def hello(name: str) -> str:
    """Say hello."""
    return f"Hello, {name}"


def build_docs() -> str:
    """Output the OpenAPI schema."""
    return get_openapi(
        title="Hello World",
        version=API_VERSION,
        summary="A simple API for saying hello.",
        routes=app.routes,
    )
