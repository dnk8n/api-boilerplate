from typing import Iterator

import pytest
from fastapi.testclient import TestClient

from api.main import app


@pytest.fixture()
def client() -> Iterator[TestClient]:
    with TestClient(app) as client:
        yield client
