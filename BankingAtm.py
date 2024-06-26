import tkinter as tk
import pymysql
from tkinter import *


con=pymysql.connect(host='localhost', 
                user='root', password='', db='ATM')
c=con.cursor()

c.execute('create table if not exists \
details(name varchar(500), \
password varchar(500), balance float)')

def new_user():
    root.destroy()

    root1=tk.Tk()
    root1.title('Registration Page')
    root1.minsize(1350,700)
    root1.config(bg='cyan')
    
    tk.Label(root1,
             text='Welcome to the Registration Page',
             font='Arial 35 bold',
             bg='cyan',
             justify=tk.CENTER,
             pady=50).grid(row=0,column=1)
    
    tk.Label(root1,
             text='Enter your name : ',
             #font='Arial 20',
             font='Arial 20 bold',
             bg='cyan',
             pady=15).grid(row=5,column=0)

    name=tk.Entry(root1)
    name.grid(row=5, column=1)

    name_error=tk.Label(root1,
                        #font=' 10',
                        font=' 30',
                        fg='dark red',
                        bg='cyan')
    name_error.grid(row=6, column=1)

    tk.Label(root1,
             text='Enter your password : ',
             #font='Arial 20',
             font='Arial 20 bold',
             bg='cyan',
             pady=15).grid(row=7,column=0)

    password1=tk.Entry(root1,
                       show='*')
    password1.grid(row=7, column=1)

    tk.Label(root1,
             bg='cyan').grid(row=8, column=1)

    tk.Label(root1,
             text='Re-enter your password : ',
             #font='Arial 20',
             font='Arial 20 bold',
             bg='cyan',
             pady=15).grid(row=9,column=0)
 
    password2=tk.Entry(root1,
                       show='*')
    password2.grid(row=9, column=1)

    password_error=tk.Label(root1,
                            font=' 10',
                            fg='dark red',
                            bg='cyan')
    password_error.grid(row=10, column=1)

    tk.Label(root1,
             bg='cyan').grid(row=11)

    tk.Button(root1,
              text='Submit',
              font='Arial 25',
              fg='white',
              bg='dark blue',
              border=8,
              justify=tk.CENTER,
              command=lambda: submit1()).grid(row=12,column=1)

    def submit1():
        flag=0

        if(name.get()==''):
            name_error.config(text='*Username cannot be empty')

            if(password1.get()!=''):
                password_error.config(text='')

        if(password1.get()==''):
            password_error.config(text='*Password cannot be empty')
            
            if(name.get()!=''):
                name_error.config(text='')

        elif (name.get()!='') and (password1.get()!=''):
            name_error.config(text='')
            password_error.config(text='')
            
            c.execute('select * from details')
            data=c.fetchall()
            
            for row in data:
                if name.get() == row[0]:
                    flag=1
                    break
                
            if flag == 1:
                name_error.config(text='*Username already exists')
                
            elif flag == 0:
                if(password2.get()!=password1.get()):
                    password_error.config(text='*Passwords do not match')
                    
                else:

                    #root1.destroy()
                    
                    root9=tk.Tk()
                    root9.title('Money Deposit')
                    root9.minsize(1350,700)
                    #root9.config(bg='dark red')
                    root9.config(bg='aqua')
                    
                    tk.Label(root9,
                             text='Would you like to deposit some money?',
                             #font='Arial 30',
                             font='Arial 40 bold',
                             #bg='dark red',
                             bg='aqua',
                             #justify=tk.CENTER).grid(row=0)
                             justify=tk.CENTER).grid(row=1,column=2)
                    
                    tk.Button(root9,
                              text='YES',
                              font='Arial 15',
                              bg='dark blue',   #
                              fg='red',
                              border=10,
                              width=15,
                              justify=tk.CENTER,
                              #command=lambda: yes()).grid(row=1, column=0)
                              command=lambda: yes()).grid(row=7, column=2)
                              
                    
                    tk.Button(root9,
                              text='NO',
                              font='Arial 15',
                              bg='dark blue',   #
                              fg='red',
                              border=10,
                              width=15,
                              justify=tk.CENTER,
                              #command=lambda: no()).grid(row=1, column=1)
                              
                              command=lambda: no()).grid(row=8, column=2)
                    

                              
                    def yes():
                        root9.destroy()

                        root10=tk.Tk()
                        root10.title('Money Deposit')
                        root10.minsize(1350,700)
                        #root10.minsize(700,450)
                        #root10.config(bg='dark red')
                        root10.config(bg='thistle')

                        tk.Label(root10,
                                 text='Enter the amount : ',
                                 #font='Arial 20',
                                 font='Arial 30 bold',
                                 #bg='dark red').grid(row=0, column=0)
                                 bg='thistle').grid(row=1, column=1)

                        amount=tk.Entry(root10)
                        #amount.grid(row=0, column=1)
                        amount.grid(row=1, column=3)


                        tk.Button(root10,
                                  text='Done',
                                  font='Arial 15',
                                  bg='dark blue',
                                  fg='white',
                                  border=8,
                                  width=25,
                                  #command=lambda: done()).grid(row=2)
                                  command=lambda: done()).grid(row=5,column=2)
                        

                        def done():
                            #root10.destroy()
                            try:
                                c.execute('insert into details values (%s, %s, %s)',(name.get(), password2.get(), amount.get()))
                                con.commit()
                                main(name, password2)
                                
                            except:
                                con.rollback()
                                tk.Label(root10,
                                         text='*Some unknown error occured',
                                         bg='dark red').grid(row=s, column=1)

                            root10.mainloop()

                    def no():
                        #root10.destroy()
                        try:
                            c.execute('insert into details values (%s, %s, %s)',(name.get(), password2.get(), 0))
                            con.commit()
                            main(name, password2)
                        except:
                            con.rollback()
                            tk.Label(root9,
                                     text='*Some unknown error occured',
                                     bg='dark red').pack()

                    root9.mainloop()
        

    root1.mainloop()

def old_user():
    root.destroy()
    
    root2=tk.Tk()
    root2.title('Login Page')
    root2.minsize(1350,700)
    #root2.minsize(1000,500)
    root2.config(bg='aquamarine')
    
    tk.Label(root2,
             text='Welcome to the Login Page',
             font='Arial 40 bold',
             bg='aquamarine',
             justify=tk.CENTER,
             
             pady=60).grid(row=0,column=1)
    
    tk.Label(root2,
             text='Enter your name : ',
             #font='Arial 20',
             font='Arial 20 bold',
             bg='aquamarine').grid(row=5,column=0)

    name=tk.Entry(root2)
    name.grid(row=5, column=1)

    name_error=tk.Label(root2,
                        bg='aquamarine',
                        fg='dark red',
                        font=' 10')
                        #font=' 30')
    
    name_error.grid(row=6, column=1)

    tk.Label(root2,
             text='Enter your password : ',
             #font='Arial 20',
             font='Arial 20 bold',
             bg='aquamarine').grid(row=7,column=0)

    password1=tk.Entry(root2,
                       show='*')
    password1.grid(row=7, column=1)

    password_error=tk.Label(root2,
                            bg='aquamarine',
                            fg='dark red',
                            font=' 10')
    password_error.grid(row=8, column=1)

    tk.Label(root2,
             bg='aquamarine').grid(row=9)

    tk.Button(root2,
              text='Submit',
              font='Arial 20',
              bg='dark blue',
              fg='white',
              border=8,
              justify=tk.CENTER,
              command=lambda: submit2()).grid(row=10,column=1)

    def submit2():
        flag=0

        if(name.get()==''):
            name_error.config(text='*Username\
            cannot be empty')
            if(password1.get()!=''):
                password_error.config(text='')

        if(password1.get()==''):
            password_error.config(text='*Password\
            cannot be empty')

            if(name.get()!=''):
                name_error.config(text='')

        elif(name.get()!='') and (password1.get()!=''):
            name_error.config(text='')
            password_error.config(text='')
            
            c.execute('select * from details')
            data=c.fetchall()
            for row in data:
                if name.get() == row[0]:
                    flag=1
                    break
                
            if flag == 0:
                name_error.config(text='*Username\
                does not exists')

            elif flag == 1:
                c.execute('select password from \
                details where name=(%s)',(name.get()))
                pwd=c.fetchone()
                
                if(password1.get()!=pwd[0]):
                    password_error.config\
                    (text='*Incorrect password')
                    
                else:
                    main(name, password1)

    root2.mainloop()

def main(name, password1):

    
    c.execute('select balance from details where name=(%s)',(name.get()))
    bal=c.fetchone()
    balance=bal[0]
    
    root3=tk.Tk()
    root3.title('Main Page')
    root3.minsize(1350,700)
    root3.config(bg='cyan')

    tk.Label(root3,
             pady=25,
             bg='cyan').pack()
    
    tk.Button(root3,
              text='Check balance',
              font='Arial 20',
              bg='dark blue',
              fg='white',
              border=8,
              width=25,
              justify=tk.CENTER,
              command=lambda: check()).pack()

    def check():
        root3.destroy()

        root4=tk.Tk()
        root4.title('Account balance')
        root4.minsize(1350,700)
        #root4.config(bg='dark red')
        root4.config(bg='cyan')
        
        tk.Label(root4,
                 text='Your available balance is Rs.' + str(balance),
                 font='Arial 30 bold',
                 #bg='dark red',
                 bg='aqua',
                 #fg='white',
                 fg='blue',
                 justify=tk.CENTER).pack()

        tk.Button(root4,
                  text='Back',
                  font='Arial 20',
                  border=5, 
                  justify=tk.CENTER,
                  command=lambda : main(name, password1)).pack()
                  

        tk.Button(root4,
                  text='Exit',
                  font='Arial 20',
                  border=5,  
                  justify=tk.CENTER,
                  command=lambda: root4.destroy()).pack()

        root4.mainloop()

    tk.Label(root3,
             bg='cyan').pack()

    tk.Button(root3,
              text='Withdraw',
              font='Arial 20',
              bg='dark blue',
              fg='white',
              border=8,
              width=25,
              justify=tk.CENTER,
              command=lambda: withdraw(balance)).pack()

    def withdraw(balance):
        root3.destroy()
        
        root5=tk.Tk()
        root5.title('Withdrwal window')
        #root5.minsize(200,100)
        root5.minsize(1350,700)
        #root5.config(bg='dark red')
        root5.config(bg='aqua')


        tk.Label(root5,
                 text='Enter the amount you want to withdraw : ',
                 #font='Arial 20',
                 font='Arial 30 bold',
                 #bg='dark red',
                 bg='aqua',
                 #fg='white',
                 fg='red',
                 justify=tk.CENTER).grid(row=1, column=0)

        money1=tk.Entry(root5)
        #money1.grid(row=0, column=1)
        money1.grid(row=1,column=1)
        
        

        withdraw_error=tk.Label(root5,
                                #bg='dark red',
                                bg='aqua',
                                fg='white',
                                #font=' 10')
                                font=' 20')
        
        #withdraw_error.grid(row=1, column=1)
        withdraw_error.grid(row=2, column=1)


        tk.Button(root5,
                  text='Withdraw',
                  font='Arial 20',
                  bg='dark blue',   #
                  fg='white',
                  border=10,
                  width=15,
                  justify=tk.CENTER,
                  command=lambda: func1(balance)).grid(row=2, column=0)

        withdraw_notice=tk.Label(root5,
                                 font='Arial 30',
                                 #bg='dark red',
                                 bg='aqua',
                                 fg='white',
                                 justify=tk.CENTER)
        withdraw_notice.grid(row=3)

        def func1(balance):

            if(float(money1.get())<0):
                withdraw_error.config(text='*Invalid amount')

            elif(float(money1.get())>balance):
                withdraw_error.config(text="*Amount withdarwn is greater than available balance")

            elif(float(money1.get())>=0)and(float(money1.get())<=balance):
                
                try:
                    balance = balance - float(money1.get())
                    
                    c.execute('update details set balance=(%s) where name=(%s)', (balance, name.get()))
                    con.commit()

                    withdraw_notice.config(text='Your available balance is Rs.' + str(balance))
                    
                except:
                    con.rollback()
                    withdraw_notice.config(text='Some unknown error occured')

        tk.Button(root5,
                  text='Back',
                  font='Arial 20',
                  bg='dark blue',
                  fg='white',
                  border=10,
                  width=15,
                  justify=tk.CENTER,
                  command=lambda : main(name, password1)).grid(row=4, column=0)

        tk.Button(root5,
                  text='Exit',
                  font='Arial 20',
                  bg='dark blue',
                  fg='white',
                  border=8,
                  width=10,
                  justify=tk.CENTER,
                  #command=lambda: root5.destroy()).grid(row=4, column=1)
                  command=lambda: root5.destroy()).grid(row=8, column=0)
                  

        root5.mainloop()

    tk.Label(root3,
             bg='cyan').pack()

    tk.Button(root3,
              text='Deposit',
              font='Arial 20',
              bg='dark blue',
              fg='white',
              border=8,
              width=25,
              justify=tk.CENTER,
              command=lambda: deposit(balance)).pack()

    def deposit(balance):
        root3.destroy()
        
        root6=tk.Tk()
        root6.title('Deposit window')
        root6.minsize(1350,700)
        root6.config(bg='cyan')

        tk.Label(root6,
                 text='Enter the amount you want to deposit : ',
                 font='Arial 25 bold',
                 bg='cyan',
                 fg='red',
                 justify=tk.CENTER,pady=10).grid(row=0, column=0)

        money2=tk.Entry(root6)
        money2.grid(row=0, column=1)

        deposit_error=tk.Label(root6,
                               bg='cyan',
                               fg='white',
                               font=' 10')
        deposit_error.grid(row=1, column=1)

        tk.Button(root6,
                  text='Deposit',
                  font='Arial 20',
                  bg='dark blue',
                  fg='white',
                  border=15,
                  justify=tk.CENTER,
                  command=lambda: func2(balance)).grid(row=2)

        deposit_notice=tk.Label(root6,
                                bg='cyan',
                                fg='orange',
                                font='Arial 20',
                                border=8,
                                width=25,
                                justify=tk.CENTER)
        deposit_notice.grid(row=3)

        def func2(balance):
            if(float(money2.get())<0):
                deposit_error.config(text='*Invalid amount')

            elif(float(money2.get())>1000000000):
                deposit_error.config(text='*Our bank allows a maximum deposition of Rs.100 crore in a go')

            elif(float(money2.get())>=0) and (float(money2.get())<=1000000000):
            
                try:
                    balance = balance + float(money2.get())

                    c.execute('update details set balance=(%s) where name=(%s)', (balance, name.get()))
                    con.commit()

                    deposit_notice.config(text='Your available balance is Rs.' + str(balance))

                except:
                    con.rollback()
                    deposit_notice.config(text='Some unknown error occured')

        tk.Button(root6,
                  text='Back',
                  font='Arial 20',
                  bg='dark blue',
                  fg='white',
                  border=15,
                  justify=tk.CENTER,
                  command=lambda : main(name, password1)).grid(row=4, column=0)

        tk.Button(root6,
                  text='Exit',
                  font='Arial 20',
                  bg='dark blue',
                  fg='white',
                  border=15,
                  justify=tk.CENTER,
                  command=lambda: root6.destroy()).grid(row=8, column=0)

        root6.mainloop()

    tk.Label(root3,
             bg='cyan').pack()

    tk.Button(root3,
              text='Change Password',
              font='Arial 20',
              bg='dark blue',
              fg='white',
              border=8,
              width=25,
              justify=tk.CENTER,
              command=lambda: change(name, password1)).pack()

    def change(name, password1):
        root3.destroy()
        
        root7=tk.Tk()
        root7.title('Password changing window')
        root7.minsize(1350,700)

        root7.config(bg='cyan')

        tk.Label(root7,
                 text='Enter your old password : ',
                 font='Arial 25 bold',
                 bg='cyan',
                 fg='red',
                 justify=tk.CENTER).grid(row=0, column=0)

        old_pwd=tk.Entry(root7,width=20,
                         show='*')
        old_pwd.grid(row=0,column=1)

        old_pwd_error=tk.Label(root7,
                               bg='cyan',
                               fg='red',
                               font=' 15')
        old_pwd_error.grid(row=1, column=1)

        tk.Label(root7,
                 text='Enter your new password : ',
                 font='Arial 25 bold',
                 bg='cyan',
                 fg='red',
                 justify=tk.CENTER).grid(row=2, column=0)

        new_pwd1=tk.Entry(root7,
                         show='*')
        new_pwd1.grid(row=2, column=1)

        new_pwd1_error=tk.Label(root7,
                                bg='cyan',
                                fg='red',
                                font=' 15')
        new_pwd1_error.grid(row=3, column=1)

        tk.Label(root7,
                 text='Re-enter your new password : ',
                 font='Arial 25 bold',
                 bg='cyan',
                 fg='red',
                 justify=tk.CENTER).grid(row=4, column=0)

        new_pwd2=tk.Entry(root7,
                         show='*')
        new_pwd2.grid(row=4, column=1)

        new_pwd2_error=tk.Label(root7,
                                bg='cyan',
                                fg='red',
                                font=' 15')
        new_pwd2_error.grid(row=5, column=1)

        tk.Button(root7,
                  text='Change password',
                  font='Arial 20',
                  bg='dark blue',
                  fg='white',
                  border=8,
                  width=20,
                  justify=tk.CENTER,
                  command=lambda: change_pwd(name, password1)).grid(row=6, column=0)

        notice=tk.Label(root7,
                        bg='cyan',
                        fg='red',
                        font='Arial 20')
        notice.grid(row=7, column=0)

        def change_pwd(name, password1):
            if(old_pwd.get()==''):
                old_pwd_error.config(text='*Old password cannot be empty')

                if(new_pwd1.get()!=''):
                    new_pwd1_error.config(text='')

            if(new_pwd1.get()==''):
                new_pwd1_error.config(text='*New password cannot be empty')

                if(old_pwd.get()!=''):
                    old_pwd_error.config(text='')

            elif(old_pwd.get()!='') and (new_pwd1.get()!=''):
                new_pwd1_error.config(text='')
                old_pwd_error.config(text='')
                
                if(old_pwd.get()!=password1.get()):
                    old_pwd_error.config(text='*Incorrect old password')
                    
                else:
                    if(new_pwd1.get()!=new_pwd2.get()):
                        new_pwd2_error.config(text='*Passwords do not match')
                        
                    else:
                        try:
                            c.execute('update details set password=(%s) where name=(%s)', (new_pwd2.get(), name.get()))
                            con.commit()
                            notice.config(text='Password updated successfully')
                            change_back.config(command=lambda: main(name, new_pwd2))
                            
                        except:
                            con.rollback()
                            notice.config(text='Unknown error occured')

        change_back=tk.Button(root7,
                              text='Back',
                              font='Arial 20',
                              fg='white',
                              bg='dark blue',
                              border=8,
                              width=15,
                              justify=tk.CENTER,
                              command=lambda : main(name, password1))
        change_back.grid(row=10,column=0)

        tk.Button(root7,
                  text='Exit',
                  font='Arial 20',
                  fg='white',
                  bg='dark blue',
                  border=8,
                  width=10,
                  justify=tk.CENTER,
                  command=lambda: root7.destroy()).grid(row=25,column=2)

        root7.mainloop()



    tk.Label(root3,
             bg='cyan').pack()

    tk.Button(root3,
              text='Return Card',
              font='Arial 20',
              bg='dark blue',
              fg='white',
              border=8,
              width=25,
              justify=tk.CENTER,
              command=lambda: return_card()).pack()

    def return_card():
        root3.destroy()
        
        root8=tk.Tk()
        root8.title('Returning card')
        root8.minsize(1350,700)
        root8.config(bg='aqua')
        

        tk.Label(root8,
                 text='Reurning Card...',
                 #font='Arial 30',
                 font='Arial 40 bold',
                 bg='aqua',
                 fg='red',
                 justify=tk.CENTER,pady=100).pack()

        tk.Button(root8,
                  text='Exit',
                  font='Arial 20',
                  fg='white',
                  bg='dark blue',
                  #bg='teal',
                  border=12,
                  justify=tk.CENTER,
                  command=lambda: root8.destroy()).pack()


        root8.mainloop()

    root3.mainloop()

root=tk.Tk()
root.title('SBI Banking Services')
root.minsize(1350,700)
#root.config(bg='indigo')
root.config(bg='#99CCFF')

p1=PhotoImage(file="C:\DB\sbi.gif")
l1=Label(borderwidth=5,relief='solid',fg='yellow',image=p1,
         compound=CENTER,bg='#019EEC')
l1.place(x=0,y=20,width=1350)

main_label=tk.Label (root,
                     text='Welcome to SBI Banking Services',
                     font='Century 50 bold',fg='blue',bg='#99CCFF')

#main_label.pack()
main_label.place(x=110,y=260)
#main_label.config(justify=tk.CENTER,pady=120)
main_label.config(justify=tk.CENTER,pady=20)

new=tk.Button(root,
              text='New User',
              font='Arial 20',
              fg='white',
              bg='dark blue',
              border=8,
              command=lambda: new_user())
#new.pack()
new.place(x=400,y=400)
new.config(justify=tk.CENTER,
           width=30)

tk.Label(root,
         #bg='indigo').pack()
         bg='#99CCFF').pack()
         #bg='green').pack()#errro


old=tk.Button(root,
              text='Registered User',
              font='Arial 20',
              fg='white',
              bg='dark blue',
              border=8,
              command=lambda: old_user())
#old.pack()
old.place(x=400,y=500)
old.config(justify=tk.CENTER,
           width=30)

root.mainloop()
