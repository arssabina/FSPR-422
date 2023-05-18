"""------------CREATE DATABASE LESSON_6_DATABASE---------------"""

import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root', 
    password='fth111620'
)
print(mydb)
# mycursor=mydb.cursor()
# mycursor.execute("""CREATE DATABASE lesson_6_database""")



"""------------CREATE TABLE CAMPAIGN---------------"""
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root', 
    password='fth111620',
    database='lesson_6_database'
)

mycursor=mydb.cursor()
# mycursor.execute("""CREATE TABLE IF NOT EXISTS campaign(
#     ID INT AUTO_INCREMENT PRIMARY KEY, 
#     name VARCHAR(40), 
#     objectives VARCHAR(40),
#     sponsor VARCHAR(40),
#     start_date DATE, 
#     end_date DATE, 
#     other_details VARCHAR(40))""")

"""----------------INSERT INFO INTO TABLE 'campaign'-------------------"""
# key="""INSERT INTO campaign (name, objectives, sponsor, start_date, end_date, other_details) VALUES (%s, %s, %s, %s, %s, %s)"""
# val=[('Farina', 'kind', 'akfa','2022-02-13','2026-02-13', 'swimming'), 
#      ('Tamina', 'clever', 'usmanov', '2020-03-12','2027-02-13', 'reading'),
#      ('Hanifa', 'smart', 'arshidinova', '2022-04-20','2028-02-13', 'dancing'), 
#      ('Asmira', 'beautiful', 'rashidov','2023-02-04','2027-02-13', 'singing'), 
#      ('Honzoda', 'little', 'bozorov','2022-06-30','2028-02-13', 'playing'),
# ]
# mycursor.executemany(key, val)
# mydb.commit()

"""----------------OUTPUT table 'campaign'-------------------"""

# mycursor.execute("""SELECT * FROM campaign""")
# result=mycursor.fetchall()
# for x in result:
#     print(x)


"""------------CREATE TABLE 'LEADS' ---------------"""
# mycursor.execute("""CREATE TABLE IF NOT EXISTS leads (
#     id INT AUTO_INCREMENT PRIMARY KEY, 
#     first_name VARCHAR(40),
#     surname VARCHAR(40),
#     other_details VARCHAR(40))""")

"""----------------INSERT INFO INTO TABLE 'leads'-------------------"""
# key="""INSERT INTO leads (first_name, surname, other_details) VALUES (%s, %s, %s)"""
# val=[('Bekzod', 'Rashidov','swimming'), 
#      ('Bohir', 'Toshxujaev', 'watching_fOotball'),
#      ('Mamura', 'Ahmedova', 'reading'), 
#      ]
# mycursor.executemany(key, val)
# mydb.commit()

"""----------------OUTPUT table 'leads'-------------------"""
# mycursor.execute("""SELECT * FROM leads""")
# result=mycursor.fetchall()
# for x in result:
#     print(x)


"""------------CREATE TABLE 'campaign_members' ---------------"""
# mycursor.execute("""CREATE TABLE IF NOT EXISTS campaign_members(
#     campaign_ID INT,
#     leads_id INT, 
#     PRIMARY KEY (campaign_id, leads_id),
#     FOREIGN KEY(campaign_ID) REFERENCES campaign(ID),
#     FOREIGN KEY (leads_id) REFERENCES leads(id))""")

# # """---------------СОЕДИНЕНИЕ ДВУХ ТАБЛИЦ 'campaign','leads'-------------------"""

mycursor.execute("""SELECT * FROM campaign_members""")
result=mycursor.fetchall()
for x in result:
    print(x)
