from tkinter import *
import mysql.connector
from tkinter import messagebox
import datetime
import subprocess
import random
import os
roota=Tk()
def connect():
   try:
     global session
     session=mysql.connector.connect(host='127.0.0.1',user='root',passwd='password',database='hosteldb')
     messagebox.showinfo(title='Connection Sucessfull !',message='Connected to the database !!')
     return 0    
   except Exception as e:
      messagebox.showerror(title='Connection error',message='Connection failed \n'+str(e)+'\nTry Again!!')
      return 1
def studentsection():
    canvas.destroy()
    canvas2=Canvas(roota,height=1080,width=1920,background='#A9A9A9')
    global F1
    F1=Frame(canvas2,width=1920,height=450,bg='#A9A9A9',highlightcolor='#FFFFFF',cursor='dot')
    F1.place(x=0,y=170)
    canvas2.create_text(670,50,text='Student Section',font=('Verdana',30),fill="#000000")    
    b1=Button(canvas2,text='Add new student',font=('verdana',20),relief='raised',bd=3,command=lambda : add(1))
    b4=Button(canvas2,text='Delete student',font=('verdana',20),relief='raised',bd=3,command=lambda: delete(1))
    b2=Button(canvas2,text='students with pending fees',font=('verdana',20),relief='raised',bd=3,command=lambda :view(1))
    b3=Button(canvas2,text='Exit',font=('verdana',20),relief='raised',bd=3,command=exit) 
    canvas2.create_window(600,650,window=b3)
    canvas2.create_window(300,130,window=b1)
    canvas2.create_window(700,130,window=b4)
    canvas2.create_window(1150,130,window=b2)    
    canvas2.pack()
def delete(flag):
    for widget in F1.winfo_children():
          widget.destroy()
    global id
    id=StringVar()
    if(flag==2):
      L1=Label(F1,text='EID :',font=('verdana',20),relief='flat',background='#A9A9A9')
      E1=Entry(F1,textvariable=id,relief='flat',bd=5,width=30)
      L1.place(x=50,y=50)
      E1.place(x=150,y=50)
      b1=Button(F1,text='Delete',font=('verdana',20),relief='raised',bd=3,command=lambda :deletequery(flag))
      b1.place(x=500,y=50)
    else:
      L1=Label(F1,text='PRN No. :',font=('verdana',20),relief='flat',background='#A9A9A9')
      E1=Entry(F1,textvariable=id,relief='flat',bd=5,width=30)
      L1.place(x=50,y=50)
      E1.place(x=200,y=50)
      b1=Button(F1,text='Delete',font=('verdana',20),relief='raised',bd=3,command=lambda :deletequery(flag))
      b1.place(x=500,y=50)
def deletequery(flag):
      if(connect()==0):
        if (flag==1):
          try:
            query="delete from student where PRN_number= '"+str(id.get())+"';"
            session._execute_query(query)
            session.commit()
            query="delete from fees where PRN= '"+str(id.get())+"';"
            session._execute_query(query)
            session.commit()
            query="update room set PRN = 99999 where PRN= '"+str(id.get())+"';"
            session._execute_query(query)
            session.commit()
            messagebox.showinfo(title='Success !!',message='Student entry deleted with PRN number \t'+str(id.get()))
          except Exception as e:
            messagebox.showerror(title='Failure' ,message='Deletion failed'+str(e))
        else:
          try:
            query="delete from staff where EID= '"+str(id.get())+"';"
            session._execute_query(query)
            session.commit()
            messagebox.showinfo(title='Success !!',message='Staff entry deleted with EID \t'+str(id.get()))
          except Exception as e:
            messagebox.showerror(title='Failure' ,message='Deletion failed'+str(e))
def staffsection():
    canvas.destroy()
    canvas1=Canvas(roota,height=1080,width=1920,background='#A9A9A9')
    global F1
    F1=Frame(canvas1,width=1920,height=450,bg='#A9A9A9',highlightcolor='#FFFFFF',cursor='dot')
    F1.place(x=0,y=170)   
    canvas1.create_text(670,50,text='Staff Section',font=('Verdana',30),fill="#000000")    
    b1=Button(canvas1,text='Add new staff member',font=('verdana',20),relief='raised',bd=3,command=lambda: add(2)) 
    b2=Button(canvas1,text='View salary of staff member(s)',font=('verdana',20),relief='raised',bd=3,command=lambda: view(2))
    b3=Button(canvas1,text='Exit',font=('verdana',20),relief='raised',bd=3,command=exit)
    b4=Button(canvas1,text='Delete staff member',font=('verdana',20),relief='raised',bd=3,command=lambda: delete(2))
    canvas1.create_window(600,650,window=b3)
    canvas1.create_window(700,130,window=b4)
    canvas1.create_window(300,130,window=b1)
    canvas1.create_window(1140,130,window=b2) 
    canvas1.pack()
def add(flag):
      for widget in F1.winfo_children():
          widget.destroy()
      L1=Label(F1,text='Enter name :',font=('verdana',20),relief='flat',background='#A9A9A9')
      L1.place(x=55,y=10)
      global name
      name=StringVar()
      global address
      address=StringVar()
      E1=Entry(F1,relief='flat',bd=5,textvariable=name,width=30)
      E1.place(x=300,y=10)
      global var
      var=IntVar()
      L2=Label(F1,text='Select Gender :',font=('verdana',20),relief='flat',background='#A9A9A9')
      L2.place(x=55,y=60)
      R1=Radiobutton(F1,text='Male ',relief='raised',variable=var,value=1,font=('verdana',15),bd=3)
      R2=Radiobutton(F1,text='Female ',relief='raised',variable=var,value=2,font=('verdana',15),bd=3)
      R1.place(x=300,y=60)
      R2.place(x=430,y=60)
      L3=Label(F1,text='Address :',relief='flat',font=('verdana',20),background='#A9A9A9')
      L3.place(x=50,y=110)
      E3=Entry(F1,textvariable=address,relief='flat',bd=5,width=30)
      E3.place(x=300,y=110)
      L4=Label(F1,text='Mobile number :',bd=5,relief='flat',font=('verdana',20),background='#A9A9A9')
      L4.place(x=50,y=150)
      global email 
      email=StringVar()
      L8=Label(F1,text='Email :',bd=5,relief='flat',font=('verdana',20),background='#A9A9A9')
      L8.place(x=50,y=195)
      E8=Entry(F1,textvariable=email,relief='flat',bd=5,width=30)
      E8.place(x=250,y=200)
      global mobileno 
      mobileno=StringVar()
      E4=Entry(F1,textvariable=mobileno,bd=5,relief='flat')
      E4.place(x=300,y=155)
      L5=Label(F1,text='Enter DOB :',bd=5,relief='flat',font=('verdana',20),background='#A9A9A9')
      L5.place(x=50,y=240)
      global dob
      global month
      global date
      global year
      date=StringVar()
      month=StringVar()
      year=StringVar()
      E5=Entry(F1,textvariable=date,bd=5,relief='flat',width=5)
      E5.place(x=320,y=250)
      L10=Label(F1,text='Date',font=('verdana',20),relief='flat',background='#A9A9A9')
      L10.place(x=250,y=250)
      L11=Label(F1,text='Month',font=('verdana',20),relief='flat',background='#A9A9A9')
      L11.place(x=400,y=250)
      L12=Label(F1,text='Year',font=('verdana',20),relief='flat',background='#A9A9A9')
      L12.place(x=600,y=250)
      E6=Entry(F1,textvariable=month,bd=5,relief='flat',width=5)
      E6.place(x=500,y=250)
      E9=Entry(F1,textvariable=year,bd=5,relief='flat',width=5)
      E9.place(x=670,y=250)
      if (flag==1):
        global rtype
        L6=Label(F1,text='Room type :',bd=5,relief='flat',font=('verdana',20),background='#A9A9A9')
        L6.place(x=50,y=300)
        rtype=StringVar()
        global programme
        programme=StringVar()
        L7=OptionMenu(F1,rtype,'A = First class' , 'B = second class')
        L7.place(x=250,y=300)
        L9=Label(F1,text='Programme :',relief='flat',font=('verdana',20),background='#A9A9A9')
        rtype.set('- Select -')
        lst1 = ['FYBTECH','SYBTECH','TYBTECH','BTECH']
        drop =OptionMenu(F1,programme,*lst1 )
        programme.set('- Select -')
        drop.place(x=250,y=350)
        L9.place(x=50,y=350)
      else:
        L6=Label(F1,text='Salary :',bd=5,relief='flat',font=('verdana',20),background='#A9A9A9')
        global amt
        L6.place(x=50,y=300)
        amt=StringVar()
        E6=Entry(F1,textvariable=amt,bd=5,relief='flat')
        E6.place(x=250,y=300)
        L7=Label(F1,text='Rs.',relief='flat',font=('verdana',20),background='#A9A9A9')
        L7.place(x=450,y=300)
      B1=Button(F1,text='Submit',font=('verdana',20),bd=3,relief='raised',command=lambda:insert(flag))
      B1.place(x=550,y=400)
def payment(flag):
      for widget in F1.winfo_children():
          widget.destroy()
      if(flag==1):
        L1=Label(F1,text='Enter amount :',relief='flat',font=('verdana',20),background='#A9A9A9')
        L1.place(x=50,y=50)
        temp=StringVar()
        E1=Entry(F1,relief='flat',textvariable=temp,bd=5)
        E1.place(x=350,y=50)
        B1=Button(F1,text='Submit',font=('verdana',20),bd=3,relief='raised',command=lambda:pay(str(temp.get()),str(PRN.get()),flag))
        B1.place(x=500,y=200)
        L2=Label(F1,text='Enter PRN number :',relief='flat',font=('verdana',20),background='#A9A9A9')
        L2.place(x=50,y=100)
        PRN=StringVar()
        E1=Entry(F1,relief='flat',textvariable=PRN,bd=5)
        E1.place(x=350,y=100)
      else:
        L1=Label(F1,text='Enter EID :',relief='flat',background='#A9A9A9',font=('verdana',20))
        L1.place(x=50,y=50)
        id=StringVar()
        L2=Label(F1,text="Enter *  to pay salary to all members",font=('verdana',10),background='#A9A9A9',relief='flat')
        L2.place(x=220,y=100)
        E1=Entry(F1,textvariable=id,relief='flat',bd=5)
        E1.place(x=220,y=50)
        B1=Button(F1,text='Submit',font=('verdana',20),bd=3,relief='raised',command=lambda :salary(str(id.get())))
        B1.place(x=600,y=150)
def pay(amount1,PRN,flag):
  if(connect()==0):
    file=open('payment.txt','r')
    amount=file.readline()
    file.close()
    amount=amount.strip()
    amount=int(amount)
    file=open('payment.txt','w')
    amount=amount+int(amount1)
    file.write(str(amount))
    file.close()
    try:
      amount1=int(amount1)
      cur=session.cursor()
      query="select amount_paid from fees where PRN = '"+str(PRN)+"';"
      session._execute_query(query)
      result=cur.fetchall()
      result=int(result[0][0])
      amount1=result+amount1
      query="update fees set amount_paid= '"+str(amount1)+"' where PRN= '"+str(PRN)+"';"
      session._execute_query(query)
      session.commit() 
      messagebox.showinfo(title='Payment accepted',message='Payment accepted !')
    except Exception as e:
      messagebox.showerror(title="Update failed",message=str(e))
def salary(id):
  if(connect()==0):
    try:
      if(id=='*'):
        file=open('payment.txt','r')
        amount=file.readline()
        file.close()
        amount=amount.strip()
        amount=int(amount)
        cur=session.cursor()
        query='select salary from staff where EID>9999'
        session._execute_query(query)
        result=cur.fetchall()
        l=len(result)
        for i in range(0,l):
          if(amount<=0):
            messagebox.showerror(title='Insufficient balance',message='Insufficient balance')
          else:
            amount=amount-int(result[i][0])
        messagebox.showinfo(title='Success',message='Success !!')
        file=open('payment.txt','w')
        file.write(str(amount))
        file.close()
      else:
        cur=session.cursor()
        query="select salary from staff where EID='"+str(id)+"';"
        session._execute_query(query)
        result=session.cursor()
        result=int(result[0][0])
        file=open('payment.txt','r')
        amount=file.readline()
        file.close()
        amount=amount.strip()
        amount=int(amount)
        amount=amount-result
        file=open('payment.txt','w')
        file.write(str(amount))
        file.close()
    except Exception as e:
      messagebox.showerror(title='Faliure',message=str(e))
def insert(flag):
  if(connect()==0):
    dob=str(date.get()+'/'+month.get()+'/'+year.get())
    a = datetime.date(int(year.get()),int(month.get()),int(date.get()))
    a=a.year
    b=datetime.date.today() 
    b=b.year
    age = b - a
    age=round(age)
    print(subprocess.getoutput(str(age)))
    try:
      if (var.get()==1):
          gender='male'
      else:
          gender='female'
      if (flag==1):
          query1="select PRN_number from student order by PRN_number desc;"
          cur=session.cursor()
          session._execute_query(query1)
          result=cur.fetchall()
          PRN=result[0][0]
          print(subprocess.getoutput(str(PRN)))
          PRN=PRN+1 
          query="insert into student values('"+str(PRN)+"','"+str(name.get())+"','"+str(address.get())+"','"+str(mobileno.get())+"','"+str(email.get())+"','"+str(dob)+"','"+str(age)+"','"+gender+"','"+str(programme.get())+"');"
          session._execute_query(query)
          session.commit()
          passwd=random.randint(10000000,99999999)
          emailid=str(email.get())
          index=emailid.index('@')
          username=emailid[:index]
          username=username.lower()
          query="insert into passwd values('"+str(username)+"','"+str(passwd)+"','student','"+str(PRN)+"','"+str(99999)+"');"
          session._execute_query(query)
          session.commit()
          print(subprocess.getoutput('password'))
          cur=session.cursor()
          room=str(rtype.get())
          index=room.index('=')
          room=room[:index-1]
          query="select room_no from room where room_type= '"+str(room)+"' and PRN=9999 ;"
          session._execute_query(query)
          result=cur.fetchall()
          result=result[0][0]
          roomno=result
          print(subprocess.getoutput(str(result)))
          print(subprocess.getoutput('room'))
          query="insert into fees values('"+str(PRN)+"','"+str(result)+"','0');"
          session._execute_query(query)
          session.commit()
          print(subprocess.getoutput('fees'))
          query="update room set PRN= '"+str(PRN)+"' where room_no= '"+str(roomno)+"';"
          session._execute_query(query)
          session.commit()
          print(subprocess.getoutput('room'))
          message="Hey "+str(name.get())+",\nWelcome to MITAOE Hostel..\nYou are sucessfully admitted in our hostel.\nYour PRN number is :"+str(PRN)+"\nYour Username is : "+str(username)+" and your password is : "+str(passwd)+".\nYou are requested to login using this password and change the password as you want.\n"
          message=message+"You have allocated room type "+str(rtype.get())+". Your room number is "+str(roomno)+". "
          command="kdeconnect-cli --name Redmi --send-sms '"+str(message)+"' --destination "+str(mobileno.get())
          #os.system(command)
          messagebox.showinfo(title='Update Successfull',message='New entry added sucessfully')
      else:
          query1="select EID from staff order by EID desc;"
          cur=session.cursor()
          session._execute_query(query1)
          result=cur.fetchall()
          EID=result[0][0]
          if (EID==''):
            EID=1
          print(subprocess.getoutput(str(EID)))
          EID=EID+1 
          query="insert into staff values('"+str(EID)+"','"+str(name.get())+"','"+str(address.get())+"','"+str(mobileno.get())+"','"+str(email.get())+"','"+str(dob)+"','"+str(age)+"','"+gender+"','"+str(amt.get())+"');"
          session._execute_query(query)
          session.commit()
          passwd=random.randint(10000000,99999999)
          emailid=str(email.get())
          index=emailid.index('@')
          username=emailid[:index]
          username=username.lower()
          query="insert into passwd values('"+str(username)+"','"+str(passwd)+"','staff','"+str(99999)+"','"+str(EID)+"');"
          session._execute_query(query)
          session.commit()
          message="Hey ,"+name.get()+"\nYou are successfully registered as a staff member in our MITAOE Hostel.\n"
          message=message+"Your username is : "+str(username)+"  and your password is : "+str(passwd)+".\nYou are requested to login using this password and change the password as you want.\n"
          command="kdeconnect-cli --name Redmi --send-sms '"+str(message)+"' --destination "+str(mobileno.get())
          #os.system(command)
          messagebox.showinfo(title='Update Successfull',message='New entry added sucessfully')
    except Exception as e:
          messagebox.showerror(title='Insertion failed',message=str(e))
def view(flag):
  if(connect()==0):
    for widget in F1.winfo_children():
          widget.destroy()
  if(flag==1):
    cur=session.cursor()
    query="select student.PRN_number,student.sname,room.room_type,fees.amount_paid from student,fees,room where student.PRN_number=fees.PRN and room.PRN=student.PRN_number and student.PRN_number in(select distinct (fees.PRN) from fees,room where (room.fees-amount_paid>0))"
    session._execute_query(query)
    result=cur.fetchall()
    l=len(result)
    L=Label(F1,text="PRN",font=('verdana',20),background='#A9A9A9')
    L.place(x=50,y=0)
    L1=Label(F1,text="Name",font=('verdana',20),background='#A9A9A9')
    L1.place(x=200,y=0)
    L=Label(F1,text="Room Type",font=('verdana',20),background='#A9A9A9')
    L.place(x=350,y=0)
    L=Label(F1,text="Fees Paid",font=('verdana',20),background='#A9A9A9')
    L.place(x=530,y=0)
    m=50
    o=50
    for i in range(0,l):
      if(m<450):
          n=50
          L1=Label(F1,text=str(result[i][0]),font=('verdana',20),background='#A9A9A9')
          L1.place(x=n,y=m)
          n=n+150
          L2=Label(F1,text=str(result[i][1]),font=('verdana',20),background='#A9A9A9')
          L2.place(x=n,y=m)
          n=n+150
          L3=Label(F1,text=str(result[i][2]),font=('verdana',20),background='#A9A9A9')
          L3.place(x=n,y=m)
          n=n+180
          L4=Label(F1,text=str(result[i][3]),font=('verdana',20),background='#A9A9A9')
          L4.place(x=n,y=m)
          m=m+50
      else:
          L1=Label(F1,text="PRN",font=('verdana',20),background='#A9A9A9')
          L1.place(x=700,y=0)
          L2=Label(F1,text="Name",font=('verdana',20),background='#A9A9A9')
          L2.place(x=850,y=0)
          L=Label(F1,text="Room Type",font=('verdana',20),background='#A9A9A9')
          L.place(x=1000,y=0)
          L=Label(F1,text="Fees Paid",font=('verdana',20),background='#A9A9A9')
          L.place(x=1180,y=0)
          n=700
          L1=Label(F1,text=str(result[i][0]),font=('verdana',20),background='#A9A9A9')
          L1.place(x=n,y=o)
          n=n+150
          L2=Label(F1,text=str(result[i][1]),font=('verdana',20),background='#A9A9A9')
          L2.place(x=n,y=o)
          n=n+150
          L3=Label(F1,text=str(result[i][2]),font=('verdana',20),background='#A9A9A9')
          L3.place(x=n,y=m)
          n=n+180
          L4=Label(F1,text=str(result[i][3]),font=('verdana',20),background='#A9A9A9')
          L4.place(x=n,y=m)
          m=m+50
          o=o+50
  elif(flag==2):
    cur=session.cursor()
    query="select eid,ename,salary from staff where EID>99999"
    session._execute_query(query)
    result=cur.fetchall()
    l=len(result)
    L=Label(F1,text="EID",font=('verdana',20),background='#A9A9A9')
    L.place(x=50,y=0)
    L1=Label(F1,text="Ename",font=('verdana',20),background='#A9A9A9')
    L1.place(x=200,y=0)
    L=Label(F1,text="Salary",font=('verdana',20),background='#A9A9A9')
    L.place(x=350,y=0)
    m=50
    o=0
    for i in range(0,l):
      if(m<450):
          n=50
          L1=Label(F1,text=str(result[i][0]),font=('verdana',20),background='#A9A9A9')
          L1.place(x=n,y=m)
          n=n+150
          L2=Label(F1,text=str(result[i][1]),font=('verdana',20),background='#A9A9A9')
          L2.place(x=n,y=m)
          n=n+150
          L2=Label(F1,text=str(result[i][2]),font=('verdana',20),background='#A9A9A9')
          L2.place(x=n,y=m)
          m=m+50
      else:
          L1=Label(F1,text="EID",font=('verdana',20),background='#A9A9A9')
          L1.place(x=600,y=0)
          L2=Label(F1,text="Ename",font=('verdana',20),background='#A9A9A9')
          L2.place(x=800,y=0)
          L=Label(F1,text="Salary",font=('verdana',20),background='#A9A9A9')
          L.place(x=1000,y=0)
          n=600
          L1=Label(F1,text=str(result[i][0]),font=('verdana',20),background='#A9A9A9')
          L1.place(x=n,y=o)
          n=n+200
          L2=Label(F1,text=str(result[i][1]),font=('verdana',20),background='#A9A9A9')
          L2.place(x=n,y=o)
          o=o+50
  else:
    cur=session.cursor()
    query='select room_no, room_type from room where PRN=9999'
    session._execute_query(query)
    result=cur.fetchall()
    l=len(result)
    m=50
    L1=Label(F1,text='Room no.',font=('verdana',20),background='#A9A9A9')
    L1.place(x=50,y=0)
    L2=Label(F1,text='Room type',font=('verdana',20),background='#A9A9A9')
    L2.place(x=200,y=0)
    o=50
    for i in range(0,l):
      if(m<450):
          n=50
          L1=Label(F1,text=str(result[i][0]),font=('verdana',20),background='#A9A9A9')
          L1.place(x=n,y=m)
          n=n+200
          L2=Label(F1,text=str(result[i][1]),font=('verdana',20),background='#A9A9A9')
          L2.place(x=n,y=m)
          m=m+50
      else:
          L1=Label(F1,text='Room no.',font=('verdana',20),background='#A9A9A9')
          L1.place(x=600,y=0)
          L2=Label(F1,text='Room type',font=('verdana',20),background='#A9A9A9')
          L2.place(x=800,y=0)
          n=600
          L1=Label(F1,text=str(result[i][0]),font=('verdana',20),background='#A9A9A9')
          L1.place(x=n,y=o)
          n=n+200
          L2=Label(F1,text=str(result[i][1]),font=('verdana',20),background='#A9A9A9')
          L2.place(x=n,y=o)
          o=o+50
def roomsection():
    canvas.destroy()
    canvas3=Canvas(roota,height=1080,width=1920,background='#A9A9A9')
    global F1
    F1=Frame(canvas3,width=1920,height=450,bg='#A9A9A9',highlightcolor='#FFFFFF',cursor='dot')
    F1.place(x=0,y=170)
    canvas3.create_text(670,50,text='Room Section',font=('Verdana',30),fill="#000000")    
    b1=Button(canvas3,text='Find empty room',font=('verdana',20),relief='raised',bd=3,command=lambda :view(3)) 
    b3=Button(canvas3,text='Exit',font=('verdana',20),relief='raised',bd=3,command=exit) 
    canvas3.create_window(600,650,window=b3)
    canvas3.create_window(700,130,window=b1)   
    canvas3.pack()
def paymentsection():
    canvas.destroy()
    canvas4=Canvas(roota,height=1080,width=1920,background='#A9A9A9')
    global F1
    F1=Frame(canvas4,width=1920,height=450,bg='#A9A9A9',highlightcolor='#FFFFFF',cursor='dot')
    F1.place(x=0,y=170)
    canvas4.create_text(670,50,text='Payment Section',font=('Verdana',30),fill="#000000")    
    b1=Button(canvas4,text='Accept payment from student',font=('verdana',20),relief='raised',bd=3,command=lambda : payment(1)) 
    b2=Button(canvas4,text='Pay salary to staff member',font=('verdana',20),relief='raised',bd=3,command=lambda : payment(2) )
    b3=Button(canvas4,text='Exit',font=('verdana',20),relief='raised',bd=3,command=exit) 
    canvas4.create_window(600,650,window=b3)
    canvas4.create_window(300,130,window=b1)
    canvas4.create_window(1000,130,window=b2)    
    canvas4.pack()
def exit():
    roota.destroy()
roota.title('Administrator Page')
canvas=Canvas(roota,height=1080,width=1920,background='#FFFFE0')
c=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(subprocess.getoutput(c))
global uname
file=open('login.txt',"r")
uname=file.readline()
uname=uname.lstrip()
file.close()
canvas=Canvas(roota,height=1080,width=1920,background='#FFE4B5')
welcometext='Welcome , '+uname
L1=Label(canvas,text=welcometext,relief='raised',bd=-1,background='#FFE4B5',fg='#000000',font=('verdana',10),anchor=W)
L1.place(x=1150,y=50)
canvas.create_text(670,50,text='Choose any one section from below',font=('Verdana',30),fill="#FF6347")              
b1=Button(canvas,text='Student Section',font=('verdana',20),relief='raised',bd=3,command=studentsection) 
canvas.create_window(300+100,200,window=b1)
b2=Button(canvas,text='Rooms Section',font=('verdana',20),relief='raised',bd=3,command=roomsection)
b5=Button(canvas,text='Exit',font=('verdana',20),relief='raised',bd=3,command=exit)
b4=Button(canvas,text='Staff Section',font=('verdana',20),relief='raised',bd=3,command=staffsection)
b3=Button(canvas,text='Payment Section',font=('verdana',20),relief='raised',bd=3,command=paymentsection)
canvas.create_window(400,450,window=b2)
canvas.create_window(870,200,window=b3)
canvas.create_window(850,450,window=b4)
canvas.create_window(600,650,window=b5)
canvas.pack()
roota.mainloop()