from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess
rootst=Tk()
rootst.title('Staff Page')
def connect():
   try:
     global session
     session=mysql.connector.connect(host='127.0.0.1',user='root',passwd='password',database='hosteldb')
     messagebox.showinfo(title='Connection Sucessfull !',message='Connected to the database !!')
     return 0    
   except Exception as e:
      print(subprocess.getoutput(e))
      if(str(e)=='list index out of range'):
         messagebox.showerror(title='Invalid password',message='Invalid password !!')
      else:
         messagebox.showerror(title='Connection error',message='Connection failed \n'+str(e)+'\nTry Again!!')
      return 1
def exit():
    rootst.destroy()
def viewprofile():
    if(connect()==0):
        for widget in F1.winfo_children():
            widget.destroy()
        try:
            cur=session.cursor()
            query="select * from staff where EID in(select EID from passwd where username='"+uname+"' and post='staff');"
            session._execute_query(query)
            result=cur.fetchall()
            result=result[0]
            l=len(result)
            m=0
            for i in range(0,l):
                if(i==0):
                    PRN=Label(F1,text='PRN :',font=('Verdana',20),relief='flat',bd=3,background='#FFFFE0')
                    PRN.place(x=0,y=m)
                elif(i==1):
                    Name=Label(F1,text='Name :',font=('verdana',20),background='#FFFFE0',relief='flat')
                    Name.place(x=0,y=m)
                elif(i==2):
                    Addr=Label(F1,text='Address :',background='#FFFFE0',font=('Verdana',20),relief='flat',bd=3)
                    Addr.place(x=0,y=m)
                elif(i==3):
                    Mob=Label(F1,background='#FFFFE0',text='Mobile no. :',font=('Verdana',20),relief='flat',bd=3)
                    Mob.place(x=0,y=m)
                elif(i==4):
                    email=Label(F1,text='Email :',font=('Verdana',20),relief='flat',bd=3,background='#FFFFE0')
                    email.place(x=0,y=m)
                elif(i==5):
                    DOB=Label(F1,text='DOB :',font=('Verdana',20),relief='flat',bd=3,background='#FFFFE0')
                    DOB.place(x=0,y=m)
                elif(i==6):
                    Age=Label(F1,text='Age :',font=('Verdana',20),background='#FFFFE0',relief='flat',bd=3)
                    Age.place(x=0,y=m)
                elif(i==7):
                    gender=Label(F1,background='#FFFFE0',text='Gender :',font=('Verdana',20),relief='flat',bd=3)
                    gender.place(x=0,y=m)
                elif(i==8):
                    Prog=Label(F1,text='Salary :',font=('Verdana',20),relief='flat',bd=3,background='#FFFFE0')
                    Prog.place(x=0,y=m)
                L=Label(F1,text=result[i],font=('verdana',20),background='#FFFFE0')
                L.place(x=200,y=m)
                #print(subprocess.getoutput(str(result[i])))
                m=m+50
        except Exception as e:
            messagebox.showerror(message=str(e),title='Error !!')
def valid():
    if(str(v4.get())=='' or str(v5.get())=='' or str(v3.get())=='' or str(v6.get())==''):
        messagebox.showerror(title='Update Failed',message='Fill all available fields')
    elif(str(v4.get())!=str(v5.get())):
        messagebox.showinfo(title='Update failed',message='Please enter same password in both the boxes')
    elif(len(str(v4.get))<8 or len(str(v5.get))<8 or len(str(v3.get()))<8):
        messagebox.showerror(title='Update failed',message='Password should be greater than 8 characters')
    else:
        if(connect()==0):
            try:
                query="update passwd set password= '"+str(v4.get())+"' where username='"+str(v6.get())+"' and post ='staff';"
                session._execute_query(query)
                session.commit()
                messagebox.showinfo(title='Update Sucessfull',message='Password updated sucessfully')
            except Exception as e:
                messagebox.showerror(title='Update failed',message=str(e))
def update():
    for widget in F1.winfo_children():
        widget.destroy()
    global v3
    v3=StringVar()
    global v4
    v4=StringVar()
    global v5
    global v6
    v6=StringVar()
    v5=StringVar()
    L1=Label(F1,text="Enter old password  :",font=('verdana',20),relief='flat',background='#FFFFE0',bd=3)
    E1=Entry(F1,bd=10,relief='flat',textvariable=v3)
    L6=Label(F1,text="Enter username :",font=('verdana',20),relief='flat',background='#FFFFE0',bd=3)
    E6=Entry(F1,bd=10,relief='flat',textvariable=v6)
    L6.place(x=200,y=10)
    E6.place(x=500,y=10)
    L2=Label(F1,text="Enter new password :",font=('verdana',20),relief='flat',background='#FFFFE0',bd=3)
    E2=Entry(F1,bd=10,relief='flat',textvariable=v4)
    L3=Label(F1,bd=3,relief='flat',font=('verdana',20),text="Confirm password    :",background='#FFFFE0')
    E3=Entry(F1,bd=10,relief='flat',textvariable=v5)
    L1.place(x=200,y=100)
    E1.place(x=500,y=100)
    L2.place(x=200,y=200)
    E2.place(x=500,y=200)
    L3.place(x=200,y=300)
    E3.place(x=500,y=300)
    B1=Button(F1,text='Submit',relief='raised',bd=3,command=valid,font=('verdana',20))
    B1.place(x=800,y=200)
canvas=Canvas(rootst,height=1080,width=1920,background='#FFFFE0')
file=open('login.txt',"r")
global uname
uname=file.readline()
uname=uname.strip()
file.close()
welcometext='Welcome , '+uname
L1=Label(canvas,text=welcometext,relief='raised',bd=-1,background='#FFFFE0',fg='#000000',font=('verdana',10),anchor=W)
L1.place(x=1150,y=50)
canvas.create_text(700,50,text='Choose an action to perform',font=('Verdana',30),fill='#191970')
b1=Button(canvas,text='View profile',command=viewprofile,font=('verdana',20),relief='raised',bd=3)
canvas.create_window(400,140,window=b1)
b2=Button(canvas,text='Update password',command=update,font=('verdana',20),relief='raised',bd=3)
canvas.create_window(900,140,window=b2)
b3=Button(canvas,text='Exit',command=exit,font=('verdana',20),relief='raised',bd=3)
canvas.create_window(600,650,window=b3) 
F1=Frame(canvas,width=1920,height=450,bg='#FFFFE0',highlightcolor='#FFFFFF',cursor='circle')
F1.place(x=0,y=170)                
canvas.pack()
rootst.mainloop()