from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ledger_bk

def login():
    uname=username.get()
    pwd=password.get()
    if uname=='' or pwd=='':
        messagebox.showinfo("Login","fill the empty field!!!")
    else:
      if uname=="Sai@123" and pwd=="123":
       messagebox.showinfo("login", "login Successful")
       main()
      else:
       messagebox.showinfo("Login", "Wrong username or password")

def main():
       window = Tk()
       window.title("Contact Management System")
       window.geometry("1227x746")
       window.config(bg="wheat")
       window.state("zoomed")
       def view_command():
           lb.delete(0,END)
           for row in ledger_bk.viewall():
               lb.insert(END,row)

       def search_command():
           lb.delete(0,END)
           for row in ledger_bk.search(Name=Name.get(),Age=Age.get(),Gender=Gender.get(),Phone=Phone.get(),Mail=Mail.get(),Address=Address.get()):
               lb.insert(END,row)

       def add_command():
           ledger_bk.add(Name.get(),Age.get(),Gender.get(),Phone.get(),Mail.get(),Address.get())
           messagebox.showinfo("Add", "Contact Added Successfully")
           lb.delete(0,END)
           lb.insert(END,Name.get(),Age.get(),Gender.get(),Phone.get(),Mail.get(),Address.get())
       def get_selected_row(event):
           try:
               global selected_tuple
               index=lb.curselection()[0]
               selected_tuple = lb.get(index)
               e1.delete(0,END)
               e1.insert(END,selected_tuple[1])
               e2.delete(0,END)
               e2.insert(END,selected_tuple[2])
               e3.delete(0,END)
               e3.insert(END,selected_tuple[3])
               e4.delete(0,END)
               e4.insert(END,selected_tuple[4])
               e5.delete(0,END)
               e5.insert(END,selected_tuple[5])
               e6.delete(0,END)
               e6.insert(END,selected_tuple[6])
        
           except IndexError:
               pass

       def update_command():
           ledger_bk.update(selected_tuple[0],Name.get(),Age.get(),Gender.get(),Phone.get(),Mail.get(),Address.get())
           messagebox.showinfo("Update", "Contact Updated Successfully")
           view_command()

       def delete_command():
           ledger_bk.delete(selected_tuple[0])
           messagebox.showinfo("Delete", 'Contact Deleted Successfully')
           view_command()
           #lb.delete(END,get_selected_row.selected_tuple)
       def clear_command():
           lb.delete(0,END)
           e1.delete(0,END)
           e2.delete(0,END)
           e3.delete(0,END)
           e4.delete(0,END)
           e5.delete(0,END)
           e6.delete(0,END)
    
       l1 = Label(window,text="Name",fg='black',bg='wheat',font=('CALIBRI',18,'bold'))
       l1.grid(row=0,column=0,columnspan=2, padx=10, pady=10)
       l2 = Label(window,text="Age",fg='black',bg='wheat',font=('CALIBRI',18,'bold'))
       l2.grid(row=1,column=0,columnspan=2, padx=10, pady=10)
       l3 = Label(window,text="Gender",fg='black',bg='wheat',font=('CALIBRI',18,'bold'))
       l3.grid(row=2,column=0,columnspan=2, padx=10, pady=10)
       l4 = Label(window,text="Phone",fg='black',bg='wheat',font=('CALIBRI',18,'bold'))
       l4.grid(row=3,column=0,columnspan=2, padx=10, pady=10)
       l5 = Label(window,text="Mail",fg='black',bg='wheat',font=('CALIBRI',18,'bold'))
       l5.grid(row=4,column=0,columnspan=2, padx=10, pady=10)
       l6 = Label(window,text="Address",fg='black',bg='wheat',font=('CALIBRI',18,'bold'))
       l6.grid(row=5,column=0,columnspan=2, padx=10, pady=10)

       Name=StringVar()
       e1 = Entry(window,textvariable=Name,width=40,font=('CALIBRI',18))
       e1.grid(row=0,column=0,columnspan=10, padx=10, pady=10)

       Age=StringVar()
       e2 = Entry(window,textvariable=Age,width=40,font=('CALIBRI',18))
       e2.grid(row=1,column=0,columnspan=10, padx=10, pady=10)

       Gender=StringVar()
       e3 = ttk.Combobox(window, font=("Calibri",18),width=38,textvariable=Gender, state="readonly")
       e3['values'] = ("Male", "Female")
       e3.grid(row=2,column=0,columnspan=10, padx=10, pady=10)

       Phone=StringVar()
       e4 = Entry(window,textvariable=Phone,width=40,font=('CALIBRI',18))
       e4.grid(row=3,column=0,columnspan=10, padx=10, pady=10)

       Mail=StringVar()
       e5 = Entry(window,textvariable=Mail,width=40,font=('CALIBRI',18))
       e5.grid(row=4,column=0,columnspan=10, padx=10, pady=10)

       Address=StringVar()
       e6 = Entry(window,textvariable=Address,width=40,font=('CALIBRI',18))
       e6.grid(row=5,column=0,columnspan=10, padx=10, pady=10)

       b1 = Button(window,text="Add",width=16,command=add_command,bg='skyblue1', fg='black',font=('CALIBRI',16))
       b1.grid(row=6,column=0)

       b2 = Button(window,text="Update",width=16,command=update_command,bg='skyblue1', fg='black',font=('CALIBRI',16))
       b2.grid(row=6,column=1)

       b3 = Button(window,text="Search",width=16,command=search_command,bg='skyblue1', fg='black',font=('CALIBRI',16))
       b3.grid(row=6,column=2)

       b4 = Button(window,text="View All",width=16,command=view_command,bg='skyblue1', fg='black',font=('CALIBRI',16))
       b4.grid(row=6,column=3)

       b5 = Button(window,text="Delete",width=16,command=delete_command,bg='skyblue1', fg='black',font=('CALIBRI',16))
       b5.grid(row=6,column=4)

       b6 = Button(window,text="Exit",width=16,command=window.destroy,bg='skyblue1', fg='black',font=('CALIBRI',16))
       b6.grid(row=6,column=6)

       b7 = Button(window,text="Clear All",width=16,command=clear_command,bg='skyblue1', fg='black',font=('CALIBRI',16))
       b7.grid(row=6,column=5)

       lb=Listbox(window,height=18,width=130,bg='beige',fg='black',font=('CALIBRI',16))
       lb.grid(row=7,column=0,columnspan=7)

       sb=Scrollbar(window)
       sb.grid(row=7,column=7,rowspan=6)

       lb.configure(yscrollcommand=sb.set)
       sb.configure(command=lb.yview)

       lb.bind('<<ListboxSelect>>',get_selected_row)
       window.mainloop()
       
def Loginform():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login Form")
    login_screen.geometry("600x400")
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    Label(login_screen,width="500", text="Login page",font=('CALIBRI',28,'bold')).pack()
    
    Label(login_screen, text="Username  ",font=('CALIBRI',18,'bold')).place(x=125,y=180)   
    Entry(login_screen, textvariable=username,font=('CALIBRI',18,'bold')).place(x=250,y=182)
    
    Label(login_screen, text="Password  ",font=('CALIBRI',18,'bold')).place(x=125,y=220)
    Entry(login_screen, textvariable=password ,show="*",font=('CALIBRI',18,'bold')).place(x=250,y=222)

    Button(login_screen, text="Login", width=10, height=1,command=login,font=('CALIBRI',18,'bold')).place(x=250,y=270)
    
    login_screen.mainloop()

Loginform()
