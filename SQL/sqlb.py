# coding: utf-8

# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist, otherwise just connect to it
conn = sqlite3.connect("new.db")
# conn = sqlite3.connect(":memory:") #avrebbe creato il db solo in memoria

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("INSERT INTO population select 'New York City', 'NY', 8200000")
cursor.execute("INSERT INTO population select 'San Franc', 'CA', 80000")

# commit the changes
conn.commit()

# close the database connection
conn.close()