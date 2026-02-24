#first import connection 
import connection as con 
import mysql.connector as connector
mycursor = con.database.cursor(dictionary=True) #create cursor only once when program start
while True:
    print("Press 1 to insert new task")
    print("Press 2 to display task")
    print("Press 3 to update existing task")
    print("Press 4 to delete existing task")
    print("Press 0 to exit from program")
    choice = int(input("enter your choice"))
    if choice<0 or choice>4:
        print("invalid choice")
    else:
        if choice == 1:
            try:
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
        elif choice == 2:
            try:
                sql = "select * from task order by id desc"
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
        elif choice == 3:
            print("update existing task")
            #use 35_upeate_row.py
        elif choice == 4:
            print("delete existing task")
            #use 34_delete_row.py
        else:
            print("good bye")
            break #break the loop

print("thank you for using our program")
