# ====================== CREATE DATABASE LESSON_4: ====================================

# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost", 
#     user = "root", 
#     password = "fth111620"
#     )
# print(mydb)

# mycursor=mydb.cursor()
# mycursor.execute("Create database lesson_4_database")


# ====================== CREATE A TABLE STUDENTS: ====================================

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fth111620",
  database="lesson_4_database"
)

mycursor = mydb.cursor()
# mycursor.execute("""CREATE TABLE IF NOT EXISTS students (
                #  name VARCHAR (10), 
                #  login CHAR (6), 
                #  gender ENUM('f', 'm'), 
                #  phone_number INT,
                #  scholarship FLOAT,
                #  results_of_exam BOOLEAN,
                #  weight DECIMAL(65, 30), 
                #  date_of_birth DATE, 
                #  log_in_time TIMESTAMP)""")

key="""INSERT INTO students(name, login, gender, phone_number, scholarship, results_of_exam, weight, date_of_birth, log_in_time)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s,%s)"""
val=('Helen', 'heleny', 'f', 9117199, 100000.2, True, 58.22, '1986-02-12', '2023-03-14 19:46:01')

mycursor.execute(key, val)
mydb.commit()

# ======================== ПРОСМОТР ТАБЛИЦЫ ======================================
# key="""SELECT * FROM students"""
# mycursor.execute(key)
# result=mycursor.fetchall()
# for x in result: 
#     print(x)

# # ======================== ДОБАВЛЕНИЕ НОВОГО СТОЛБЦА В ТАБЛИЦУ ==================

# mycursor.execute("""ALTER TABLE students 
#     ADD COLUMN ID INT 
#     AUTO_INCREMENT PRIMARY KEY""")

# =========== ОБНОВЛЕНИЕ ИНФО В ТАБЛИЦЕ ================================-=========

mycursor.execute("""UPDATE students SET weight = 59.2 WHERE ID=1;""") 
mydb.commit()

# =========================УДАЛЕНИЕ ЗНАЧЕНИЙ В ТАБЛИЦЕ============================

# mycursor.execute("""DELETE FROM students """)  для удаления всего инфо с таблицы
mycursor.execute("""DELETE FROM students""")  # для удаления инфо пользователя с 2-id с таблицы
