from tkinter import *
from tkinter import messagebox

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

        


    