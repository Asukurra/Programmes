# to query the remote mysql database we are downloading a library - this is with 'pip install mysql-connector-python' in the cmd

import mysql.connector

con = mysql.connector.connect(
user = 'ardit700_student',
password = 'ardit700_student',
host = '108.167.140.122',
database = 'ardit700_pm1database'
)
# the above is saving the connection detials into a vari to be used, the detials above are provided by the teacher of this course 

cursor = con.cursor()
# .cursor is an object that is used to navigate through the data in the database

word = input("Enter a word: ")

qurey = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' "%word)
# where we added the WHERE Expression = 'inlay' we needed to wrap teh string in "" not '' beacuse we have a ' inside the string
# the Ezpression is the name of a table header in the SQL table we are querying
# the above is querying the sql database for ALL data, select * is select all, from table name 
results = cursor.fetchall()
#.fetchall is teh method to return all the data

# print(results[0])
# this returns a list of tuples
# we have added the [0] index to remove the [] from our output
# as print results only gives all the definations of a work in a single list, we want to use a for loop to change this

if results:
    for result in results:
        print(result[1])
else:
    print("no word found")        
# the above will print out the first 1 index for each answer - givein ga clean look for each answer
