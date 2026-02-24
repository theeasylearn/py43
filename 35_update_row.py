#first import connection 
import connection as con 
import mysql.connector as connector
productid = int(input("Enter product id to update row from table"))
title = input("Enter new task title")
detail = input("Enter new task detail")
requireddate = input("Enter task completion date (on or before which task must be completed)")
category = input("Press 1 for urgent, press 2 for important and press 3 casual task")
status = input("Press 0 for set task as pending, press 1 to set task as completed ")
try:
    sql = "update task set title=%s,detail=%s,requireddate=%s,category=%s,status=%s where id=%s"
    data = [title,detail,requireddate,category,status,productid]
    cursor = con.database.cursor()
    cursor.execute(sql,data)
    con.database.commit()
    print(cursor.rowcount, " row has been updated")
except connector.Error as error:
    print("Error ",error)
