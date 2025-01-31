from tkinter import *
from BusinessLayer.BLDriver import BLDriver
from BusinessLayer.BLTripInfo import BLTripInfo
from Models.TripInformation import TripInfo
from Models.Driver import Driver
#from PIL import ImageTk
from tkinter import ttk

class AdmViewBooking():
    def __init__(self, ):
        self.root= Tk()
        self.root.title("Driver Interface Page")
        self.root.geometry("1300x600")
        self.root.resizable(False, False)
        self.root.config(background="orange")

        self.title = Label(self.root, text="Hello Admin",
                           font=('Times New Roman', '20', 'bold'),
                           background='yellow')
        self.title.place(x=600, y=20)
        title1 = Label(self.root, text="Please assign the drivers.",
                       font=('Times New Roman', '20', 'bold'),
                       background='yellow')
        title1.place(x=530, y=50)

        dvrID = Label(self.root, text="Driver ID:",
                    font=('Times New Roman', '10', 'bold'),
                    background='yellow')
        dvrID.place(x=30, y=160)
        self.dvrID_entry = Entry(self.root)
        self.dvrID_entry.place(x=120, y=160)

        bookID = Label(self.root, text="Booking ID:",
                      font=('Times New Roman', '10', 'bold'),
                      background='yellow')
        bookID.place(x=30, y=200)
        self.bookID_entry = Entry(self.root)
        self.bookID_entry.place(x=120, y=200)

        back_button = Button(self.root, text="BACK", font=('times new roman', '15', 'bold'),
                             command=lambda: [self.root.destroy(), self.openAdmin()])
        back_button.place(x=60, y=340, width=200)

        assign_button = Button(self.root, text="ASSIGN DRIVER", font=('times new roman', '15', 'bold'),
                                 command=self.assign)
        assign_button.place(x=60, y=280, width=200)

        # Create Treeview

        self.frame1 = Frame(self.root)
        self.frame1.place(x=650, y=180, width=550, height=200)

        self.treeview = ttk.Treeview(self.frame1)

        self.treeview['show'] = 'headings'

        self.treeview["columns"] = ("Booking_ID", "Pickup", "Destination", "Date", "Time")

        # assigning width, minwidth and anchor to the column

        self.treeview.column("Booking_ID", width=100, minwidth=120, anchor=CENTER)
        self.treeview.column("Pickup", width=130, minwidth=100, anchor=CENTER)
        self.treeview.column("Destination", width=130, minwidth=120, anchor=CENTER)
        self.treeview.column("Date", width=90, minwidth=100, anchor=CENTER)
        self.treeview.column("Time", width=90, minwidth=100, anchor=CENTER)


        # assigning texts and anchors to the headings

        self.treeview.heading("Booking_ID", text="Booking ID", anchor=CENTER)
        self.treeview.heading("Pickup", text="Pickup Location", anchor=CENTER)
        self.treeview.heading("Destination", text="Destination Location", anchor=CENTER)
        self.treeview.heading("Date", text="Date", anchor=CENTER)
        self.treeview.heading("Time", text="Time", anchor=CENTER)

        abook = TripInfo()
        asb = BLTripInfo(abook)
        ab = asb.admin_view_book()


        for i in range(len(ab)):
            self.treeview.insert(parent='', index='end', iid=i,
                                 values=(ab[i][0], ab[i][2], ab[i][3], ab[i][4], ab[i][5], ab[i][6]))

        # Pack Treeview
        self.treeview.pack()

        self.frame2 = Frame(self.root)
        self.frame2.place(x=300, y=180, width=360, height=200)
        self.treeview1 = ttk.Treeview(self.frame2)
        self.treeview1['show'] = 'headings'

        self.treeview1["columns"] = ("Driver_ID", "Driver_Name","Driver_CarModel")

        # assigning width, minwidth and anchor to the column

        self.treeview1.column("Driver_ID", width=110, minwidth=100, anchor=CENTER)
        self.treeview1.column("Driver_Name", width=130, minwidth=130, anchor=CENTER)

        self.treeview1.column("Driver_CarModel", width=119, minwidth=130, anchor=CENTER)


        # assigning texts and anchors to the headings

        self.treeview1.heading("Driver_ID", text="Driver ID", anchor=CENTER)
        self.treeview1.heading("Driver_Name", text="Name", anchor=CENTER)

        self.treeview1.heading("Driver_CarModel", text="Car Model", anchor=CENTER)


        vbooking = Driver()
        vb = BLDriver(vbooking)
        bb = vb.adminViewDbook()

        for i in range(len(bb)):
            self.treeview1.insert(parent='', index='end', iid=i,
                                 values=(
                                 bb[i][0], bb[i][1], bb[i][5]))

        # Pack Treeview
        self.treeview1.pack()

        self.root.mainloop()

        # Function for sending back to admin page while clicking on the back button
    def openAdmin(self):
        from FrontEndLayer.AdminPage import AdminPg
        login = AdminPg()

#function for assigning booking to the driver by the admin
    def assign(self):

        driver_ID= self.dvrID_entry.get()
        booking_ID= self.bookID_entry.get()
        adminAssign= TripInfo()
        adminAssign.setDriver_ID(driver_ID)
        adminAssign.setBooking_ID(booking_ID)
        ad= BLTripInfo(adminAssign)
        assignBook= ad.assignDriver()

#AdmViewBooking()



