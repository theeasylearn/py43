# 1st we have to import ready made mysql.connector module and give alias to it like connector
#here mysql is package name and connector is module name
import mysql.connector as connector
#code block to make connection with database (make sure wamp/mamp server is running in background)
try:
  #create connection using given host, user, password database and portno
  database = connector.connect(host='localhost',user='root',passwd='',database='om',port='3306')
  print('connection created successfully')
except connector.Error as e:
  print('Error occurred (please read detail given below)')
  print(e.errno)
  print(e.msg)
  
