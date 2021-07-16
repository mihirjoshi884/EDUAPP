""" EDU_APP is a educational app which contain educational videos 
    and notes for students who are in class 11th and class 12th.
    courses are available for all students who are in science + maths
    science + bio, commerce + maths , commerce + IP.

    for building app manny packages are used like- Graphical User Inteface (GUI-tkinter), 
    MY SQL CONNECTOR  , RANDOM MODULE , SECRETS MODULE , STRING MODULE ,

    My app works basically on tkinter . tkinter is a python module which runs basically  on graphical user interface .
    tkinter helps  in  presenting python program in impressive and presentable manner so that IT and non IT- user can
    easily interact and access  with  the program with out understanding it's source code .
    

    tkinter basic format is -                   
                                                from tkinter import *  -- (here we import each and every methods which are
                                                                            defined in the module . instead of this way we 
                                                                            can import tkinter by--import tkinter but it 
                                                                            will always take more steps for using it's 
                                                                            method . 
                                                                            EXAMPLE- 

                                                                            [1]  from tkinter import * :
                                                                                           
                                                                                we can use - Label function as
                                                                                     root=Tk()
                                                                                     l1= Label(root,text="label name")
                                                                                     l1.pack()

                                                                            [2]  import tkinter as tk :
                                                                                 but in this method we have to use label 
                                                                                 function as 

                                                                                    root=tk.Tk()
                                                                                    l1= tk.label(root,text="label name")
                                                                                    l1.pack()      

                                                root= Tk()              ( important code must be written in between these 
                                                                          these lines. )
                                                

                                                root.mainloop()
"""

import tkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox
import teacherslogin 
from teacherslogin import teacherwin
import admin
from admin import __admin_login__
import vidplaymethods 
from vidplaymethods import accounts,biology,business,maths,economics
from vidplaymethods import hindi,english,physics,chemistry,Informatic_Practices



def main():

    root=Tk()
    root.geometry("500x300+150+150")
    root.minsize(500,300)
    root.maxsize(500,300)
    studentid=StringVar() 
    unm=StringVar()
    pwd=StringVar()

    dname=""
    dstd=""
    dstream=""
    dusrname=""
    dusrpass=""
    dgender=""
    did=""


    

    label_id= Label(root,text="student ID",font="40")
    label_id.place(x=100,y=40)
    label= Label(root,text="username",font=40)
    label.place(x=100,y=70)
    label_1= Label(root,text="password",font=40)
    label_1.place(x=100,y=100)


    entry=Entry(root,textvar=unm)
    entry.place(x=180,y=70)
    entry_1=Entry(root,textvar=pwd)
    entry_1.place(x=180,y=100)
    entry_id= Entry(root,textvar=studentid)
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


    """here we use very important function of tkinter module which is Toplevel(). This function mainly help in 
    opening a new GUI window with a button .

            This widget is directly controlled by the window manager. It don’t need any parent window to work on.
            The general syntax is:

                            w = TopLevel(master, option=value)
    
                    
    
    """

    def login():
        print("inside login....")
        # studentid=StringVar() 
        # username=StringVar()
        # password=StringVar()

        dname=""
        dstd=""
        dstream=""
        dusrname=""
        dusrpass=""
        dgender=""
        did=""
        
        try:
            mycon= mysql.connector.connect(host='localhost',
                                            database='__edu_database__',
                                            user='root',
                                            password='mimityson',
                                    )
        
            cur= mycon.cursor()
            stdid= (studentid.get())
            print(stdid)
            sqlvar = "select * from stdinfo where ID = '{}' ".format(stdid)
            print(sqlvar)
            cur.execute(sqlvar)


            apple= cur.fetchall()
            for i in apple:
                print(i)
                did=i[0]
                dname=i[1]
                dstd=i[2]
                dstream=i[3]
                dgender=i[4]
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


            classlab= Label(login_,text="class-12",width=50,height=50)
            classlab.pack()

            def __home__():

                

                home= Toplevel()
                home.geometry("500x300+150+150")
                home.minsize(500,300)
                home.maxsize(500,300)

                

                
                if dstream == "commerce":

                    commercelab=Label(home,text="COMMERCE",font=("calibre",30),bg="light salmon",width=40,fg="green")
                    commercelab.pack()

                    account_l1= Button(home,text="ACCOUNTS",width=20,command= accounts)
                    account_l1.place(x=150,y=50)

                    business_b1= Button(home,text="BUSINESS",width=20,command=business)
                    business_b1.place(x=150,y=100)


                    economics_b2= Button(home,text="ECONOMICS",width=20,command= economics)
                    economics_b2.place(x=150,y=150)


                    english_b3= Button(home,text="ENGLISH",width=20,command= english)
                    english_b3.place(x=150,y=200)


                    hindi= Button(home,text="hindi",width=20)
                    hindi.place(x=150,y=250)

                    ip= Button(home,text="INFORMATIC PRACTICES",command= Informatic_Practices)
                    ip.place(x=150,y=275)

                else :
            
                    if dstream == "science+maths":

                        mathlab=Label(home,text="SCIENCE + MATHS",font=("calibre",30),bg="lightgreen",width=40,fg="yellow")
                        mathlab.pack()


                        physics_l1= Button(home,text="PHYSICS",width=20, command= physics)
                        physics_l1.place(x=150,y=50)

                        chemistry_b1= Button(home,text="CHEMISTRY",width=20,command= chemistry)
                        chemistry_b1.place(x=150,y=100)


                        maths_b2= Button(home,text="MATHS",width=20,command= maths)
                        maths_b2.place(x=150,y=150)


                        english_b3= Button(home,text="ENGLISH",width=20, command=english)
                        english_b3.place(x=150,y=200)


                        hindi= Button(home,text="OTHER SUBJECTS",width=20,command= hindi )
                        hindi.place(x=150,y=250)


                        ip= Button(home,text="INFORMATIC PRACTICES",command= Informatic_Practices)
                        ip.place(x=150,y=275)

                    else:
        
        
                        biolab=Label(home,text="SCIENCE+BIOLOGY",font=("calibre",30),bg="lightgreen",width=40,fg="yellow")
                        biolab.pack()


                        physics_l1= Button(home,text="PHYSICS",width=20,command= physics)
                        physics_l1.place(x=150,y=50)

                        chemistry_b1= Button(home,text="CHEMISTRY",width=20,command= chemistry)
                        chemistry_b1.place(x=150,y=100)


                        biology_b2= Button(home,text="BIOLOGY",width=20,command= biology)
                        biology_b2.place(x=150,y=150)


                        english_b3= Button(home,text="ENGLISH",width=20,command= english)
                        english_b3.place(x=150,y=200)


                        hindi= Button(home,text="HINDI",width=20,command=hindi)
                        hindi.place(x=150,y=250)

        



                home.mainloop()

            def __profile__():
                global dname
                global dstd
                global dstream
                global dusrname
                global dusrpass
                global dgender
                global did


                try:
                    mycon= mysql.connector.connect(host='localhost',
                                                    database='__edu_database__',
                                                    user='root',
                                                    password='mimityson',
                                                    )
        
                    cur= mycon.cursor()
                    stdid= (studentid.get())
                    sqlvar = "select * from stdinfo where ID = '{}' ".format(stdid)
                    cur.execute(sqlvar)


                    apple= cur.fetchall()
                    for i in apple:
                        
                        did=i[0]
                        dname=i[1]
                        dstd=i[2]
                        dstream=i[3]
                        dgender=i[4]
                        dusrname=i[5]
                        dusrpass=i[6]

                    cur.close()
                    mycon.close()

                except:      
                    messagebox.showerror(title='login error', message='Error while connecting to MySQL')

                _id= did
                
                _name= dname
                
                _gender= dgender
                
                _standard= dstd
            
                _stream= dstream
                
                _usrname= dusrname
        
                _usrpass= dusrpass
                
                
                profile= Tk()
                profile.geometry("500x300+150+150")
                profile.minsize(500,300)
                profile.maxsize(500,300)

                profilelab=Label(profile,text="PROFILE",font=("calibre",30),bg="lightgreen",width=40,fg="yellow")
                profilelab.pack()

                stidlabel=  Label(profile,text="student idcode",bg="purple4",fg="white")
                stidlabel.place(x=50,y=75)
                stidlabel1=  Label(profile,text= _id,bg="purple4",fg="white" )
                stidlabel1.place(x=350,y=75)

                namelabel= Label(profile,text="name of the student",bg="red",fg="misty rose")
                namelabel.place(x=50,y=100)
                namelabel1= Label(profile,text= _name,bg="red",fg="misty rose")
                namelabel1.place(x=350,y=100)

                genderlabel= Label(profile,text="gender",bg="light salmon",fg="purple3")
                genderlabel.place(x=50,y=125)
                genderlabel1= Label(profile,text= _gender,bg="light salmon",fg="purple3")
                genderlabel1.place(x=350,y=125)

                standardlabel= Label(profile,text="standard",bg="yellow",fg="green2")
                standardlabel.place(x=50,y=150)
                standardlabel1= Label(profile,text= _standard,bg="yellow",fg="green2")
                standardlabel1.place(x=350,y=150)

                streamlabel= Label(profile,text="stream",bg="cornsilk3",fg="black")
                streamlabel.place(x=50,y=175)
                streamlabel1= Label(profile,text=_stream,bg="cornsilk3",fg="black")
                streamlabel1.place(x=350,y=175)

                usernamelabel= Label(profile,text="username",bg="lavender",fg="DarkGoldenrod2")
                usernamelabel.place(x=50,y=200)
                usernamelabel1= Label(profile,text= _usrname,bg="lavender",fg="DarkGoldenrod2")
                usernamelabel1.place(x=350,y=200)

                passwordlabel= Label(profile,text="password",bg="powder blue",fg="purple4")
                passwordlabel.place(x=50,y=225)
                passwordlabel1= Label(profile,text= _usrpass,bg="powder blue",fg="purple4")
                passwordlabel1.place(x=350,y=225)


                profile.mainloop()

            def logout():
                login_.destroy()
                    
                

            profile_btn= Button(login_,text="PROFILE",width=18,command= __profile__)
            profile_btn.place(x=0,y=0)

            home_btn= Button(login_,text="HOME",width=18,command= __home__)
            home_btn.place(x=135,y=0)

            library_btn= Button(login_,text="LIBRARY",width=18)
            library_btn.place(x=270,y=0)

            logout_btn= Button(login_,text="LOGOUT",width=12,command=logout)
            logout_btn.place(x=405,y=0)
            login_.mainloop()
            
        
        else:
        
            messagebox.showerror(title='login error', message='username/password is incorrect')


            


            
    def  __create_account__ ():


        """ __create_account__(): this method help in to go to  account creation page so that he can registre himself with
                                this app 

        """

        tp=Toplevel()
        tp.geometry("500x700+150+150")
        tp.minsize(400,700)
        tp.maxsize(400,700)
        tp.title('CREATE ACCOUNT')

        sname=StringVar()
        sclass=StringVar()
        stream=StringVar()
        gender=StringVar()
        var1=StringVar()
        sid=StringVar()
        username=StringVar()
        password=StringVar()

        label_1=Label(tp,text="NEW ACCOUNT",font=("calibre",40),bg="lightgreen")
        label_1.pack()
        label_2=Label(tp,text="name of student",font="40")
        label_2.place(x=10 , y =100)
        label_3=Label(tp,text="class",font="40")
        label_3.place(x=50,y=130)
        label_4=Label(tp,text="stream",font=40)
        label_4.place(x=50,y=160)
        label_5=Label(tp,text="gender   -",font="40,bold")
        label_5.place(x=50,y=185)
        label_6= Label(tp,text="username",font="40")
        label_6.place(x=50,y=220)
        label_7= Label(tp,text="password",font="40")
        label_7.place(x=50,y=250)

        name_entry_1=Entry(tp,textvar=sname ,width=20)
        name_entry_1.place(x=130 ,y=100)
        class_entry_2=Entry(tp,textvar=sclass,width=20)
        class_entry_3=Entry(tp,textvar=stream,width=20)
        class_entry_2.place(x=130,y=130)
        class_entry_3.place(x=130,y=160)
        user_entry= Entry(tp,textvar=username)
        user_entry.place(x=130,y=220)
        pass_entry=Entry(tp,textvar=password)
        pass_entry.place(x=130,y=250)
            
                
        """
        below code  helps in generating unique student id for std_id which is a primary key
        of table - stdinfo which belongs to  database - __edu_database__ .
        In this function string , secerets , random module are used to build random and unique id .

        STRING MODULE - The string module contains a number of useful constants and classes .
                        deprecated legacy functions that are also available as methods on strings.
                        In addition, Python’s built-in string classes support the sequence type methods described in the Sequence .
                        this types — str, unicode, list, tuple,etc. and also the string-specific methods described in the String Methods section.

        SECRETES MODULE - The secrets module is used for generating cryptographically strong random
                        numbers suitable for managing data such as passwords, account authentication,
                        security tokens, and related secrets.

                        In particularly, secrets should be used in preference to the default pseudo-random
                        number generator in the random module, which is designed for modelling and simulation,
                        not security or cryptography.

        RANDOM MODULE -  This module implements pseudo-random number generators for various distributions.

                        For integers, there is uniform selection from a range. For sequences, there is uniform
                        selection of a random element, a function to generate a random permutation of a list in-place,
                        and a function for random sampling without replacement.

        """
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
        selected_rest_chars = [secrets.choice(allowedchars)for _ in range(7)]
        # put the selected 3 chars with the rest 17 chars together
        selected_rest_chars.extend(selected_chars)
        #shuffle the 6 chars - this our id
        random.shuffle(selected_rest_chars)
        # combine the chars to our id
        s="".join(selected_rest_chars)

            
        var1.set(s)
        label= Label(tp,textvar=var1)
        label.place(x=250,y=300)
        


        label0=Label(tp,text="enter id in required box ")
        label0.place(x=10,y=300)
        studentid_label=Label(tp,text="here enter the id given to u ")
        studentid_label.place(x=10 , y=380)
        studentid_entry= Entry(tp,textvar=sid,width=30)
        studentid_entry.place(x=160,y=380)        
        gender_entry= Entry(tp,textvar=gender)
        gender_entry.place(x=130,y=185)
            

        def create_account ():

            """ create_account(): this method helps in registering the user account in the database of the app
                                this will give  authorisation to the user so that he /she can access the feature of this 
                                app.
            """



            import mysql.connector

            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mimityson",
            database="__edu_database__"
            )

            mycursor = mydb.cursor()


            sql = "INSERT INTO stdinfo (ID,name_student,standard,stream,gender,username,password) VALUES (%s, %s ,%s,%s,%s,%s,%s)"
            val = (sid.get(),sname.get(),sclass.get(),stream.get(),gender.get(),username.get(),password.get())
            mycursor.execute(sql, val)

            mydb.commit()
            mydb.close()
            messagebox.showinfo(title='account saved', message='congratulation your account is saved !!!')

                                    

        std_button= Button(tp,text="create account",width=20,command= create_account )
        std_button.place(x=120,y=500)

        tp.mainloop()

        
    button = Button(root,text="cancel",command= __cancel__ )
    button.place(x=180,y=160)
    button_1=Button(root,text="login",command= login)
    button_1.place(x=250,y=160)
    button_2=Button(root,text="create an account",width="20" ,command= __create_account__ )
    button_2.place(x=160,y=200)
    button_3=Button(root,text="login as admin",width=12,command= __admin_login__)
    button_3.place(x=400,y=10)
    button_4= Button(root,text="login as teacher",command= teacherwin)
    button_4.place(x=400,y=35)


    root.mainloop()

if __name__ == "__main__":

    main()
