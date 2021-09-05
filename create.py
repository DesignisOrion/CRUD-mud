import sqlite3

connection = sqlite3.connect('users.db')

cursor = connection.cursor()

command = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)"

cursor.execute(command)

