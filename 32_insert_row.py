#we have to import module connection and we will use using an alias con
import connection as con 
import mysql.connector as connector
try:
    mycursor = con.database.cursor()
    sql = "insert into task (title,detail,requireddate,category) values (%s,%s,%s,%s)"
    title = input("Enter new task title")
    detail = input("Enter new task detail")
    requireddate = input("Enter task completion date (on or before which task must be completed)")
    category = input("Press 1 for urgent, press 2 for imporant and press 3 casual task")
    values = [title,detail,requireddate,category]
    mycursor.execute(sql,values)
    con.database.commit()
    print(mycursor.rowcount," row inserted successfully")
except connector.Error as e:
    print("error in inserting row")
    print(e.errno)
    print(e.msg)
