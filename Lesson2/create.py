import sqlite3

# Create in memory connection which will desapeer once connection end

#connection = sqlite3.connect(':memory:')


connection = sqlite3.connect('sample.db')

table = 'CREATE TABLE people (id integer primary key, name TEXT , sirname TEXT , age INT)'


cursor = connection.cursor()

cursor.execute(table)

connection.commit()
