"""------------CREATE DATABASE LESSON_5_HOMEWORK---------------"""

import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root', 
    password='fth111620'
)
print(mydb)
mycursor=mydb.cursor()
# mycursor.execute("""CREATE DATABASE lesson_5_homework""")


"""----------------CREATE 1-TABLE MARCH-------------------"""
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='fth111620',
    database='lesson_5_homework'
)
mycursor=mydb.cursor()
# mycursor.execute("""CREATE TABLE IF NOT EXISTS march(
#     id INT AUTO_INCREMENT PRIMARY KEY, 
#     name VARCHAR(10), 
#     fav_date INT)""")

"""----------------INSERT INFO INTO 1-TABLE MARCH-------------------"""
key="""INSERT INTO march(name, fav_date) VALUES (%s, %s)"""
val=[('Mama', 1),
     ('Samir',2),
     ('Sabina', None),
     ('Asmira', 4),
     ]
# mycursor.executemany(key, val)
# mydb.commit()

"""----------------OUTPUT 1-TABLE MARCH-------------------"""
# mycursor.execute("""SELECT * FROM march""")
# result=mycursor.fetchall()
# for x in result:
#     print(x)


"""----------------CREATE 2-TABLE favorits-------------------"""
# mycursor.execute("""CREATE TABLE IF NOT EXISTS favorits(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     food VARCHAR(10), 
#     number INT)""")

"""----------------INSERT INFO INTO 2-TABLE favorits-------------------"""
# key="""INSERT INTO favorits(food, number) VALUES (%s, %s)"""
# val=[('cheese', 2),
#      ('pear', 3), 
#      ('apple', 1),
#      ]
# mycursor.executemany(key, val)
# mydb.commit()

"""----------------OUTPUT 2-TABLE favorits-------------------"""
# mycursor.execute("""SELECT * FROM favorits""")
# result=mycursor.fetchall()
# for x in result:
#     print(x)

"""----------------OUTPUT TWO TABLES WITH JOIN-------------------"""
# mycursor.execute("""SELECT name, food FROM march
# JOIN favorits ON march.id=number""") 
# result=mycursor.fetchall()
# for x in result:
#     print(x)


# mycursor.execute("""ALTER TABLE march (
#     ADD FOREIGN KEY (id) REFERENCES favorits(id)) """) 