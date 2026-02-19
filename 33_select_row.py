#first import connection 
import connection as con 
import mysql.connector as connector
try:
    sql = "select * from task order by id desc"
    mycursor = con.database.cursor(dictionary=True)
    #execute sql statement 
    mycursor.execute(sql)
    #fetch one row from table 
    # row = mycursor.fetchone()
    #fetch all row from table
    table = mycursor.fetchall()
    # print(table)
    heading = f"{'id':<6}  {'title':32}  {'category':<10}  {'detail':48}  {'status':<10}"
    print(heading)
    print("_"*110)
    for row in table: #table is list and row is dictionary(one dictionary for each row in table)
        status = None 
        if row['status'] == 0:
            status = "pending" 
        else:
            status = "completed"
        category = None 
        if row['category'] == 1:
            category = "urgent" 
        elif row['status'] == 2:
             category = "important"
        else:
             category = "casual"  
        output = f"{row['id']:<6}  {row['title']:32}  {category}  {row['detail']:48} {status}"
        print(output)
except connector.Error as error:
    print(error.errno)
    print(error.msg)