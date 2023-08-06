from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    # Satic files are stored in the `static` folder
    link_to_css = url_for("static", filename="style.css")

    # Render the template with the stylesheet
    return render_template("06-template.html", stylesheet=link_to_css)


if __name__ == "__main__":
    app.run(debug=True)
