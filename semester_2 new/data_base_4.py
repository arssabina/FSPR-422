# ===================CREATE DATABASE LESSON_5_DATABASE=============================
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="fth111620"
)
print(mydb)

mycursor=mydb.cursor()
# mycursor.execute("CREATE database lesson_5_database")

# ========================CREATE TABLE 'users'==============================

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="fth111620",
    database="lesson_5_database"
    )

mycursor=mydb.cursor()
# mycursor.execute("""CREATE TABLE IF NOT EXISTS users(
#         ID INT AUTO_INCREMENT PRIMARY KEY, 
#         name VARCHAR(10),
#         fav INT)""")

# =================INSERT DATA INTO "users" table==========================

key="""INSERT INTO users (name, fav) VALUES(%s, %s)"""
val=[('Sabina', None),
     ('Farina', 1),
     ('Tamina', 2),
     ('Hanifa', 3),
     ]

# mycursor.executemany(key, val)
# mydb.commit()

# ===================ВЫВОД ТАБЛИЦЫ "users"================================
# mycursor.execute("""SELECT * FROM users""")
# result=mycursor.fetchall()
# for x in result:
#     print(x)

# ========================CREATE TABLE 'products'==============================

# mycursor.execute("""CREATE TABLE IF NOT EXISTS products(
#         pr_ID INT AUTO_INCREMENT PRIMARY KEY,
#         pr_name VARCHAR(10))""")

key="""INSERT INTO products (pr_name) VALUE(%s)"""
val=[('pen',),
     ('book',), 
     ('copy-book',),
     ('marker',),
     ]
# mycursor.executemany(key, val)
# mydb.commit()

# ===================ВЫВОД ТАБЛИЦЫ "products"================================
# mycursor.execute("""SELECT * FROM products""")
# result=mycursor.fetchall()
# for x in result:
#     print(x)



# ===================ВЫВОД ТАБЛИЦ В ОБЪЕДИНЕННОМ ВИДЕ INNER ================================
# mycursor.execute("""SELECT users.name,
# products.pr_name FROM users
# INNER JOIN products
# ON products.pr_ID=users.fav""")
# result=mycursor.fetchall()
# for x in result: 
#     print(x)

# ===================ВЫВОД ТАБЛИЦ В ОБЪЕДИНЕННОМ ВИДЕ LEFT JOIN ================================
mycursor.execute("""SELECT users.name,
products.pr_name FROM users
RIGHT JOIN products
ON products.pr_ID=users.fav""")
result=mycursor.fetchall()
for x in result: 
    print(x)
