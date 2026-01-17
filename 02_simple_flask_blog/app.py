from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    posts = [
        {"id": 1, "title": "Post 1", "content": "This is the content of post 1."},
        {"id": 2, "title": "Post 2", "content": "Another day, another post."},
        {"id": 3, "title": "Post 3", "content": "The final post."},
    ]
    return render_template(
        "index.html", title="Welcome to Simple Flask Blog", posts=posts
    )


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return render_template("post.html", post_id=post_id)


if __name__ == "__main__":
    app.run(debug=True)
