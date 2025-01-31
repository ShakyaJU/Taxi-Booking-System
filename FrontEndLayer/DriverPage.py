from tkinter import *
from BusinessLayer.BLTripInfo import BLTripInfo
from Models.TripInformation import TripInfo
from PIL import ImageTk
from tkinter import ttk

#For Foreign key
driver_ID=0

class DriverPg():
    def __init__(self, driver):
        self.root= Tk()
        global driver_ID
        driver_ID = driver.getDriver_ID()
        self.root.title("Driver Interface Page")
        self.root.geometry("1000x600")
        self.root.bg = ImageTk.PhotoImage(file="C:/Users/LEGEND GAMEING PC/Pictures/Dvr.jpg")
        self.bg_image = Label(self.root, image=self.root.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.root.resizable(False, False)
        self.root.config(background="yellow")
        self.title = Label(self.root, text="Welcome to our services",
                           font=('Times New Roman', '20', 'bold'),
                           background='yellow')
        self.title.place(x=350, y=20)
        title1 = Label(self.root, text="Here are your bookings.",
                       font=('Times New Roman', '20', 'bold'),
                       background='yellow')
        title1.place(x=350, y=50)

        back_button = Button(self.root, text="LOGOUT", font=('times new roman', '15', 'bold'),
                             command=lambda: [self.root.destroy(), self.openlog()])
        back_button.place(x=80, y=510, width=200)

        # Create Treeview
        self.frame1 = Frame(self.root)
        self.frame1.place(x=250, y=150, width=550, height=200)
        self.treeview = ttk.Treeview(self.frame1)
        self.treeview['show'] = 'headings'
        self.treeview["columns"] = ("Booking_ID", "Pickup", "Destination", "Date", "Time")

        # assigning width, minwidth and anchor to the column
        self.treeview.column("Booking_ID", width=100, minwidth=100, anchor=CENTER)
        self.treeview.column("Pickup", width=130, minwidth=100, anchor=CENTER)
        self.treeview.column("Destination", width=130, minwidth=100, anchor=CENTER)
        self.treeview.column("Date", width=90, minwidth=100, anchor=CENTER)
        self.treeview.column("Time", width=90, minwidth=100, anchor=CENTER)

        # assigning texts and anchors to the headings
        self.treeview.heading("Booking_ID", text="Booking ID", anchor=CENTER)
        self.treeview.heading("Pickup", text="Pickup Location", anchor=CENTER)
        self.treeview.heading("Destination", text="Destination Location", anchor=CENTER)
        self.treeview.heading("Date", text="Date", anchor=CENTER)
        self.treeview.heading("Time", text="Time", anchor=CENTER)

        vbooking = TripInfo()
        vbooking.setDriver_ID(int(driver_ID))
        vb = BLTripInfo(vbooking)
        bb = vb.view_driverbook()

        for i in range(len(bb)):
            self.treeview.insert(parent='', index='end', iid=i, values=(bb[i][0], bb[i][2], bb[i][3], bb[i][4], bb[i][5]))

        # Pack Treeview
        self.treeview.pack()

        self.root.mainloop()

        # Function for sending to login page while clicking on the back button
    def openlog(self):
        from FrontEndLayer.LoginPage import LoginPg
        login = LoginPg()





