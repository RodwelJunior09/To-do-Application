from wtforms import Form, StringField, PasswordField, validators, BooleanField, TextAreaField

class EditListForm(Form):
    edit_title = StringField('Edit_Title', [validators.Length(min=10, max=20)])
    edit_objective = StringField('Edit_Objective', [validators.Length(min=10, max=25)])
    edit_content = TextAreaField('Edit_Content', [validators.Length(min=4, max=1000)])