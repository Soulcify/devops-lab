from app import get_message

def test_hello():
    assert get_message() == "Hello, DevOps!"
