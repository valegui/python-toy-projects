import phonenumbers
from phonenumbers import NumberParseException
from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = "secret_key"


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")

    def validate_phone(self, field):
        if len(field.data) > 16:
            raise ValidationError("Invalid phone number.")
        try:
            input_number = phonenumbers.parse(field.data)
            if not phonenumbers.is_valid_number(input_number):
                raise ValidationError("Invalid phone number.")
        except NumberParseException as e:
            try:
                # Try with US country code
                input_number = phonenumbers.parse("+1" + field.data)
                if not phonenumbers.is_valid_number(input_number):
                    raise ValidationError("Invalid phone number.")
            except NumberParseException:
                raise ValidationError("Invalid phone number format.") from e


@app.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Message sent successfully from {form.name.data}!", "success")
        return redirect(url_for("success"))
    return render_template("contact.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
