import sqlite3

## Connect to Sqlite
connection= sqlite3.connect("student.db")

## Create a cursor object to insert records, create table, retreive
cursor=connection.cursor()

## Create Table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Harsh','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Harshit','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Tushar','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Anil','Devops','A',50)''')
cursor.execute('''Insert Into STUDENT values('Manish','Machine Learning','A',35)''')
cursor.execute('''Insert Into STUDENT values('NIKHIL','Devops','A',20)''')

## Display all the records

print("The inserted records are")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## Close the connection
    
connection.commit()
connection.close()