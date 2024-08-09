import sqlite3 

##connect to sqlite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

#create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Jane','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Katy','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Johnny','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Esra','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Adrian','DEVOPS','A',35)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
