# coding: utf-8

# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist, otherwise just connect to it
conn = sqlite3.connect("new.db")
# conn = sqlite3.connect(":memory:") #avrebbe creato il db solo in memoria

# get a cursor object used to execute SQL commands
c = conn.cursor()

# use a for loop to iterate through the database, printing the results line by line
for row in c.execute("SELECT * from population"):
	print row

c.execute("SELECT * from population")
# fetchall() retrieves all records from the query
rows = c.fetchall()

# output the rows to the screen, row by row
for r in rows:
	print r[0], r[1]
	
# commit the changes
# conn.commit()

# close the database connection
conn.close()