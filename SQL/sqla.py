# coding: utf-8

# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist, otherwise just connect to it
conn = sqlite3.connect("new.db")
conn = sqlite3.connect(":memory:") #avrebbe creato il db solo in memoria

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT) """)

# close the database connection
conn.close()