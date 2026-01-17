from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/")
def index():
    return render_template(
        "index.html", time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


@app.route("/about")
def about():
    return render_template(
        "about.html", time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
