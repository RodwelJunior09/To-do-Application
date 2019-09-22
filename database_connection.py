import psycopg2

conn = None
try:
    conn = psycopg2.connect(user = "postgres", password="", host="localhost", port="5432", database="todo_app")
    print("Connecting to database....")
except (Exception, psycopg2.DatabaseError) as identifier:
    print(identifier)


def add_todo_data(title, objective, content):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO todos_list (title_item, objective_item, content) VALUES ('{}', '{}', '{}')".format(title, objective, content))
        conn.commit()
        print("Added sucessfully")
    except (Exception, psycopg2.DatabaseError) as identifier:
        print("There is error adding values to database", identifier)
        
def get_todo_data():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM todos_list")
        all_data = cur.fetchall()
        return all_data
    except (Exception, psycopg2.DatabaseError) as identifier:
        print("There is a error selecting the values on database", identifier)

