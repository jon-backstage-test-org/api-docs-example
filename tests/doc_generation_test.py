import json
from pathlib import Path

from api_docs_example import build_docs


def test_generate_docs() -> None:
    """Not really a test, more a hack.

    By assuming the tests will always be run we can generate new API docs each time.
    """
    with Path("openapi.json").open("w") as f:
        f.write(json.dumps(build_docs(), indent=2))
