from starlette.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)
from starlette.testclient import TestClient


def test_health(client: TestClient) -> None:
    response = client.get("/api/health")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"live": "true"}


def test_post(client: TestClient) -> None:
    url_to_shorten = "https://google.com/profile"
    response = client.post("/api/urls", json={"url": url_to_shorten})
    assert response.status_code == HTTP_200_OK
    response_object = response.json()
    expected_keys = ["short_url", "original_url"]

    assert expected_keys == [*response_object.keys()]
    assert response_object["original_url"] == url_to_shorten


def test_post_invalid_url(client: TestClient) -> None:
    invalid_url = "/invalid-url"
    response = client.post("/api/urls", json={"url": invalid_url})
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


def test_get_invalid_link(client: TestClient) -> None:
    response = client.get("/invalid-link")
    assert response.status_code == HTTP_404_NOT_FOUND


def test_get_all(link, client) -> None:
    response = client.get("/api/urls")
    assert response.status_code == HTTP_200_OK
    response_object = response.json()
    expected_keys = ["id", "short_url", "original_url", "hit"]
    row = response_object[0]
    assert expected_keys == [*row.keys()]
