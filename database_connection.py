from datetime import date
import psycopg2


conn = None
try:
    conn = psycopg2.connect(user = "postgres", password="", host="localhost", port="5432", database="todo_app")
    print("Connecting to database....")
except (Exception, psycopg2.DatabaseError) as identifier:
    print(identifier)


def add_new_user_data(name, email, password):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO account (name, password, email, created_on) VALUES ('{}', '{}', '{}', '{}')".format(name, password, email, date.today()))
        conn.commit()
        print("Added Sucessfully")
    except (Exception, psycopg2.DatabaseError) as identifier:
        print("There is an error adding the user to database", identifier)

def find_user_data(email, password):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM account where email='{}' and password = '{}'".format(email, password))
        return cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as identifier:
        print("There is an error finding the user on the database", identifier)

def add_todo_data(title, objective, content):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO todos_list (title_item, objective_item, content) VALUES ('{}', '{}', '{}')".format(title, objective, content))
        conn.commit()
        print("Added sucessfully")
    except (Exception, psycopg2.DatabaseError) as identifier:
        print("There is error adding values to database", identifier)

def update_records(new_title, new_objective, new_content, id):
    try:
        cur = conn.cursor()
        cur.execute("UPDATE todos_list SET title_item = '{}', objective_item = '{}', content = '{}' WHERE item_id = {};".format(new_title, new_objective, new_content, id))
        conn.commit()
        print("Updated Sucessfully")
    except (Exception, psycopg2.DatabaseError) as identifier:
        print("There is an error updating values to database", identifier)

def get_todo_data():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM todos_list")
        all_data = cur.fetchall()
        return all_data
    except (Exception, psycopg2.DatabaseError) as identifier:
        print("There is a error selecting the values on database", identifier)

def delete_record(id_to_delete):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM todos_list WHERE item_id = {}".format(id_to_delete))
        print("ID number {} deleted.".format(id_to_delete))
    except (Exception, psycopg2.DatabaseError) as identifier:
        print("There is an error deleting the record on database", identifier)

