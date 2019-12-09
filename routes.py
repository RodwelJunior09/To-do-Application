from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash
from flask_login import LoginManager
from forms.loginForm import LoginForm
from forms.create_list import CreateToDo
from forms.edit_form import EditListForm
from database_connection import add_todo_data, get_todo_data, delete_record, update_records, add_new_user_data, find_user_data

app = Flask(__name__, static_url_path="/static")
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/create_to_do', methods=["GET", "POST"])
def CreatingList():
    form = CreateToDo(request.form)
    if request.method == "POST":
        add_todo_data(form.title.data, form.objective.data, form.content.data)
        return redirect(url_for('homePage'))
    return render_template('CreateList.html', form=form)

# Finish the edit part of the page
@app.route('/edit/<int:id>', methods=["POST"])
def edit_list(id):
    if request.method == "POST":
        title = request.form.get("title_edit")
        objective = request.form.get("objective_edit")
        content = request.form.get("content_edit")
        update_records(title, objective, content, id)
        return redirect(url_for('homePage'))

@app.route('/api/todo_list', methods=["GET"])
def todo_api():
    data = get_todo_data()
    all_data = todo_api_json(data)
    return jsonify(all_data)

@app.route('/loginpage', methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        user_email = request.form.get("user_email")
        user_password = request.form.get("user_password")
        if find_user_data(user_email, generate_password_hash(user_password)):
            return redirect(url_for("homePage"))
    return render_template("LoginPage.html")

@app.route("/register_user", methods=["GET", "POST"])
def registerUser():
    if request.method == "POST":
        password = request.form.get("password_registration")
        another_pass = request.form.get("password_verify")
        if password == another_pass:
            name = request.form.get("name_registration")
            email = request.form.get("email_registration")
            add_new_user_data(name, email, generate_password_hash(password))
            return redirect(url_for('login_page'))
        else:
            return render_template("UserRegister.html", error_msg="There's an error with the password matching..")
    return render_template("UserRegister.html")

@app.route('/', methods=["GET", "POST"])
def homePage():
    data = get_todo_data()
    all_data = todo_api_json(data)
    return render_template("HomePage.html", apidata=all_data)


@app.route('/delete/<int:id>', methods=["POST"])
def delete_list(id):
    if request.method == "POST":
        delete_record(id)
        print("Sucessfully Deleting")
        return redirect(url_for('homePage'))

def todo_api_json(data):
    todo_data = []
    for d in data:
        todo_data.append({'id': d[0], 'title': d[1], 'objective': d[2], 'content': d[3]})
    return todo_data
    

if __name__ == '__main__':
    app.run("", 5000, True)