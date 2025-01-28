from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField("Nazwa użytkownika", validators=[DataRequired()])
    password = PasswordField("Hasło", validators=[DataRequired()])
    submit = SubmitField("Zaloguj się")


class RegisterForm(FlaskForm):
    username = StringField("Nazwa użytkownika", validators=[DataRequired(), Length(3, 150)])
    password = PasswordField("Hasło", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Potwierdz hasło", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Zarejestruj się")
