import sqlite3 as sql

def create_table():
    conn = sql.connect('deneme.db')
    cursor = conn.cursor()

    cursor.execute(''' Create Table IF NOT EXISTS USERS(
                   id integer PRIMARY KEY,
                   name text,
                     lastname text,
                   username text,
                     password text
                     )''')
    conn.commit()
    conn.close()
def insert(name,lastname,username,password):
    conn = sql.connect('deneme.db')
    cursor = conn.cursor()
    add_command = """INSERT INTO USERS(name,lastname,username,password) VALUES {}"""
    data = (name,lastname,username,password)
    cursor.execute(add_command.format(data))
    conn.commit()
    conn.close()

def print_all():
    conn = sql.connect('deneme.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USERS")
    list_all = cursor.fetchall()
    for user in list_all:
        print(user)
    conn.close()
def update_password(username,newPassword):
    conn = sql.connect('deneme.db')
    cursor = conn.cursor()
    upd_command = """Update Users Set password = '{}' where username = '{}' """
    cursor.execute(upd_command.format(newPassword,username))
    conn.commit()
    conn.close()
def delete_account(username):
    conn = sql.connect("deneme.db")
    cursor = conn.cursor()
    del_command = """Delete from Users where username = '{}'"""
    cursor.execute(del_command.format(username))
    conn.commit()
    conn.close()

def delete_table():
    conn = sql.connect('deneme.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE USERS")
    conn.commit()
    conn.close()

def search_user(username):
    conn = sql.connect('deneme.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USERS WHERE username = '{}'".format(username))
    user = cursor.fetchone()
    conn.close()
    return user
