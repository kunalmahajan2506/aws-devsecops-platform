import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Cloud DevOps Platform Running"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_ready():
    client = app.test_client()

    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json["status"] == "ready"


def test_metrics():
    client = app.test_client()

    response = client.get("/metrics")

    assert response.status_code == 200