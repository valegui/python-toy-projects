from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "id": 1,
        "title": "Introduction to Flask",
        "content": "Flask is a micro web framework for Python. It is designed to make it easy to create web applications.",
        "author": "John Doe",
    },
    {
        "id": 2,
        "title": "Flask Templates",
        "content": "Flask templates are used to render HTML pages. They are stored in the templates folder.",
        "author": "Jane Doe",
    },
    {
        "id": 3,
        "title": "Flask Routing",
        "content": "Flask routing is used to map URLs to functions. They are stored in the app.py file.",
        "author": "John Doe",
    },
]


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post:
        return render_template("post.html", post=post)
    else:
        return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
