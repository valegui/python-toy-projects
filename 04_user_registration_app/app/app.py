from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = "secret_key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class UserDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            if not username or not email or not password:
                flash("All fields are required", "error")
                return redirect(url_for("register"))

            hashed_password = generate_password_hash(password)
            user = UserDB(username=username, email=email, password=hashed_password)

            try:
                db.session.add(user)
                db.session.commit()
                flash("Registration successful", "success")
                return redirect(url_for("login"))
            except Exception:
                db.session.rollback()
                flash("Registration failed", "error")

    return render_template("register.html", form=form)


@app.route("/login")
def login():
    return render_template("login.html")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
