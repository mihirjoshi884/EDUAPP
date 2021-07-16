import tkinter as tk
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

    root=tk.Tk()
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
            
            key= i[1]
            value= i[2]
        
            acc_vidlist[key]= value 


        

        
        cur.close()
        

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

def business():
    root=tk.Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('BUSINESS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)



    busi_vidlist = {}

    try:
        mycon= mysql.connector.connect(host='localhost',
                                        database='__edu_database__',
                                        user='root',
                                        password='mimityson',
                                        )
            
        cur= mycon.cursor()
        sqlvar = " SELECT * FROM busi_vid ;"
        cur.execute(sqlvar)
        val_key= cur.fetchall()
        for i in val_key:
            
            key= i[1]
            value= i[2]
        
            busi_vidlist[key]= value 


        

        
        cur.close()
        

    except:      
        messagebox.showerror(title='login error', message='Error while connecting to MySQL')
        print(e)


    # Create listbox 
    listbox1 = Listbox(root,width=100)
    for x, y in enumerate(busi_vidlist):
        listbox1.insert(x+1, y)
    listbox1.place_configure(x=200,y=300,anchor='w')

    def play():
        
        entry1.delete(0, 'end')
        ch_url = listbox1.get(ANCHOR)
        entry1.insert(0, busi_vidlist[ch_url])
        url=s.get()
        wb.open(url)




    buttonplay= Button(root,text="play",command= play)
    buttonplay.place(x=890,y=48)

    root.mainloop()

def economics():

    root=tk.Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('ECONOMICS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)



    eco_vidlist = {} 
    
    try:
        mycon= mysql.connector.connect(host='localhost',
                                        database='__edu_database__',
                                        user='root',
                                        password='mimityson',
                                        )
            
        cur= mycon.cursor()
        sqlvar = " SELECT * FROM eco_vid ;"
        cur.execute(sqlvar)
        val_key= cur.fetchall()
        for i in val_key:
            
            key= i[1]
            value= i[2]
        
            eco_vidlist[key]= value 


        

        
        cur.close()
        

    except:      
        messagebox.showerror(title='login error', message='Error while connecting to MySQL')
        print(e)


    # Create listbox 
    listbox1 = Listbox(root,width=100)
    for x, y in enumerate(eco_vidlist):
        listbox1.insert(x+1, y)
    listbox1.place_configure(x=200,y=300,anchor='w')

    def play():
        
        entry1.delete(0, 'end')
        ch_url = listbox1.get(ANCHOR)
        entry1.insert(0, eco_vidlist[ch_url])
        url=s.get()
        wb.open(url)




    buttonplay= Button(root,text="play",command= play)
    buttonplay.place(x=890,y=48)

    root.mainloop()
    
def english():

    root=tk.Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('english - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)



    eng_vidlist= { }
    root=Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('ACCOUNTS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)
    dict1= dict()

    mycon= mysql.connector.connect(host='localhost',
                                    database='__edu_database__',
                                    user='root',
                                    password='mimityson',
                                    )
            
    cur= mycon.cursor()
    sqlvar = " SELECT * FROM eng_vid ;"
    cur.execute(sqlvar)
    val_key= cur.fetchall()
    for i in val_key:
            
        key= i[1]
        value= i[2]
        
        dict1[key]= value 


        

        
    cur.close()


    
    

    # Create listbox 
    listbox1 = Listbox(root,width=100)
    for x, y in enumerate(eng_vidlist):
        listbox1.insert(x+1, y)
    listbox1.place_configure(x=200,y=300,anchor='w')

    def play():
        
        entry1.delete(0, 'end')
        ch_url = listbox1.get(ANCHOR)
        entry1.insert(0, eng_vidlist[ch_url])
        url=s.get()
        wb.open(url)




    buttonplay= Button(root,text="play",command= play)
    buttonplay.place(x=890,y=48)

    root.mainloop()

def hindi():

    root=tk.Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('HINDI - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)



    hindi_vidlist = { } 
    root=Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('ACCOUNTS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)
    dict1= dict()

    mycon= mysql.connector.connect(host='localhost',
                                    database='__edu_database__',
                                    user='root',
                                    password='mimityson',
                                    )
            
    cur= mycon.cursor()
    sqlvar = " SELECT * FROM hindi_vid ;"
    cur.execute(sqlvar)
    val_key= cur.fetchall()
    for i in val_key:
            
        key= i[1]
        value= i[2]
        
        dict1[key]= value 


        

        
    cur.close()

    # Create listbox 
    listbox1 = Listbox(root,width=100)
    for x, y in enumerate(hindi_vidlist):
        listbox1.insert(x+1, y)
    listbox1.place_configure(x=200,y=300,anchor='w')

    def play():
        
        entry1.delete(0, 'end')
        ch_url = listbox1.get(ANCHOR)
        entry1.insert(0, hindi_vidlist[ch_url])
        url=s.get()
        wb.open(url)




    buttonplay= Button(root,text="play",command= play)
    buttonplay.place(x=890,y=48)

    root.mainloop()

def Informatic_Practices():

    root=tk.Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('INFORMATIC PRACTICES - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)



    ip_vidlist = { } 
    root=Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('ACCOUNTS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)
    dict1= dict()

    mycon= mysql.connector.connect(host='localhost',
                                    database='__edu_database__',
                                    user='root',
                                    password='mimityson',
                                    )
            
    cur= mycon.cursor()
    sqlvar = " SELECT * FROM ip_vid ;"
    cur.execute(sqlvar)
    val_key= cur.fetchall()
    for i in val_key:
            
        key= i[1]
        value= i[2]
        
        dict1[key]= value 


        

        
    cur.close()

    # Create listbox 
    listbox1 = Listbox(root,width=100)
    for x, y in enumerate(ip_vidlist):
        listbox1.insert(x+1, y)
    listbox1.place_configure(x=200,y=300,anchor='w')

    def play():
        
        entry1.delete(0, 'end')
        ch_url = listbox1.get(ANCHOR)
        entry1.insert(0, ip_vidlist[ch_url])
        url=s.get()
        wb.open(url)




    buttonplay= Button(root,text="play",command= play)
    buttonplay.place(x=890,y=48)

    root.mainloop()

def physics():

    root=tk.Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('PHYSICS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)



    phy_vidlist = { } 
    root=Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('ACCOUNTS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)
    dict1= dict()

    mycon= mysql.connector.connect(host='localhost',
                                    database='__edu_database__',
                                    user='root',
                                    password='mimityson',
                                    )
            
    cur= mycon.cursor()
    sqlvar = " SELECT * FROM phy_vid ;"
    cur.execute(sqlvar)
    val_key= cur.fetchall()
    for i in val_key:
            
        key= i[1]
        value= i[2]
        
        dict1[key]= value 


        

        
    cur.close()

    # Create listbox 
    listbox1 = Listbox(root,width=100)
    for x, y in enumerate(phy_vidlist):
        listbox1.insert(x+1, y)
    listbox1.place_configure(x=200,y=300,anchor='w')

    def play():
        
        entry1.delete(0, 'end')
        ch_url = listbox1.get(ANCHOR)
        entry1.insert(0, phy_vidlist[ch_url])
        url=s.get()
        wb.open(url)




    buttonplay= Button(root,text="play",command= play)
    buttonplay.place(x=890,y=48)

    root.mainloop()

def  chemistry():

    root=tk.Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('CHEMISTRY - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)



    chem_vidlist = { } 
    root=Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('ACCOUNTS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)
    dict1= dict()

    mycon= mysql.connector.connect(host='localhost',
                                    database='__edu_database__',
                                    user='root',
                                    password='mimityson',
                                    )
            
    cur= mycon.cursor()
    sqlvar = " SELECT * FROM chem_vid ;"
    cur.execute(sqlvar)
    val_key= cur.fetchall()
    for i in val_key:
            
        key= i[1]
        value= i[2]
        
        dict1[key]= value 


        

        
    cur.close()

    # Create listbox 
    listbox1 = Listbox(root,width=100)
    for x, y in enumerate(chem_vidlist):
        listbox1.insert(x+1, y)
    listbox1.place_configure(x=200,y=300,anchor='w')

    def play():
        
        entry1.delete(0, 'end')
        ch_url = listbox1.get(ANCHOR)
        entry1.insert(0, chem_vidlist[ch_url])
        url=s.get()
        wb.open(url)




    buttonplay= Button(root,text="play",command= play)
    buttonplay.place(x=890,y=48)

    root.mainloop()

def maths():

    root=tk.Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('MATHS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)



    math_vidlist = { } 
    root=Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('ACCOUNTS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)
    dict1= dict()

    mycon= mysql.connector.connect(host='localhost',
                                    database='__edu_database__',
                                    user='root',
                                    password='mimityson',
                                    )
            
    cur= mycon.cursor()
    sqlvar = " SELECT * FROM math_vid ;"
    cur.execute(sqlvar)
    val_key= cur.fetchall()
    for i in val_key:
            
        key= i[1]
        value= i[2]
        
        dict1[key]= value 


        

        
    cur.close()

    # Create listbox 
    listbox1 = Listbox(root,width=100)
    for x, y in enumerate(math_vidlist):
        listbox1.insert(x+1, y)
    listbox1.place_configure(x=200,y=300,anchor='w')

    def play():
        
        entry1.delete(0, 'end')
        ch_url = listbox1.get(ANCHOR)
        entry1.insert(0, math_vidlist[ch_url])
        url=s.get()
        wb.open(url)




    buttonplay= Button(root,text="play",command= play)
    buttonplay.place(x=890,y=48)

    root.mainloop()

def biology():

    root=tk.Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('BIOLOGY - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)



    bio_vidlist = { } 
    root=Tk()
    root.geometry("1000x1000")
    root.minsize(500,600)
    root.maxsize(1200,1200)
    root.title('ACCOUNTS - CLASS 12')
    s=StringVar()
    entry1= Entry(root,textvar=s,width=100)
    entry1.place(x=200,y=100)
    dict1= dict()

    mycon= mysql.connector.connect(host='localhost',
                                    database='__edu_database__',
                                    user='root',
                                    password='mimityson',
                                    )
            
    cur= mycon.cursor()
    sqlvar = " SELECT * FROM bio_vid ;"
    cur.execute(sqlvar)
    val_key= cur.fetchall()
    for i in val_key:
            
        key= i[1]
        value= i[2]
        
        dict1[key]= value 


        

        
    cur.close()

    # Create listbox 
    listbox1 = Listbox(root,width=100)
    for x, y in enumerate(bio_vidlist):
        listbox1.insert(x+1, y)
    listbox1.place_configure(x=200,y=300,anchor='w')

    def play():
        
        entry1.delete(0, 'end')
        ch_url = listbox1.get(ANCHOR)
        entry1.insert(0, bio_vidlist[ch_url])
        url=s.get()
        wb.open(url)




    buttonplay= Button(root,text="play",command= play)
    buttonplay.place(x=890,y=48)

    root.mainloop()
