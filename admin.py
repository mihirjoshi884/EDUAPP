import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

def __admin_login__():
    root= Tk()
    root.geometry("500x300+150+150")
    root.minsize(500,300)
    root.maxsize(500,300)
    root.title('ADMIN LOGIN')
    usrname= StringVar()
    usrpass= StringVar()
    

    admin_label= Label(root,text="admin_username",font=("bold"))
    admin_label.place(x=100,y=70)
    admin_label_1= Label(root,text="admin_password",font=("bold"))
    admin_label_1.place(x=100,y=100)


    entry=Entry(root,textvar=usrname)
    entry.place(x=240,y=70)
    entry_1=Entry(root,textvar=usrpass)
    entry_1.place(x=240,y=100)

    def show_pass ():
        entry_1=Entry(root,textvar=usrname,show="")
        entry_1.place(x=240,y=100)
    
    def hide_pass ():
        entry_1=Entry(root,textvar=usrpass,show="*")
        entry_1.place(x=240,y=100)


    rd=Radiobutton(root,text="show",command= show_pass)
    rd.place(x=240,y=120)
    rd1=Radiobutton(root,text="hide",command= hide_pass)
    rd1.place(x=310,y=120)

    def login_admin():
        
        

        """ This method will take the authorised user to admin page where he or she can access the adminstration of the app 
            like uplaoding educational videos , notes etc.
         """

        adminuser= usrname.get()
        adminpass= usrpass.get()

        admin_username=""
        admin_password=""

        if adminuser == admin_username and adminpass == admin_password:
            
            admin_window= Tk()
            admin_window.geometry("900x700+150+150")
            admin_window.minsize(700,700)
            admin_window.maxsize(700,700)
            admin_window.title('admin window')

            
            def stdata():
                root=tk.Toplevel()
                root.title('table')
                root.geometry("500x600")

                row=""
                def commerce():
                    global row
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="mimityson",
                            database="__edu_database__"
                            )

            
                    cur=mydb.cursor()
        
                    sql="SELECT * FROM stdinfo where stream= 'commerce';"
                    cur.execute(sql)
                    row=cur.fetchall()
                    total = cur.rowcount
                        
                    for i in row:
                        tv.insert('','end',values=i)


                def maths():
                    global row
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="mimityson",
                            database="__edu_database__"
                            )

            
                    cur=mydb.cursor()
        
                    sql="SELECT * FROM stdinfo where stream= 'science+maths';"
                    cur.execute(sql)
                    row=cur.fetchall()
                    total = cur.rowcount
        
                    for i in row:
                        tv.insert('','end',values=i)


                def biology():
                    global row
                    mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="mimityson",
                                database="__edu_database__"
                                )

            
                    cur=mydb.cursor()
        
                    sql="SELECT * FROM stdinfo where stream= 'science+biology';"
                    cur.execute(sql)
                    row=cur.fetchall()
                    total = cur.rowcount
    
                    for i in row:
                        tv.insert('','end',values=i)


                img=PhotoImage(file="C:\\Users\\xx__mike_juliet__xx\\Desktop\\programing\\python\\edu_app\\kv logo.png ")
                lab= Label(root,text="STUDENT DATA",bg="green",fg="white",font=("calibre",40))
                lab.pack()
                lab["compound"]= LEFT
                lab["image"]= img

                fm= Frame(root)
                fm.pack(side=tk.LEFT,padx=20,pady=20)
                tv= ttk.Treeview(fm,column=(1,2,3,4,5,6,7),show="headings",height="20")
                tv.heading(1,text="ID")
                tv.heading(2,text="student name")
                tv.heading(3,text="standard")
                tv.heading(4,text="stream")
                tv.heading(5,text="gender")
                tv.heading(6,text="username")
                tv.heading(7,text="user password")
                tv.pack()

    
                b1= Button(root,text="commerce",width="30",bg='green',fg='yellow',command= commerce)
                b1.place(x=100,y=150)

                b2= Button(root,text="SCIENCE +MATHS",width="30",bg='pink',fg='red', command= maths)
                b2.place(x=310,y=150)

                b3= Button(root,text="SCIENCE + BIOLOGY",width="30",bg='red',fg='black',command= biology)
                b3.place(x=530,y=150)



                labid=StringVar()
                labusr= StringVar()
                id_label=Label(root,text="student id",font=('calibre',15))
                id_label.place(x=100,y=600)
                id_entry= Entry(root,textvar= labid)
                id_entry.place(x=200,y=600)

                usrlab=Label(root,text="usrname",font=('calibre',15))
                usrlab.place(x=100,y=625)
                usrentry= Entry(root,textvar=labusr)
                usrentry.place(x=200,y=625)

                def usredit():
                    try:
                        mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="mimityson",
                                    database="__edu_database__"
                                    )
                        cur=mydb.cursor()
                        global labid
                        print(labid)
                        global labusr
                        print(labusr)
            
                        v= labid
                        b= labusr
                        cur=mydb.cursor()

        
                        sql=   """  UPDATE stdinfo SET username= (%s) WHERE ID='{}';""".format(v)
                        value= (b)

                        cur.execute(sql,value)
                        mydb.commit()
                        print("record successfully updated")
                        sql1="""select * from stdinfo where ID='{}' """.format(labid)
                        cur.execute(sql1)
                        row= cur.fetchall()
                        for i in row:
                            print(row)
                            print(i[5])
                            print(i[6])

                    
                    except mysql.connector.Error as error:
                        print("Failed to update record to database:{}".format(error))

                    finally:
                        if (mydb.is_connected ()):
                            cur.close()
                            mydb.close()
                            print("mysql connection is closed")
                            


                usrbutton= Button(root,text="edit",command= usredit)
                usrbutton.place(x=350,y=625)

                

                pwdlab= Label(root,text="password",font=('calibre',15))
                pwdlab.place(x=100,y=650)
                pwdentry= Entry(root)
                pwdentry.place(x=200,y=650)

                def pwdedit():
                    mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="mimityson",
                                database="__edu_database__"
                                )

            
                    cur=mydb.cursor()
        
                    sql="""  UPDATE stdinfo
                             SET password= '{}'.format(labusr)
                             WHERE ID='{}'.format(labid)
                    
                        """


                    cur.execute(sql)
                    mydb.commit()

                pwdbutton= Button(root,text="edit",command= pwdedit)
                pwdbutton.place(x=350,y=650)



    


    


                root.mainloop()

            def teachdata():

                teach=tk.Toplevel()
                teach.title('TEACHERS TABLE ')
                teach.geometry("1500x1500")
                
                img=PhotoImage(file="C:\\Users\\xx__mike_juliet__xx\\Desktop\\programing\\python\\edu_app\\ kv logo.png")
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
                
            
                
                
                tv.pack()
                teach.mainloop()
    


            
            def logout():
                admin_window.destroy()
                

            STD= Button(admin_window,text="STUDENT'S DATA",width=20,command= stdata)
            STD.place(x=0,y=0)

            TEACHERDATA= Button(admin_window,text="TEACHER'S DATA",width=20,command= teachdata)
            TEACHERDATA.place(x=135,y=0)

            library_btn= Button(admin_window,text="TEXT",width=20)
            library_btn.place(x=270,y=0)

            logout_btn= Button(admin_window,text="LOGOUT",width=20,command= logout)
            logout_btn.place(x=390,y=0)
        
        
            admin_window.mainloop()


        else:

            messagebox.showerror(title='login error', message='username/password is incorrect')

    button_2=Button(root,text="login",width="20" ,command= login_admin)
    button_2.place(x=230,y=180)


    root.mainloop()

