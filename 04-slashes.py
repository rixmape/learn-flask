from flask import Flask

app = Flask(__name__)


@app.route("/projects/")
def projects():
    """
    The canonical URL for the projects endpoint has a trailing slash. It's similar to a folder in a file system. If you access the URL without a trailing slash (/projects), Flask redirects you to the canonical URL with the trailing slash (/projects/).
    """
    return "The project page"


@app.route("/about")
def about():
    """
    The canonical URL for the about endpoint does not have a trailing slash. It’s similar to the pathname of a file. Accessing the URL with a trailing slash (/about/) produces a 404 “Not Found” error. This helps keep URLs unique for these resources, which helps search engines avoid indexing the same page twice.
    """
    return "The about page"


if __name__ == "__main__":
    app.run(debug=True)
