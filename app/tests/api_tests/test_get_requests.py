import pytest
import requests


"""Pytest Testing for GET Requests Using JSONPlaceholder"""


def test_get_posts():
    """
    Tests GET request on /posts endpoint
    Args:
        none
    Returns:
        none
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    #print(response.json())


def test_get_comments():
    """
    Tests GET request on /comments endpoint
    Args:
        none
    Returns:
        none
    """
    response = requests.get("https://jsonplaceholder.typicode.com/comments")
    assert response.status_code == 200
    #print(response.json())


def test_get_albums():
    """
    Tests GET request on /albums endpoint
    Args:
        none
    Returns:
        none
    """
    response = requests.get("https://jsonplaceholder.typicode.com/albums")
    assert response.status_code == 200
    #print(response.json())


def test_get_photos():
    """
    Tests GET request on /photos endpoint
    Args:
        none
    Returns:
        none
    """
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    assert response.status_code == 200
    #print(response.json())


def test_get_todos():
    """
    Tests GET request on /todos endpoint
    Args:
        none
    Returns:
        none
    """
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    assert response.status_code == 200
    #print(response.json())


def test_get_users():
    """
    Tests GET request on /users endpoint
    Args:
        none
    Returns:
        none
    """
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    #print(response.json())


def test_get_post_by_post_id():
    """
    Tests GET request on /posts using specific post ID
    Args:
        none
    Returns:
        none
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")     # Post ID = 1
    assert response.status_code == 200
    print()
    print(response.json())


def test_get_comments_by_post_id():
    """
    Tests GET request on /comments using specific post ID
    Args:
        none
    Returns:
        none
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
    assert response.status_code == 200
    print()
    print(response.json())


def test_get_comments_by_post_id_using_query_string():
    """
    Tests GET request on /comments using specific post ID
    Args:
        none
    Returns:
        none
    """
    response = requests.get("https://jsonplaceholder.typicode.com/comments?postId=1")
    assert response.status_code == 200
    print()
    print(response.json())
