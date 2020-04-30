import sqlite3

connection = sqlite3.connect('tamagotchi.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS tamagotchis (id INTEGER PRIMARY KEY, name text, love integer, hunger integer, hp integer)"
cursor.execute(create_table)

connection.commit()
connection.close()