from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/login")
def login():
    return "login"


@app.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"


if __name__ == "__main__":
    # Here we use `app.test_request_context()` to tell Flask to behave as
    # though it is handling a request, even though we are interacting with it
    # through a Python shell. This allows us to call `url_for()` with the name
    # of the function we want to generate a URL for as an argument, and Flask
    # will return the URL for that function.
    with app.test_request_context():
        print(url_for("index"))
        print(url_for("login"))
        print(url_for("login", next="/"))
        print(url_for("profile", username="John Doe"))
