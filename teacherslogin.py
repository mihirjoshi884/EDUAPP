from tkinter import *
import mysql.connector
from tkinter import messagebox

def teacherwin():
    

    root= Tk()
    root.geometry("500x300+150+150")
    root.minsize(500,300)
    root.maxsize(500,300)
    root.title('teacher login')

    teacherid=StringVar() 
    unm=StringVar()
    pwd=StringVar()

    tname=""
    sub_name=""
    sub_code=""
    dusrname=""
    dusrpass=""
    kvname=""
    tid=""

    label_id= Label(root,text="teacher ID",font="40")
    label_id.place(x=100,y=40)
    label= Label(root,text="username",font=40)
    label.place(x=100,y=70)
    label_1= Label(root,text="password",font=40)
    label_1.place(x=100,y=100)


    entry=Entry(root,textvar=unm)
    entry.place(x=180,y=70)
    entry_1=Entry(root,textvar=pwd)
    entry_1.place(x=180,y=100)
    entry_id= Entry(root,textvar=teacherid)
    entry_id.place(x=180,y=40)


    def show_pass ():


        """ show_pass() :method is user defined method which is used in show in password which will be typed by 
        user of these app .
        """
        entry_1= Entry(root,show="")
        entry_1.place(x=180,y=100)


    def hide_pass ():


        """ hide_pass (): method is also an user defined methods which is used to hide password so that privacy is
            can be sustained .  
        """
        entry_1= Entry(root,show="*")
        entry_1.place(x=180,y=100)


    rd=Radiobutton(root,text="show",command= show_pass)
    rd.place(x=180,y=120)
    rd1=Radiobutton(root,text="hide",command= hide_pass)
    rd1.place(x=250,y=120)


    def __cancel__ ():


        """ __cancel__(): this method helps in quiting the program . 
        """   
        print("program is aborting")
        quit()
    def login():
        print("inside login....")
        # studentid=StringVar() 
        # username=StringVar()
        # password=StringVar()
 
    

        global tname 
        global sub_name
        global sub_code
        global dusrname
        global dusrpass
        global kvname
        global tid

        try:
            mycon= mysql.connector.connect(host='localhost',
                                            database='__edu_database__',
                                            user='root',
                                            password='mimityson',
                                            )
        
            cur= mycon.cursor()
            kv_t_id= (teacherid.get())
            sqlvar = "select * from teacher_table where ID = '{}' ".format(kv_t_id)
            cur.execute(sqlvar)


            apple= cur.fetchall()
            for i in apple:
                print(i)
                tid=i[0]
                tname=i[1]
                sub_name=i[2]
                sub_code=i[3]
                kvname=i[4]
                dusrname=i[5]
                dusrpass=i[6] 
                

                
            cur.close()
            mycon.close()


        except:      
            messagebox.showerror(title='login error', message='Error while connecting to MySQL')
    
    
        username = unm.get()
        password= pwd.get()

        print(username, dusrname)
        print(password, dusrpass)

        if (username==dusrname) and (password == dusrpass):
            

            login_= Toplevel()
            login_.geometry("500x300+150+150")
            login_.minsize(500,300)
            login_.maxsize(500,300)

            def __home__():
                
                        

                home= Toplevel()
                home.geometry("500x300+150+150")
                home.minsize(500,300)
                home.maxsize(500,300)

                home.mainloop()
                
                
                
            def __profile__():
                    
                profile= Toplevel()
                profile.geometry("500x300+150+150")
                profile.minsize(500,300)
                profile.maxsize(500,300)

                global tname
                global sub_name
                global sub_code
                global dusrname
                global dusrpass
                global kvname
                global tid

                try:
                    mycon= mysql.connector.connect(host='localhost',
                                                    database='__edu_database__',
                                                    user='root',
                                                     password='mimityson',
                                                    )
                
                    cur= mycon.cursor()
                    kv_t_id= (teacherid.get())
                    sqlvar = "select * from stdinfo where ID = '{}' ".format(kv_t_id)
                    cur.execute(sqlvar)


                    apple= cur.fetchall()
                    for i in apple:
                                
                                
                        print(i)
                        tid=i[0]
                        tname=i[1]
                        sub_name=i[2]
                        sub_code=i[3]
                        kvname=i[4]
                        dusrname=i[5]
                        dusrpass=i[6] 
                    

                    cur.close()
                    mycon.close()

                except:      
                    messagebox.showerror(title='login error', message='Error while connecting to MySQL')

                
                img=PhotoImage(file="kv logo.png")    
                lab=Label(profile,text="PROFILE",font=("calibre",30),bg="lightgreen",fg="yellow")
                lab.pack()
                lab["compound"]= LEFT
                lab["image"]= img

                stidlabel=  Label(profile,text="teacher idcode",bg="purple4",fg="white")
                stidlabel.place(x=50,y=75)
                stidlabel1=  Label(profile,text= tid,bg="purple4",fg="white" )
                stidlabel1.place(x=350,y=75)

                namelabel= Label(profile,text="name of the teacher",bg="red",fg="misty rose")
                namelabel.place(x=50,y=100)
                namelabel1= Label(profile,text= tname,bg="red",fg="misty rose")
                namelabel1.place(x=350,y=100)
                genderlabel= Label(profile,text="subject name",bg="light salmon",fg="purple3")
                genderlabel.place(x=50,y=125)
                genderlabel1= Label(profile,text= sub_name,bg="light salmon",fg="purple3")
                genderlabel1.place(x=350,y=125)

                standardlabel= Label(profile,text="subject code",bg="yellow",fg="green2")
                standardlabel.place(x=50,y=150)
                standardlabel1= Label(profile,text= sub_code,bg="yellow",fg="green2")
                standardlabel1.place(x=350,y=150)

                streamlabel= Label(profile,text="name of the kv",bg="cornsilk3",fg="black")
                streamlabel.place(x=50,y=175)
                streamlabel1= Label(profile,text=kvname,bg="cornsilk3",fg="black")
                streamlabel1.place(x=350,y=175)

                usernamelabel= Label(profile,text="username",bg="lavender",fg="DarkGoldenrod2")
                usernamelabel.place(x=50,y=200)
                usernamelabel1= Label(profile,text= dusrname,bg="lavender",fg="DarkGoldenrod2")
                usernamelabel1.place(x=350,y=200)

                passwordlabel= Label(profile,text="password",bg="powder blue",fg="purple4")
                passwordlabel.place(x=50,y=225)
                passwordlabel1= Label(profile,text= dusrpass,bg="powder blue",fg="purple4")
                passwordlabel1.place(x=350,y=225)


                profile.mainloop()
                


            def upload():
                    
                    
                subject= ""            
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="mimityson",
                    database="__edu_database__"
                    )

                mycursor = mydb.cursor()


                sql = """ SELECT * FROM teachertable WHERE ID ='{}' """.format(teacherid.get())
                mycursor.execute(sql)

                row = mycursor.fetchall()
                for i in row :
                    subject= i[2]
                        
                print(subject)
                    

                if subject == "Accounts":
                                                
                    uploadwin = Toplevel()
                    uploadwin.geometry("600x400")
                    uploadwin.minsize(500,300)
                    uploadwin.maxsize(900,600)

                    img=PhotoImage(file="kv logo.png")
                    img1=PhotoImage(file="kv logo.png")
                    mainlab= Label(uploadwin,text="UPLOAD",bg="yellow",fg="black",font="calibre 60")
                    mainlab.pack()
                    mainlab["compound"]= LEFT,
                    mainlab["image"]= img

                    st= StringVar()
                    chap= StringVar()
                    url= StringVar()

                    std = Label(uploadwin,text="CLASS")
                    std.place(x=100,y=160)
                    stdentry= Entry(uploadwin,textvar=std,width=50)
                    stdentry.place(x=200,y=160)

                    chaplab= Label(uploadwin,text="CHAPTER NAME")
                    chaplab.place(x=100,y=200)
                    chapentry= Entry(uploadwin,textvar=chap,width=50)
                    chapentry.place(x=200,y=200)


                    urllab= Label(uploadwin,text="VIDEO LINK")
                    urllab.place(x=100,y=240)
                    urlentry= Entry(uploadwin,textvar=url,width=50)
                    urlentry.place(x=200,y=240)
                    def upload():
                            
                        mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="mimityson",
                                    database="__edu_database__"
                                    )

                        mycursor = mydb.cursor()


                        sql = "INSERT INTO acc_vid (class,chapter_name,url) VALUES (%s,%s, %s )"
                        val = (st.get(),chap.get(),url.get())
                        mycursor.execute(sql, val)

                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo(title='account saved', message='congratulation your video is uploaded !!!')


                    upload= Button(uploadwin,text="upload",width=30,command= upload)
                    upload.place(x=200,y=290)
                    uploadwin.mainloop()
                        
                elif subject == "Business studies":
                        
                    uploadwin = Toplevel()
                    uploadwin.geometry("600x400")
                    uploadwin.minsize(500,300)
                    uploadwin.maxsize(900,600)

                    img=PhotoImage(file="kv logo.png")
                    img1=PhotoImage(file="kv logo.png")
                    mainlab= Label(uploadwin,text="UPLOAD",bg="yellow",fg="black",font="calibre 60")
                    mainlab.pack()
                    mainlab["compound"]= LEFT,
                    mainlab["image"]= img

                    st= StringVar()
                    chap= StringVar()
                    url= StringVar()

                    std = Label(uploadwin,text="CLASS")
                    std.place(x=100,y=160)
                    stdentry= Entry(uploadwin,textvar=std,width=50)
                    stdentry.place(x=200,y=160)

                    chaplab= Label(uploadwin,text="CHAPTER NAME")
                    chaplab.place(x=100,y=200)
                    chapentry= Entry(uploadwin,textvar=chap,width=50)
                    chapentry.place(x=200,y=200)


                    urllab= Label(uploadwin,text="VIDEO LINK")
                    urllab.place(x=100,y=240)
                    urlentry= Entry(uploadwin,textvar=url,width=50)
                    urlentry.place(x=200,y=240)
                    def upload():
                            
                        mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="mimityson",
                                    database="__edu_database__"
                                    )

                        mycursor = mydb.cursor()


                        sql = "INSERT INTO busi_vid (class,chapter_name,url) VALUES (%s,%s, %s )"
                        val = (st.get(),chap.get(),url.get())
                        mycursor.execute(sql, val)

                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo(title='account saved', message='congratulation your video is uploaded !!!')




                    upload= Button(uploadwin,text="upload",width=30,command= upload)
                    upload.place(x=200,y=290)
                    uploadwin.mainloop()
                        
                elif subject == "English":
                        
                    uploadwin = Toplevel()
                    uploadwin.geometry("600x400")
                    uploadwin.minsize(500,300)
                    uploadwin.maxsize(900,600)

                    img=PhotoImage(file="kv logo.png")
                    img1=PhotoImage(file="kv logo.png")
                    mainlab= Label(uploadwin,text="UPLOAD",bg="yellow",fg="black",font="calibre 60")
                    mainlab.pack()
                    mainlab["compound"]= LEFT,
                    mainlab["image"]= img

                    st= StringVar()
                    chap= StringVar()
                    url= StringVar()

                    std = Label(uploadwin,text="CLASS")
                    std.place(x=100,y=160)
                    stdentry= Entry(uploadwin,textvar=std,width=50)
                    stdentry.place(x=200,y=160)

                    chaplab= Label(uploadwin,text="CHAPTER NAME")
                    chaplab.place(x=100,y=200)
                    chapentry= Entry(uploadwin,textvar=chap,width=50)
                    chapentry.place(x=200,y=200)


                    urllab= Label(uploadwin,text="VIDEO LINK")
                    urllab.place(x=100,y=240)
                    urlentry= Entry(uploadwin,textvar=url,width=50)
                    urlentry.place(x=200,y=240)
                    def upload():
                            
                        mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="mimityson",
                                    database="__edu_database__"
                                    )

                        mycursor = mydb.cursor()


                        sql = "INSERT INTO eng_vid (class,chapter_name,url) VALUES (%s,%s, %s )"
                        val = (st.get(),chap.get(),url.get())
                        mycursor.execute(sql, val)

                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo(title='account saved', message='congratulation your video is uploaded !!!')




                    upload= Button(uploadwin,text="upload",width=30,command= upload)
                    upload.place(x=200,y=290)
                    uploadwin.mainloop()
                        
                        
                elif subject == "Hindi":
                        
                    uploadwin = Toplevel()
                    uploadwin.geometry("600x400")
                    uploadwin.minsize(500,300)
                    uploadwin.maxsize(900,600)

                    img=PhotoImage(file="kv logo.png")
                    img1=PhotoImage(file="kv logo.png")
                    mainlab= Label(uploadwin,text="UPLOAD",bg="yellow",fg="black",font="calibre 60")
                    mainlab.pack()
                    mainlab["compound"]= LEFT,
                    mainlab["image"]= img

                    st= StringVar()
                    chap= StringVar()
                    url= StringVar()

                    std = Label(uploadwin,text="CLASS")
                    std.place(x=100,y=160)
                    stdentry= Entry(uploadwin,textvar=std,width=50)
                    stdentry.place(x=200,y=160)

                    chaplab= Label(uploadwin,text="CHAPTER NAME")
                    chaplab.place(x=100,y=200)
                    chapentry= Entry(uploadwin,textvar=chap,width=50)
                    chapentry.place(x=200,y=200)


                    urllab= Label(uploadwin,text="VIDEO LINK")
                    urllab.place(x=100,y=240)
                    urlentry= Entry(uploadwin,textvar=url,width=50)
                    urlentry.place(x=200,y=240)
                    def upload():
                            
                        mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="mimityson",
                                    database="__edu_database__"
                                    )

                        mycursor = mydb.cursor()


                        sql = "INSERT INTO hindi_vid (class,chapter_name,url) VALUES (%s,%s, %s )"
                        val = (st.get(),chap.get(),url.get())
                        mycursor.execute(sql, val)

                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo(title='account saved', message='congratulation your video is uploaded !!!')




                    upload= Button(uploadwin,text="upload",width=30,command= upload)
                    upload.place(x=200,y=290)
                    uploadwin.mainloop()
                        
                        
                elif subject == "Informatic_Practices":
                        
                    uploadwin = Toplevel()
                    uploadwin.geometry("600x400")
                    uploadwin.minsize(500,300)
                    uploadwin.maxsize(900,600)

                    img=PhotoImage(file="kv logo.png")
                    img1=PhotoImage(file="kv logo.png")
                    mainlab= Label(uploadwin,text="UPLOAD",bg="yellow",fg="black",font="calibre 60")
                    mainlab.pack()
                    mainlab["compound"]= LEFT,
                    mainlab["image"]= img

                    st= StringVar()
                    chap= StringVar()
                    url= StringVar()

                    std = Label(uploadwin,text="CLASS")
                    std.place(x=100,y=160)
                    stdentry= Entry(uploadwin,textvar=std,width=50)
                    stdentry.place(x=200,y=160)

                    chaplab= Label(uploadwin,text="CHAPTER NAME")
                    chaplab.place(x=100,y=200)
                    chapentry= Entry(uploadwin,textvar=chap,width=50)
                    chapentry.place(x=200,y=200)


                    urllab= Label(uploadwin,text="VIDEO LINK")
                    urllab.place(x=100,y=240)
                    urlentry= Entry(uploadwin,textvar=url,width=50)
                    urlentry.place(x=200,y=240)
                    def upload():
                            
                        mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="mimityson",
                                    database="__edu_database__"
                                       )

                        mycursor = mydb.cursor()


                        sql = "INSERT INTO ip_vid (class,chapter_name,url) VALUES (%s,%s, %s )"
                        val = (st.get(),chap.get(),url.get())
                        mycursor.execute(sql, val)

                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo(title='account saved', message='congratulation your video is uploaded !!!')




                    upload= Button(uploadwin,text="upload",width=30,command= upload)
                    upload.place(x=200,y=290)
                    uploadwin.mainloop()
                        
                elif subject == "Chemistry":
                        
                    uploadwin = Toplevel()
                    uploadwin.geometry("600x400")
                    uploadwin.minsize(500,300)
                    uploadwin.maxsize(900,600)

                    img=PhotoImage(file="kv logo.png")
                    img1=PhotoImage(file="kv logo.png")
                    mainlab= Label(uploadwin,text="UPLOAD",bg="yellow",fg="black",font="calibre 60")
                    mainlab.pack()
                    mainlab["compound"]= LEFT,
                    mainlab["image"]= img

                    st= StringVar()
                    chap= StringVar()
                    url= StringVar()

                    std = Label(uploadwin,text="CLASS")
                    std.place(x=100,y=160)
                    stdentry= Entry(uploadwin,textvar=std,width=50)
                    stdentry.place(x=200,y=160)

                    chaplab= Label(uploadwin,text="CHAPTER NAME")
                    chaplab.place(x=100,y=200)
                    chapentry= Entry(uploadwin,textvar=chap,width=50)
                    chapentry.place(x=200,y=200)


                    urllab= Label(uploadwin,text="VIDEO LINK")
                    urllab.place(x=100,y=240)
                    urlentry= Entry(uploadwin,textvar=url,width=50)
                    urlentry.place(x=200,y=240)
                    def upload():
                            
                        mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="mimityson",
                                    database="__edu_database__"
                                    )

                        mycursor = mydb.cursor()


                        sql = "INSERT INTO chem_vid (class,chapter_name,url) VALUES (%s,%s, %s )"
                        val = (st.get(),chap.get(),url.get())
                        mycursor.execute(sql, val)

                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo(title='account saved', message='congratulation your video is uploaded !!!')




                    upload= Button(uploadwin,text="upload",width=30,command= upload)
                    upload.place(x=200,y=290)
                    uploadwin.mainloop()
                        
                        
                elif subject == "Maths":
                        
                    uploadwin = Toplevel()
                    uploadwin.geometry("600x400")
                    uploadwin.minsize(500,300)
                    uploadwin.maxsize(900,600)

                    img=PhotoImage(file="kv logo.png")
                    img1=PhotoImage(file="kv logo.png")
                    mainlab= Label(uploadwin,text="UPLOAD",bg="yellow",fg="black",font="calibre 60")
                    mainlab.pack()
                    mainlab["compound"]= LEFT,
                    mainlab["image"]= img

                    st= StringVar()
                    chap= StringVar()
                    url= StringVar()

                    std = Label(uploadwin,text="CLASS")
                    std.place(x=100,y=160)
                    stdentry= Entry(uploadwin,textvar=std,width=50)
                    stdentry.place(x=200,y=160)

                    chaplab= Label(uploadwin,text="CHAPTER NAME")
                    chaplab.place(x=100,y=200)
                    chapentry= Entry(uploadwin,textvar=chap,width=50)
                    chapentry.place(x=200,y=200)


                    urllab= Label(uploadwin,text="VIDEO LINK")
                    urllab.place(x=100,y=240)
                    urlentry= Entry(uploadwin,textvar=url,width=50)
                    urlentry.place(x=200,y=240)
                    def upload():
                            
                        mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="mimityson",
                                    database="__edu_database__"
                                    )

                        mycursor = mydb.cursor()


                        sql = "INSERT INTO math_vid (class,chapter_name,url) VALUES (%s,%s, %s )"
                        val = (st.get(),chap.get(),url.get())
                        mycursor.execute(sql, val)

                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo(title='account saved', message='congratulation your video is uploaded !!!')




                    upload= Button(uploadwin,text="upload",width=30,command= upload)
                    upload.place(x=200,y=290)
                    uploadwin.mainloop()
                        
                elif subject == "Biology":
                        
                    uploadwin = Toplevel()
                    uploadwin.geometry("600x400")
                    uploadwin.minsize(500,300)
                    uploadwin.maxsize(900,600)

                    img=PhotoImage(file="kv logo.png")
                    img1=PhotoImage(file="kv logo.png")
                    mainlab= Label(uploadwin,text="UPLOAD",bg="yellow",fg="black",font="calibre 60")
                    mainlab.pack()
                    mainlab["compound"]= LEFT,
                    mainlab["image"]= img

                    st= StringVar()
                    chap= StringVar()
                    url= StringVar()

                    std = Label(uploadwin,text="CLASS")
                    std.place(x=100,y=160)
                    stdentry= Entry(uploadwin,textvar=std,width=50)
                    stdentry.place(x=200,y=160)

                    chaplab= Label(uploadwin,text="CHAPTER NAME")
                    chaplab.place(x=100,y=200)
                    chapentry= Entry(uploadwin,textvar=chap,width=50)
                    chapentry.place(x=200,y=200)


                    urllab= Label(uploadwin,text="VIDEO LINK")
                    urllab.place(x=100,y=240)
                    urlentry= Entry(uploadwin,textvar=url,width=50)
                    urlentry.place(x=200,y=240)
                    def upload():
                            
                        mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="mimityson",
                                    database="__edu_database__"
                                    )

                        mycursor = mydb.cursor()


                        sql = "INSERT INTO bio_vid (class,chapter_name,url) VALUES (%s,%s, %s )"
                        val = (st.get(),chap.get(),url.get())
                        mycursor.execute(sql, val)

                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo(title='account saved', message='congratulation your video is uploaded !!!')




                    upload= Button(uploadwin,text="upload",width=30,command= upload)
                    upload.place(x=200,y=290)
                    uploadwin.mainloop()
                        
                        
                        
                elif subject == "Physics":
                        
                        
                    uploadwin = Toplevel()
                    uploadwin.geometry("600x400")
                    uploadwin.minsize(500,300)
                    uploadwin.maxsize(900,600)

                    img=PhotoImage(file="kv logo.png")
                    img1=PhotoImage(file="kv logo.png")
                    mainlab= Label(uploadwin,text="UPLOAD",bg="yellow",fg="black",font="calibre 60")
                    mainlab.pack()
                    mainlab["compound"]= LEFT,
                    mainlab["image"]= img

                    st= StringVar()
                    chap= StringVar()
                    url= StringVar()

                    std = Label(uploadwin,text="CLASS")
                    std.place(x=100,y=160)
                    stdentry= Entry(uploadwin,textvar=std,width=50)
                    stdentry.place(x=200,y=160)

                    chaplab= Label(uploadwin,text="CHAPTER NAME")
                    chaplab.place(x=100,y=200)
                    chapentry= Entry(uploadwin,textvar=chap,width=50)
                    chapentry.place(x=200,y=200)


                    urllab= Label(uploadwin,text="VIDEO LINK")
                    urllab.place(x=100,y=240)
                    urlentry= Entry(uploadwin,textvar=url,width=50)
                    urlentry.place(x=200,y=240)
                    def upload():
                            
                        mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="mimityson",
                                    database="__edu_database__"
                                    )

                        mycursor = mydb.cursor()


                        sql = "INSERT INTO phy_vid (class,chapter_name,url) VALUES (%s,%s, %s )"
                        val = (st.get(),chap.get(),url.get())
                        mycursor.execute(sql, val)

                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo(title='account saved', message='congratulation your video is uploaded !!!')




                    upload= Button(uploadwin,text="upload",width=30,command= upload)
                    upload.place(x=200,y=290)
                    uploadwin.mainloop()
                        
                            
                            
                    
                    
                elif subject == "Economics":
                        
                        
                    uploadwin = Toplevel()
                    uploadwin.geometry("600x400")
                    uploadwin.minsize(500,300)
                    uploadwin.maxsize(900,600)

                    img=PhotoImage(file="kv logo.png")
                    img1=PhotoImage(file="kv logo.png")
                    mainlab= Label(uploadwin,text="UPLOAD",bg="yellow",fg="black",font="calibre 60")
                    mainlab.pack()
                    mainlab["compound"]= LEFT,
                    mainlab["image"]= img

                    st= StringVar()
                    chap= StringVar()
                    url= StringVar()

                    std = Label(uploadwin,text="CLASS")
                    std.place(x=100,y=160)
                    stdentry= Entry(uploadwin,textvar=std,width=50)
                    stdentry.place(x=200,y=160)

                    chaplab= Label(uploadwin,text="CHAPTER NAME")
                    chaplab.place(x=100,y=200)
                    chapentry= Entry(uploadwin,textvar=chap,width=50)
                    chapentry.place(x=200,y=200)


                    urllab= Label(uploadwin,text="VIDEO LINK")
                    urllab.place(x=100,y=240)
                    urlentry= Entry(uploadwin,textvar=url,width=50)
                    urlentry.place(x=200,y=240)
                    def upload():
                            
                        mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="mimityson",
                                    database="__edu_database__"
                                    )

                        mycursor = mydb.cursor()


                        sql = "INSERT INTO eco_vid (class,chapter_name,url) VALUES (%s,%s, %s )"
                        val = (st.get(),chap.get(),url.get())
                        mycursor.execute(sql, val)

                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo(title='account saved', message='congratulation your video is uploaded !!!')




                    upload= Button(uploadwin,text="upload",width=30,command= upload)
                    upload.place(x=200,y=290)
                    uploadwin.mainloop()
                        
                    
                    
                    
            def logout():
                login_.destroy()

            profile_btn= Button(login_,text="PROFILE",width=18,command= __profile__ )
            profile_btn.place(x=0,y=0)

            home_btn= Button(login_,text="HOME",width=18)
            home_btn.place(x=135,y=0)

            library_btn= Button(login_,text="UPLOAD",width=18,command= upload)
            library_btn.place(x=270,y=0)

            logout_btn= Button(login_,text="LOGOUT",width=12,command= logout)
            logout_btn.place(x=405,y=0)
            login_.mainloop()
            
                
            

                
            
            
    def crtteacher():

        var1=StringVar()
        tid=StringVar()
        tname=StringVar()
        tsubject=StringVar()
        sub_code=StringVar()
        username=StringVar()
        password=StringVar()
        kvname=StringVar()
    
    
        crt_teacher= Toplevel()
        crt_teacher.geometry("900x700+150+150")
        crt_teacher.minsize(700,700)
        crt_teacher.maxsize(700,700)
        crt_teacher.title('CREATE ACCOUNT')

        label_1=Label(crt_teacher,text="NEW TEACHER ACCOUNT",font=("calibre",40),bg="pink")
        label_1.pack()
        label_2=Label(crt_teacher,text="name of teacher",font="40")
        label_2.place(x=50, y =100)
        label_3=Label(crt_teacher,text="subject name",font="40")
        label_3.place(x=50,y=130)
        label_4=Label(crt_teacher,text="subject code",font=40)
        label_4.place(x=50,y=160)
        label_5=Label(crt_teacher,text="kv name",font="40,bold")
        label_5.place(x=50,y=185)
        label_6= Label(crt_teacher,text="username",font="40")
        label_6.place(x=50,y=220)
        label_7= Label(crt_teacher,text="password",font="40")
        label_7.place(x=50,y=250)

        name_entry_1=Entry(crt_teacher,textvar=tname ,width=20)
        name_entry_1.place(x=200 ,y=100)
        class_entry_2=Entry(crt_teacher,textvar=tsubject,width=20)
        class_entry_3=Entry(crt_teacher,textvar=sub_code,width=20)
        class_entry_2.place(x=200,y=130)
        class_entry_3.place(x=200,y=160)
        user_entry= Entry(crt_teacher,textvar=username)
        user_entry.place(x=200,y=220)
        pass_entry=Entry(crt_teacher,textvar=password)
        pass_entry.place(x=200,y=250)
        kv_entry= Entry(crt_teacher,textvar=kvname)
        kv_entry.place(x=200,y=185)

        import string ,secrets,random

        #select a uppercase
        upper=secrets.choice(string.ascii_uppercase)
        # select a lowercase
        lower=secrets.choice(string.ascii_lowercase)
        # select a number
        digit=secrets.choice(string.digits)
        # put the selected 3 char together
        selected_chars=list()
        selected_chars.extend(upper)
        selected_chars.extend(lower)
        selected_chars.extend(digit)
        #select rest chars in all allowed chars:6-3=3
        allowedchars = upper + lower + digit
        selected_rest_chars = [secrets.choice(allowedchars)for _ in range(5)]
        # put the selected 3 chars with the rest 17 chars together
        selected_rest_chars.extend(selected_chars)
        #shuffle the 6 chars - this our id
        random.shuffle(selected_rest_chars)
        # combine the chars to our id
        s="".join(selected_rest_chars)


        var1.set(s)
        label= Label(crt_teacher,textvar=var1)
        label.place(x=250,y=300)
      


        label0=Label(crt_teacher,text="enter id in required box ")
        label0.place(x=10,y=300)
        studentid_label=Label(crt_teacher,text="here enter the id given to u ")
        studentid_label.place(x=10 , y=380)
        studentid_entry= Entry(crt_teacher,textvar=tid,width=30)
        studentid_entry.place(x=160,y=380)        

        def create_account ():
            import mysql.connector
            
    
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mimityson",
            database="__edu_database__"
            )

            mycursor = mydb.cursor()


            sql="INSERT INTO teachertable(ID,teacher_name,sub_name,sub_code,kv_name,username,password)VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (tid.get(),tname.get(),tsubject.get(),sub_code.get(),kvname.get(),username.get(),password.get())
            mycursor.execute(sql, val)

            mydb.commit()
            mydb.close()
            messagebox.showinfo(title='account saved', message='congratulation your account is saved !!!')

                                  

        std_button= Button(crt_teacher,text="create account",width=20,command= create_account )
        std_button.place(x=120,y=500)
        
        crt_teacher.mainloop()


    

                

    button = Button(root,text="cancel",command= __cancel__ )
    button.place(x=180,y=160)
    button_1=Button(root,text="login",command= login)
    button_1.place(x=250,y=160)
    button_2=Button(root,text="create an account",width="20" ,command= crtteacher)
    button_2.place(x=160,y=200)



    root.mainloop()


