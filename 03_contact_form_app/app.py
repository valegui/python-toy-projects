from flask import Flask, flash, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = "secret_key"


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Message sent successfully from {form.name.data}!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
