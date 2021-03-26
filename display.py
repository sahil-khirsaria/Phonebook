from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect("database.db")
cur=con.cursor()

class Display(Toplevel):
    def __init__(self,person_id):
        Toplevel.__init__(self)
        self.geometry("650x650+350+100")
        self.title("Display Contact")
        self.resizable(False,False)

        query="select * from Address where person_id = '{}' ".format(person_id)
        result=cur.execute(query).fetchone()
        self.person_id=person_id
        person_name=result[1]
        person_surname=result[2]
        person_email=result[3]
        person_phone=result[4]
        person_address=result[5]

        self.top=Frame(self,height=150,bg="white")
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=480,bg="brown")
        self.bottom.pack(fill=X)

        self.top_image=PhotoImage(file=r"D:\PFP\SahilPatel\Python App And Program\Phonebook\display.png")

        self.top_image_label=Label(self.top,image=self.top_image,bg="White")
        self.top_image_label.place(x=100,y=40)

        self.heading=Label(self.top,text="Person Details",font="Times 40 bold",bg="White",fg="Black")
        self.heading.place(x=175,y=40)

        #  Name
        self.label_name=Label(self.bottom,text="Name",font="Arial 15 bold",bg="white",fg="brown")
        self.label_name.place(x=50,y=50)

        self.entry_name=Entry(self.bottom,width=40,bd=2)
        self.entry_name.insert(0,person_name)
        self.entry_name.config(state="disable")
        self.entry_name.place(x=150,y=50)

        # surname
        self.label_surname=Label(self.bottom,text="Surname",font="Arial 15 bold",bg="white",fg="brown")
        self.label_surname.place(x=50,y=100)

        self.entry_surname=Entry(self.bottom,width=40,bd=2)
        self.entry_surname.insert(0,person_surname)
        self.entry_surname.config(state="disable")
        self.entry_surname.place(x=150,y=100)

        #  Num
        self.label_num=Label(self.bottom,text="Number",font="Arial 15 bold",bg="white",fg="brown")
        self.label_num.place(x=50,y=150)

        self.entry_num=Entry(self.bottom,width=40,bd=4)
        self.entry_num.insert(0,person_phone)
        self.entry_num.config(state="disable")
        self.entry_num.place(x=150,y=150)

        # Email
        self.label_email=Label(self.bottom,text="Email",font="Arial 15 bold",bg="white",fg="brown")
        self.label_email.place(x=50,y=200)

        self.entry_email=Entry(self.bottom,width=40,bd=4)
        self.entry_email.insert(0,person_email)
        self.entry_email.config(state="disable")
        self.entry_email.place(x=150,y=200)

        # Address
        self.label_address=Label(self.bottom,text="Address",font="Arial 15 bold",bg="white",fg="brown")
        self.label_address.place(x=50,y=250)

        self.entry_address=Text(self.bottom,width=40,height=7,bd=4)
        self.entry_address.insert(1.0,person_address)
        self.entry_address.config(state="disable")
        self.entry_address.place(x=150,y=250)