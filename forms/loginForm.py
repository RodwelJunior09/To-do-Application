from wtforms import Form, StringField, PasswordField, validators, BooleanField

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=12)])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
