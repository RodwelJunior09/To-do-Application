from wtforms import Form, StringField, PasswordField, validators, BooleanField, TextAreaField

class CreateToDo(Form):
    title = StringField('Title', [validators.Length(min=10, max=20)])
    objective = StringField('Objective', [validators.Length(min=10, max=25)])
    content = TextAreaField('Content', [validators.Length(min=4, max=1000)])
    