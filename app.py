from flask import Flask

def get_message():
    return "Hello, DevOps!"

def add(a, b):
    return a + b

def is_palindrome(s: str) -> bool:
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]

def average(nums):
    if not nums:
        raise ValueError("empty list")
    return sum(nums) / len(nums)

def to_upper(text: str) -> str:
    return text.upper()

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def hello():
        return get_message()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
