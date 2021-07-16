import pandas as pd
import mysql.connector

connection= mysql.connector.connect(host="localhost", user="root",password="mimityson",database="__edu_database__",port=3306)
df = pd.read_sql("SELECT * FROM stdinfo ;",connection)
print(df)
 

