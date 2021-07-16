import mysql.connector
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

def teachdata():
    
    teach=tk.Tk()
    teach.title('TEACHERS TABLE ')
    teach.geometry("1500x1500")
                
    img=PhotoImage(file="kv logo.png")
    lab= Label(teach,text="TEACHER DATA",bg="green",fg="white",font=("calibre",40))
    lab.pack()
    lab["compound"]= LEFT
    lab["image"]= img

    fm= Frame(teach)
    fm.pack(side=tk.LEFT,padx=20,pady=20)
    tv= ttk.Treeview(fm,column=(1,2,3,4,5,6,7),show="headings",height="20")
    tv.heading(1,text="ID")
    tv.heading(2,text="teavher name")
    tv.heading(3,text="sub_name")
    tv.heading(4,text="sub_code")
    tv.heading(5,text="kv_name")
    tv.heading(6,text="username")
    tv.heading(7,text="user password")
    tv.pack()

    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mimityson",
            database="__edu_database__"
            )

            
    cur=mydb.cursor()
        
    sql="SELECT * FROM teachertable ;"
    cur.execute(sql)
    row=cur.fetchall()
    total = cur.rowcount
    print("total no. of records are:",str(total))

    for i in row:
        tv.insert('','end',values=i)
                
            
                
                
    
    teach.mainloop()
    
teachdata()