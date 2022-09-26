import sqlite3

from sqlite3 import Error


def sql_connection():
    try:
        conn = sqlite3.connect('mydatabase.db')
        return conn
    except Error:
        print(Error)


def sql_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("CREATE TABLE employee(emp_id n(5), emp_name char(30), dept char(15), project char(20))")
    cursorObj.executescript("""
   INSERT INTO employee VALUES(5001,'James Hoog', 'devlopment', "fusion attendence portal");
   INSERT INTO employee VALUES(5002,'Nail Knite', 'cyber security', "security operarion center");
   INSERT INTO employee VALUES(5003,'Pit Alex', 'testing', "development testing");
   """)
    conn.commit()
    cursorObj.execute("SELECT * FROM salesman")
    rows = cursorObj.fetchall()
    print("Agent details:")
    for row in rows:
        print(row)


sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")
