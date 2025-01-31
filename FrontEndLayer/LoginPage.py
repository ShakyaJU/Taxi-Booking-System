from tkinter import *
from tkinter import messagebox
from FrontEndLayer.RegistrationPage import RegistrationPg
from FrontEndLayer.DriverRegistrationPage import DriverRegistrationPg
from Models.Customer import Customer
from Models.Driver import Driver
from BusinessLayer.BLCustomer import BLCustomer
from BusinessLayer.BLDriver import BLDriver
from PIL import ImageTk

class LoginPg():
    def __init__(self):
        self.root= Tk()
        self.root.title("Login Page")
        self.root.geometry("400x500+580+180") #Dimentions of the window
        self.root.bg = ImageTk.PhotoImage(file="C:/Users/LEGEND GAMEING PC/Pictures/TAXIpy.jpg")
        self.bg_image = Label(self.root, image=self.root.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.root.resizable(False, False)
        self.root.config(background="yellow")

        #Labels and Entries with their required dimentions
        self.title= Label(self.root, text="Welcome to Dunder Mifflin",
                            font=('Times New Roman', '20', 'bold'),
                            background='yellow')
        self.title.place(x=40, y=20)
        self.title1= Label(self.root, text="Taxi Company",
                            font=('Times New Roman', '20', 'bold'),
                            background='yellow')
        self.title1.place(x=110, y=50)

        email= Label(self.root, text="Email Address:",
                            font = ('Times New Roman', '10', 'bold'),
                            background = 'yellow')
        email.place(x=60, y=160)
        self.email_entry = Entry(self.root)
        self.email_entry.place(x=180, y=160)

        password = Label(self.root, text="Password: ",
                                font = ('Times New Roman', '10', 'bold'),
                                background = 'yellow')
        password.place(x=60, y=200)
        self.password_entry = Entry(self.root, show='*')
        self.password_entry.place(x=180, y=200)

        #CheckBox
        def show_password():
            if checkbox_value.get() == 1:
                # show password
                self.password_entry.config(show="")
            else:
                # hide password
                self.password_entry.config(show="*")
        # create a checkbox
        checkbox_value = IntVar()
        checkbox = Checkbutton(self.root, text="Show password", background= 'white',
                               font=('Times New Roman', '10', 'bold'),
                               variable=checkbox_value, command=show_password)
        checkbox.place(x=180, y=240)

        #Adding Buttons
        login_button= Button(self.root, text="LOGIN", font=('times new roman', '10', 'bold'), command= self.custLogin)
        login_button.place(x=130, y=290, width=140)

        driverlogin_button = Button(self.root, text="DRIVER LOGIN", font=('times new roman', '10', 'bold'), command=self.driverLogin)
        driverlogin_button.place(x=130, y=330, width=140)

        register_button= Button(self.root, text="REGISTER", font=('times new roman', '10', 'bold'),
                                command= lambda :[self.root.destroy(), RegistrationPg() ])
        register_button.place(x=130, y=370, width=140)

        driverregister_button = Button(self.root, text="DRIVER REGISTER", font=('times new roman', '10', 'bold'),
                                 command=lambda: [self.root.destroy(), DriverRegistrationPg()])
        driverregister_button.place(x=130, y=410, width=140)
        self.root.mainloop()

#Function for customer and admin login
    def custLogin(self):
        Customer_Email = self.email_entry.get()
        Customer_Password = self.password_entry.get()
    #Admin login
        if Customer_Email == "" or Customer_Password == "":
            messagebox.showerror("Error", "Email or Password is empty.")
        elif Customer_Email== "Admin123" and Customer_Password== "Admin123":
            messagebox.showinfo("Done!", "Login Successful. Welcome Admin")
            self.root.destroy()
            self.adminLog()
        else:
            cst = Customer()
            cst.setEmail(Customer_Email)
            cst.setPassword(Customer_Password)
            bl = BLCustomer(cst)
            lg = bl.logCustomer()

            if lg['status']:
                from FrontEndLayer.CustomerPage import CustomerPg
                messagebox.showinfo('Done!', 'Login Successful')
                self.root.destroy()
                log = lg['content']
                customer = Customer()
                customer.setCust_ID(log[0][0])
                customer.setName(log[0][1])
                CustomerPg(customer)
            # else:
            #     messagebox.showerror('error', 'Invalid Email or Password')

#Function for driver login
    def driverLogin(self):
        driver_Email = self.email_entry.get()
        driver_Password = self.password_entry.get()
        if driver_Email == "" or driver_Password == "":
            messagebox.showerror("Error", "Email or Password is empty.")
        else:
            dvr = Driver()
            dvr.setDriverEmail(driver_Email)
            dvr.setDriverPassword(driver_Password)
            bl = BLDriver(dvr)
            dlg = bl.logDriver()

            if dlg['status']:
                from FrontEndLayer.DriverPage import DriverPg
                messagebox.showinfo('Done!', 'Login Successful')
                self.root.destroy()
                log = dlg['content']
                driver = Driver()
                driver.setDriver_ID(log[0][0])
                driver.setDriverName(log[0][1])
                DriverPg(driver)
        # else:
        #     messagebox.showerror('error', 'Invalid Email or Password')

    #Function for logging into admin page
    def adminLog(self):
        from FrontEndLayer.AdminPage import AdminPg
        ap= AdminPg()


