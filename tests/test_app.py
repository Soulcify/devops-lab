import pytest
from app import get_message, add, is_palindrome, average, to_upper, create_app

def test_get_message():
    assert get_message() == "Hello, DevOps!"

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_is_palindrome_true():
    assert is_palindrome("Socorram-me subi no onibus em Marrocos") is True

def test_is_palindrome_false():
    assert is_palindrome("devops") is False

def test_average_normal():
    assert average([2, 4, 6]) == 4

def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])

def test_to_upper():
    assert to_upper("DevOps") == "DEVOPS"

def test_flask_client():
    app = create_app()
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello, DevOps!" in resp.data
