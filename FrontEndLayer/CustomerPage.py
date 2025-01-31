from tkinter import *
from BusinessLayer.BLTripInfo import BLTripInfo
from Models.TripInformation import TripInfo
from tkinter import ttk, messagebox
from PIL import ImageTk
from tkcalendar import *
from datetime import datetime,timedelta,date

# For Foreign key
customer_ID=0
name= None

class CustomerPg():
    def __init__(self, customer):
        self.root= Tk()
        global customer_ID, name
        customer_ID= customer.getCust_ID()
        name= customer.getName()
        self.root.title("Customer Page")
        self.root.geometry("1100x600")
        self.root.bg = ImageTk.PhotoImage(file="C:/Users/LEGEND GAMEING PC/Pictures/Cmap.png")
        self.bg_image = Label(self.root, image=self.root.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.root.resizable(False, False)
        self.root.config(background="yellow")
        self.title = Label(self.root, text="Welcome to our services",
                           font=('Times New Roman', '20', 'bold'),
                           background='yellow')
        self.title.place(x=400, y=20)
        #Labels and entries for customer interface
        title1 = Label(self.root, text="Please enter the following details for booking Taxi",
                       font=('Times New Roman', '20', 'bold'),
                       background='yellow')
        title1.place(x=260, y=60)

        title2 = Label(self.root, text="View Your Booking.",
                       font=('Times New Roman', '15', 'bold'),
                       background='white')
        title2.place(x=620, y=130)

        bID = Label(self.root, text="Booking ID:",
                       font=('Times New Roman', '10', 'bold'),
                       background='yellow')
        bID.place(x=50, y=160)
        self.bID_entry = Entry(self.root)
        self.bID_entry.place(x=180, y=160)

        pickup = Label(self.root, text="Pickup Location:",
                      font=('Times New Roman', '10', 'bold'),
                      background='yellow')
        pickup.place(x=50, y=200)
        self.pickup_entry = Entry(self.root)
        self.pickup_entry.place(x=180, y=200)

        destination = Label(self.root, text="Destination Location: ",
                         font=('Times New Roman', '10', 'bold'),
                         background='yellow')
        destination.place(x=50, y=240)
        self.destination_entry = Entry(self.root)
        self.destination_entry.place(x=180, y=240)

        #Date Entry
        Choosedate = Label(self.root, text="Choose Date: ",
                         font=('Times New Roman', '10', 'bold'),
                         background='yellow')
        Choosedate.place(x=50, y=280)

        date_today = datetime.now()  # today's date
        max_date = date.today() + timedelta(days=10)
        self.date_entry = DateEntry(self.root, selectmode='day', mindate=date_today, maxdate=max_date, bg="light gray", bd=2)
        self.date_entry.place(x=180, y=280, width=130, height=25)

        #COmbobox for time entry
        Choosetime = Label(self.root, text="Choose Time: ",
                           font=('Times New Roman', '10', 'bold'),
                           background='yellow')
        Choosetime.place(x=50, y=320)

        self.time_entry = ttk.Combobox(self.root)

        self.time_entry['values'] = (
            "8:00 Am", "9:00 Am", "10:00 Am", "11:00 Am", "12:00 Am", "1:00 Pm", "2:00 Pm", "3:00 Pm", "4:00 Pm",
            "5:00 Pm", "6:00 Pm", "7:00 Pm", "8:00 Pm")
        self.time_entry['state'] = 'readonly'
        self.time_entry.place(x=180, y=320, width=130, height=25)

        book_button = Button(self.root, text="BOOK", font=('times new roman', '15', 'bold'), command= self.book )
        book_button.place(x=80, y=360, width=200)

        viewbook_button = Button(self.root, text="UPDATE BOOKING", font=('times new roman', '15', 'bold'), command= self.update )
        viewbook_button.place(x=80, y=410, width=200)

        cancel_button = Button(self.root, text="CANCEL BOOKING", font=('times new roman', '15', 'bold'), command= self.cancel)
        cancel_button.place(x=80, y=460, width=200)

        logout_button = Button(self.root, text="LOGOUT", font=('times new roman', '15', 'bold'), command= lambda :[self.root.destroy(), self.openlog() ])
        logout_button.place(x=80, y=510, width=200)

        # Create Treeview
        self.frame1= Frame(self.root)
        self.frame1.place(x=420, y=160, width=600, height=200)
        self.treeview= ttk.Treeview(self.frame1)
        self.treeview['show']= 'headings'

        self.treeview["columns"]= ("Booking_ID", "Pickup", "Destination", "Date", "Time")

        #assigning width, minwidth and anchor to the column
        self.treeview.column("Booking_ID", width=100, minwidth=120, anchor=CENTER)
        self.treeview.column("Pickup", width=130, minwidth=120, anchor=CENTER)
        self.treeview.column("Destination", width=130, minwidth=120, anchor=CENTER)
        self.treeview.column("Date", width=80, minwidth=120, anchor=CENTER)
        self.treeview.column("Time", width=80, minwidth=120, anchor=CENTER)

        #assigning texts and anchors to the headings
        self.treeview.heading("Booking_ID", text="Booking ID", anchor=CENTER)
        self.treeview.heading("Pickup", text="Pickup Location", anchor=CENTER)
        self.treeview.heading("Destination", text="Destination Location", anchor=CENTER)
        self.treeview.heading("Date", text="Date", anchor=CENTER)
        self.treeview.heading("Time", text="Time", anchor=CENTER)

        vbooking = TripInfo()
        vbooking.setCust_ID(int(customer_ID))
        vb = BLTripInfo(vbooking)
        bb = vb.viewbook()

        for i in range(len(bb)):
            self.treeview.insert(parent='', index='end', iid=i, values=(bb[i][0], bb[i][2], bb[i][3], bb[i][4], bb[i][5]))

        # Pack Treeview
        self.treeview.pack()

        self.root.mainloop()

#Function for booking a taxi done by the customer in BOOK button command
    def book(self):
        pickup = self.pickup_entry.get()
        destination = self.destination_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        tripdetail = TripInfo()
        tripdetail.setPickup(pickup)
        tripdetail.setDestination(destination)
        tripdetail.setDate(date)
        tripdetail.setTime(time)
        tripdetail.setCust_ID(customer_ID)

        bl = BLTripInfo(tripdetail)
        book = bl.booktrip()

    def update(self):
        booking_ID = self.bID_entry.get()
        pickup = self.pickup_entry.get()
        destination = self.destination_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()


        tripdetail = TripInfo()
        tripdetail.setPickup(pickup)
        tripdetail.setDestination(destination)
        tripdetail.setDate(date)
        tripdetail.setTime(time)

        tripdetail.setBooking_ID(booking_ID)
        ub= BLTripInfo(tripdetail)
        upbook= ub.updatebook()

    def cancel(self):
        booking_ID = self.bID_entry.get()

        tripdetail = TripInfo()
        tripdetail.setBooking_ID(booking_ID)
        ub = BLTripInfo(tripdetail)
        upbook = ub.cancelbook()


    #Function for sending to login page while clicking on the back button
    def openlog(self):
        from FrontEndLayer.LoginPage import LoginPg
        login = LoginPg()










