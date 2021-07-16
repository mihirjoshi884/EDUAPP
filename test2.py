

from tkinter import *
from tkinter import messagebox
from tkinter import Listbox
import webbrowser as wb
from webbrowser import open
import numpy as np
from numpy import array
import pandas as pd
from pandas import Series
import mysql.connector 
from mysql.connector import Error as e


def accounts():
    
    root=Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('ACCOUNTS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)



    acc_vidlist = {} 
    try:
        mycon= mysql.connector.connect(host='localhost',
                                        database='__edu_database__',
                                        user='root',
                                        password='mimityson',
                                        )
            
        cur= mycon.cursor()
        sqlvar = " SELECT * FROM acc_vid ;"
        cur.execute(sqlvar)
        val_key= cur.fetchall()
        for i in val_key:
            
            key= i[0]
            value= i[1]
        
            acc_vidlist[key]= value

    print(acc_vidlist)

        
        cur.close()
        mycon.close()

    except:      
        messagebox.showerror(title='login error', message='Error while connecting to MySQL')
        print(e)


    

    # Create listbox 
    listbox1 = Listbox(root,width=100)
    for x, y in enumerate(acc_vidlist):
        listbox1.insert(x+1, y)
    listbox1.place_configure(x=200,y=300,anchor='w')

    def play():
        
        entry1.delete(0, 'end')
        ch_url = listbox1.get(ANCHOR)
        entry1.insert(0, acc_vidlist[ch_url])
        url=s.get()
        wb.open(url)




    buttonplay= Button(root,text="play",command= play)
    buttonplay.place(x=890,y=48)

    root.mainloop()
    
if __name__ == "__main__":
    
    accounts()