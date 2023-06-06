# СОЗДАНИЕ ТАБЛИЦЫ:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fth111620",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# =======================NEW_1 DATABASE=========================================
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="fth111620",
#   database="new_1"
# )

# mycursor = mydb.cursor()

# sql= """CREATE TABLE IF NOT EXISTS students (name VARCHAR(50), 
#                 surname VARCHAR(50),
#                 sex VARCHAR (50), 
#                 study TEXT, 
#                 adress VARCHAR (150), 
#                 class VARCHAR (10), 
#                 phone_number VARCHAR(20))"""

# mycursor.execute(sql)
# sql="SHOW TABLES"
# mycursor.execute(sql)

# for i in mycursor: 
#     print(i)


# ДОБАВЛЕНИЕ НОВОГО СТОЛБЦА В ТАБЛИЦУ ИЛИ КАКИЕ-ТО ИЗМЕНЕНИЯ: 

# sql="""ALTER TABLE students 
#     ADD COLUMN ID INT
#     AUTO_INCREMENT PRIMARY KEY"""

# mycursor.execute(sql)


# =====================new_2 DATABASE===================
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fth111620",
  database="new_2"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE pupils (name VARCHAR(25), surname VARCHAR(25))")

# =======================ДОБАВЛЕНИЕ ЗАПИСИ В ТАБЛИЦУ:================= 

sql="INSERT INTO pupils (name, surname) VALUES (%s, %s)"""
val=('Nick', 'Greenfield')
mycursor.execute(sql, val)
mydb.commit()

val=[('Nick', 'Green'),
     ('Sam', 'Brown'),
     ('Jane', 'Ostin'),
     ]

mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount)

# ========================= ПРОСМОТР ТАБЛИЦЫ ================================
sql="""SELECT * FROM pupils"""
mycursor.execute(sql)
result=mycursor.fetchall()
for x in result: 
    print(x)

# Выбор вывода таблицы выборочно по столбцам:
mycursor.execute("""SELECT name from pupils""")
result=mycursor.fetchall()
for x in result: 
    print(x)

# Выбор вывода таблицы выборочно определ.кол-во столбцов:
mycursor.execute("""SELECT name from pupils""")
result=mycursor.fetchmany(2)
for x in result: 
    print(x)