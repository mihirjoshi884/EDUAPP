import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='__edu_database__',
                                         user='root',
                                         password='mimityson',
                                        
                                         )
                                        
    if connection.is_connected():
         cur= connection.cursor()
         Input= (Input)
         "select * from stdinfo where ID= %s"
         cur.execute("select * from stdinfo where ID= %s",Input)

         apple= cur.fetchall()
         for row in apple:
             print(row)

         Input= input("enter your id:")
         fetch()
    
except:      
      print("Error while connecting to MySQL")
      
finally:
    if (connection.is_connected()):
        cur.close()
        connection.close()
