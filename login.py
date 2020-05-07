from tkinter import *
import subprocess
import os
import datetime
from tkinter import messagebox
import mysql.connector
root=Tk()
root.title('MITAOE Hostel Login Page')
def connect():
   try:
     global session
     session=mysql.connector.connect(host='127.0.0.1',user='root',passwd='password',database='hosteldb')
     messagebox.showinfo(title='Connection Sucessfull !',message='Connected to the database !!')
     return 0    
   except Exception as e:
      messagebox.showerror(title='Connection error',message='Connection failed \n'+str(e)+'\nTry Again!!')
      return 1
def valid(v1,v2):
     if(v1.get()=='' or v2.get()==''):
        messagebox.showerror(title='Empty username or password',message='Username or password can not empty\nTry again!!!')
        return 1
     elif(len(v2.get())<8):
        messagebox.showerror(title='Invalid password',message='Invalid password..\nPassword should not less than 8 characters\nTry again!!!')
        return 1
     else :
        return 0
def show():
     global v1
     v1=StringVar()
     global v2
     v2=StringVar()
     l1=Label(canvas,text="Username :",font=('verdana',20),relief='flat',background="#E6E6FA",bd=3)
     l2=Label(canvas,text="Password :",font=('verdana',20),relief='flat',background="#E6E6FA",bd=3)
     canvas.create_window(400,450,window=l1)
     canvas.create_window(400,500,window=l2)
     e1=Entry(canvas,bd=10,relief='flat',textvariable=v1)
     e2=Entry(canvas,bd=10,relief='flat',show='*',textvariable=v2)
     canvas.create_window(600,450,window=e1)
     canvas.create_window(600,500,window=e2) 
     b1=Button(canvas,text='Submit',font=('verdana',20),relief='raised',bd=3,command=create_window)
     canvas.create_window(600,600,window=b1)    
def create_window():
     uname=str(v1.get())
     if(valid(v1,v2)==1):
        pass
     elif(connect()==1) :
        pass
     elif(var.get()==1):
        try:
         cur=session.cursor()
         ans=str(v2.get())
         print(subprocess.getoutput(ans))
         query=str("select password from passwd where username= '"+str(v1.get())+"' and post='student';")
         session._execute_query(query)
         result=cur.fetchall()
         result=str(result[0][0])
         print(subprocess.getoutput(result))
         if(result==ans):
            messagebox.showinfo(title='Login Sucessfull',message='You are loged in as student')
            file=open('login.txt',"w")
            file.write(uname+'\n')
            file.close()
            file=open('loginhistory.txt',"a")
            file.write(uname+'\t '+str(datetime.datetime.now())+'\n')
            file.close()
            root.destroy()
            os.system('python3 /home/admin-pc/Documents/DBMS\ project/student.py')
         else:
            raise Exception('Invalid username or password')
        except Exception as e:
           e1=str(e)
           print(subprocess.getoutput(e1))
           if(e1=='list index out of range'):
              messagebox.showerror(title='Authentication failure',message='Invalid username or password')
           messagebox.showerror(title='Authentication failure',message=str(e))
     elif (var.get()==3):
        try:
           cur=session.cursor()
           query=str("select password from passwd where username= '"+str(v1.get())+"' and post='staff';")
           ans=str(v2.get())
           session._execute_query(query)
           result=cur.fetchall()
           result=str(result[0][0])
           if(result==ans):
               messagebox.showinfo(title='Login Sucessfull',message='You are loged in as staff')
               file=open('login.txt',"w")
               file.write(uname+'\n')
               file.close()
               file=open('loginhistory.txt',"a")
               file.write(uname+'\t '+str(datetime.datetime.now())+'\n')
               file.close()
               root.destroy()
               os.system('python3 /home/admin-pc/Documents/DBMS\ project/staff.py')
              
           else:
               raise Exception('Invalid username or password')
        except Exception as e:
           messagebox.showerror(title='Authentication failure',message=str(e))
        
     else:
        try:
           cur=session.cursor()
           ans=str(v2.get())
           print(subprocess.getoutput(ans))
           query=str("select password from passwd where username= '"+str(v1.get())+"' and post='admin';")
           session._execute_query(query)
           result=cur.fetchall()
           result=str(result[0][0])
           print(subprocess.getoutput(result))
           if(result==ans):
               messagebox.showinfo(title='Login Sucessfull',message='You are loged in as system Administration')
               file=open('login.txt',"w")
               file.write(uname+'\n')
               file.close()
               file=open('loginhistory.txt',"a")
               file.write(uname+'\t '+str(datetime.datetime.now())+'\n')
               file.close()
               root.destroy()
               os.system('python3 /home/admin-pc/Documents/DBMS\ project/admin.py')
           else:
               raise Exception('Invalid username or password')
        except Exception as e:
           messagebox.showerror(title='Authentication failure',message=str(e))
#os.system('kdeconnect-cli --name Redmi --send-sms "otp is 31556" --destination 8888402205')
canvas=Canvas(root,height=1080,width=1920,background='#E6E6FA')
canvas.create_text(680,100,text="WELCOME TO MITAOE HOSTEL",font=('Lucida Handwriting',60),fill="#191970")
canvas.create_text(100,300,text='Login as :',font=('verdana',20))
var=IntVar()
r1=Radiobutton(canvas,text='Student',variable=var,value=1,font=('verdana',20),relief='raised',command=show,bd=3)
r2=Radiobutton(canvas,text='System Admin',variable=var,value=2,font=('verdana',20),relief='raised',command=show,bd=3)
r3=Radiobutton(canvas,text='Staff',variable=var,value=3,font=('verdana',20),relief='raised',command=show,bd=3)
canvas.create_window(156,400,window=r1)
canvas.create_window(200,350,window=r2)
canvas.create_window(135,450,window=r3)
canvas.pack()
root.mainloop()