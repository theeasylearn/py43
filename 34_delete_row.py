#first import connection 
import connection as con 
import mysql.connector as connector
productid = int(input("Enter product id to delete row from table"))
try:
    sql = "delete from task where id=%s"
    data = [productid] #list
    cursor = con.database.cursor() 
    cursor.execute(sql,data) #execute sql statement using data 
    con.database.commit() #to save changes into database
    print(str(cursor.rowcount) + " rows deleted")
except connector.Error as error:
    print("Error :- ",error)
    