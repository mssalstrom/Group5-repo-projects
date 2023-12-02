import pytest
import requests
import json


"""Pytest Testing for POST/PUT/PATCH/DELETE Requests Using JSONPlaceholder"""

@pytest.fixture
def json_data():
    """
    Pytest fixture for JSON test data
    Returns:
        Formatted JSON string used for POST requests
    """
    return json.dumps({"title": "stuff", "body": "things", "userId": 1})


def test_post(json_data):
    """
    Tests POST request on /posts endpoint
    Args:
        json_data: json formatted string for POST requests
    Returns:
        none
    """
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=json_data)
    assert response.status_code == 201
    #print(response.json())


def test_put():
    """
    Tests PUT request on /posts/1 endpoint
    Returns:
        none
    """
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1",
                            data={"title": "new title", "body": "new data"})
    assert response.status_code == 200
    #print(response.json())


def test_patch():
    """
    Tests PATCH request on posts/1 endpoint
    Returns:
        none
    """
    response = requests.patch("https://jsonplaceholder.typicode.com/posts/1",
                              data={"body": "new data"})
    assert response.status_code == 200
    #print(response.json())


def test_delete():
    """
    Tests DELETE request on posts/1 endpoint
    Returns:
        none
    """
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.json() == {}
