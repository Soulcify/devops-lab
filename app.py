from flask import Flask

def get_message():
    return "Hello, DevOps!"

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def hello():
        return get_message()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
