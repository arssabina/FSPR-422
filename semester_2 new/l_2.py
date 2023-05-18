# colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# def writeToFile(text):
#     with open(text + ".txt", 'w') as file: 
#         file.write(text)

# for color in colors:
#     writeToFile(color)

# writeToFile("FSPR-4-22")


# =======================================================================

try: 
    file=open("text.txt", 'r')
    print(file.read())
    
except: 
    print('Cannot read file')

# finally: 
#     file.close()
# =======================================================================

try: 
    file=open("text.txt", 'w')
    print(file.write("text"))
    
except: 
    print('Cannot write into file')

finally: 
    file.close()

    # ==================================================================

# def check_username(username): 
#     if len(username) < 8:
#         raise Error ("username must be at least 8 symbols")
    
# try: 
#     username='Sabina'
#     check_username
# except: 
#     print("Error")


# ==============================================================================
# CREATE DATABASE:

# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost", 
#     user = "root", 
#     password = "fth111620"
#     )
# print(mydb)

# mycursor=mydb.cursor()
# mycursor.execute("Create database new_db_1")


# ===========================================================================
# # CHECK IF DATABASE EXISTS: 

# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="fth111620"
# )

# mycursor=mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)г


# =====================================================================
# DROP DATABASE

# import mysql.connector
# mydb=mysql.connector.connect(
#     host = "localhost", 
#     user = "root", 
#     password = "fth111620"
# )

# mycursor=mydb.cursor()
# mycursor.execute("DROP DATABASE new_db_1")



import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fth111620",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# ===========================================================================================

# ВВОД ЗНАЧЕНИЙ: 

sql="INSERT INTO customers (name) VALUE (%s)"""
val=('Nick')
mycursor.execute(sql, val)
mydb.commit()



sql="""ALTER TABLE customers
ADD COLUMN surname VARCHAR (15)"""
mycursor.execute(sql)



sql="""INSERT INTO customers (surname) VALUE (%s)"""
val=('Green')
mycursor.execute(sql, val)
mydb.commit()


val=[('Nick', 'Green'),
     ('Sam', 'Brown'),
     ('Jane', 'Ostin'),
     ]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount)
