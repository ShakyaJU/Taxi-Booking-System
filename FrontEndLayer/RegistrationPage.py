from tkinter import *
from BusinessLayer.BLCustomer import BLCustomer
from Models.Customer import Customer
from PIL import ImageTk

class RegistrationPg():
    def __init__(self):
        self.root= Tk()
        self.root.title("Registration Page")
        self.root.geometry("500x400")
        self.root.bg = ImageTk.PhotoImage(file="C:/Users/LEGEND GAMEING PC/Pictures/Regi.jpg")
        self.bg_image = Label(self.root, image=self.root.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.root.resizable(False, False)
        self.root.config(background= 'yellow')

        title= Label(self.root, text="Please fill up the registration form",
                     font=('Times New Roman', '20', 'bold'),
                     background='yellow')
        title.place(x= 40, y=20)

        name = Label(self.root, text="Name :",
                      font=('Times New Roman', '10', 'bold'),
                      background='yellow')
        name.place(x=100, y=80)
        self.name_entry = Entry(self.root)
        self.name_entry.place(x=220, y=80)

        address = Label(self.root, text="Address :",
                     font=('Times New Roman', '10', 'bold'),
                     background='yellow')
        address.place(x=100, y=110)
        self.address_entry = Entry(self.root)
        self.address_entry.place(x=220, y=110)

        telephone = Label(self.root, text="Telephone :",
                     font=('Times New Roman', '10', 'bold'),
                     background='yellow')
        telephone.place(x=100, y=140)
        self.telephone_entry = Entry(self.root)
        self.telephone_entry.place(x=220, y=140)

        email = Label(self.root, text="Email Address :",
                     font=('Times New Roman', '10', 'bold'),
                     background='yellow')
        email.place(x=100, y=170)
        self.email_entry = Entry(self.root)
        self.email_entry.place(x=220, y=170)

        password = Label(self.root, text="Password :",
                     font=('Times New Roman', '10', 'bold'),
                     background='yellow')
        password.place(x=100, y=200)
        self.password_entry = Entry(self.root, show='*')
        self.password_entry.place(x=220, y=200)

        confpw = Label(self.root, text="Conform Password :",
                         font=('Times New Roman', '10', 'bold'),
                         background='yellow')
        confpw.place(x=100, y=230)
        self.confpw_entry = Entry(self.root, show='*')
        self.confpw_entry.place(x=220, y=230)

        # CheckBox
        def show_password():
            if checkbox_value.get() == 1:
                # show password
                self.password_entry.config(show="")
                self.confpw_entry.config(show="")
            else:
                # hide password
                self.password_entry.config(show="*")
                self.confpw_entry.config(show="*")
        # create a checkbox
        checkbox_value = IntVar()
        checkbox = Checkbutton(self.root, text="Show password", background='white',
                               font=('Times New Roman', '10', 'bold'),
                               variable=checkbox_value, command=show_password)
        checkbox.place(x=180, y=260)

        register_button = Button(self.root, text="REGISTER", font=('times new roman', '10', 'bold'), command= self.register)
        register_button.place(x=130, y=300, width=100)

        back_button = Button(self.root, text="BACK", font=('times new roman', '10', 'bold'), command= lambda :[self.root.destroy(), self.openlog() ])
        back_button.place(x=240, y=300, width=100)


        self.root.mainloop()

    def register(self):
        Customer_Name= self.name_entry.get()
        Customer_Address= self.address_entry.get()
        Customer_Telephone= self.telephone_entry.get()
        Customer_Email= self.email_entry.get()
        Customer_Password= self.password_entry.get()
        regdetail= Customer(Customer_Name, Customer_Address, Customer_Telephone, Customer_Email, Customer_Password)
        bl= BLCustomer(regdetail)
        reg= bl.cust()
        if reg:
            self.root.destroy


    def openlog(self):
        from FrontEndLayer.LoginPage import LoginPg
        login= LoginPg()


