from tkinter import *
from PIL import ImageTk

class AdminPg():
    def __init__(self):
        self.root = Tk()
        self.root.title("Admin Page")
        self.root.geometry("400x400+500+200")
        # self.root.bg = ImageTk.PhotoImage(file="C:/Users/LEGEND GAMEING PC/Pictures/Admin.jpg")
        # self.bg_image = Label(self.root, image=self.root.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.root.resizable(False, False)
        self.root.config(background='orange')
        #Adding Labels
        self.title = Label(self.root, text="Welcome Admin",
                           font=('Times New Roman', '15', 'bold'),
                           background='yellow')
        self.title.place(x=125, y=20)
        self.title1 = Label(self.root, text="What would you like to do?",
                       font=('Times New Roman', '15', 'bold'),
                       background='yellow')
        self.title1.place(x=80, y=50)


        #Adding Buttons
        viewC_button = Button(self.root, text="VIEW ALL CUSTOMERS", font=('times new roman', '12', 'bold'),
                                 command=lambda: [self.root.destroy(),self.viewallcustomer()])
        viewC_button.place(x=95, y=120, width=200)

        viewD_button = Button(self.root, text="VIEW ALL DRIVERS", font=('times new roman', '14', 'bold'),
                               command=lambda: [self.root.destroy(),self.viewalldriver()])
        viewD_button.place(x=95, y=170, width=200)

        viewB_button = Button(self.root, text="VIEW ALL BOOKINGS", font=('times new roman', '13', 'bold'),
                               command=lambda: [self.root.destroy(),self.viewBookingAdmin()])
        viewB_button.place(x=95, y=230, width=200)

        logout_button = Button(self.root, text="LOGOUT", font=('times new roman', '15', 'bold'),
                             command=lambda: [self.root.destroy(), self.openlog()])
        logout_button.place(x=95, y=280, width=200)


        self.root.mainloop()

#function for logging out from the admin page in LOGOUT button command
    def openlog(self):
        from FrontEndLayer.LoginPage import LoginPg
        login= LoginPg()

#function to open AdmViewCustomer page in "VIEW ALL CUSTOMER" button command
    def viewallcustomer(self):
        from FrontEndLayer.AdmViewCustomer import AdmViewCustomer
        open= AdmViewCustomer()

# function to open AdmViewDriver page in "VIEW ALL DRIVERS" button command
    def viewalldriver(self):
        from FrontEndLayer.AdmViewDriver import AdmViewDriver
        open= AdmViewDriver()

# function to open AdmViewBooking page in "VIEW ALL BOOKINGS" button command
    def viewBookingAdmin(self):
        from FrontEndLayer.AdmViewBooking import AdmViewBooking
        open= AdmViewBooking()


