from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_login import LoginManager
from forms.loginForm import LoginForm
from forms.create_list import CreateToDo
from database_connection import add_todo_data, get_todo_data

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

# @app.route('/delete_list', methods=["GET"])
# def DeletePost():


@app.route('/api/todo_list', methods=["GET"])
def todo_api():
    data = get_todo_data()
    all_data = todo_api_json(data)
    return jsonify(all_data)

@app.route('/loginpage', methods=["GET", "POST"])
def login_page():
    return render_template("LoginPage.html")

@app.route('/', methods=["GET"])
def homePage():
    form = CreateToDo(request.form)
    data = get_todo_data()
    all_data = todo_api_json(data)
    return render_template("HomePage.html", apidata=all_data, form=form)


def todo_api_json(data):
    todo_data = []
    for d in data:
        todo_data.append({'id': d[0], 'title': d[1], 'objective': d[2], 'content': d[3]})
    return todo_data
    

if __name__ == '__main__':
    app.run("", 5000, True)