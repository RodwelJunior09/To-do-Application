from wtforms import Form, StringField, PasswordField, validators, BooleanField
from wtforms.validators import InputRequired

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=50), InputRequired()])
    password = PasswordField('Password', [validators.DataRequired(), InputRequired()])
