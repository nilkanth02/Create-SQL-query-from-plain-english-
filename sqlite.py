import sqlite3

# connect to SQlite
connection = sqlite3.connect("student.db")

# Create the cursor object to insert record, create table
cursor = connection.cursor()

# Create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

# cursor.execute(table_info)

# Insert some more records
cursor.execute('''Insert into STUDENT values('Krish','Data Science', 'A', 90)''')
cursor.execute('''insert into STUDENT values('Sudhanshu', 'Data Science', 'B', 100)''')
cursor.execute('''insert into STUDENT values('Dariya', 'Data Science', 'A', 86)''')
cursor.execute('''insert into STUDENT values('Vikas', 'Devops', 'A', 50)''')
cursor.execute('''insert into STUDENT values('Dipesh', 'Devops', 'A', 35)''')

# Display all the records
print("The inserted records are: ")
data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()
