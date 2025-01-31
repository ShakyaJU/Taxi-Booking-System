from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from BusinessLayer.BLDriver import BLDriver
from Models.Driver import Driver

class AdmViewDriver():
    def __init__(self):
        self.root = Tk()
        self.root.title("View Drivers")
        self.root.geometry("900x500")
        # self.root.bg = ImageTk.PhotoImage(file="C:/Users/LEGEND GAMEING PC/Pictures/ViewCD.jpg")
        # self.bg_image = Label(self.root, image=self.root.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.root.resizable(False, False)
        self.root.config(background="orange")

        self.title = Label(self.root, text="Driver Table",
                           font=('Times New Roman', '20', 'bold'),
                           background='yellow')
        self.title.place(x=350, y=20)

        back_button = Button(self.root, text="BACK", font=('times new roman', '15', 'bold'),
                             command=lambda: [self.root.destroy(), self.openAdmin()])
        back_button.place(x=80, y=410, width=200)

        # Create Treeview

        self.frame1 = Frame(self.root)
        self.frame1.place(x=40, y=100, width=840, height=200)
        self.treeview = ttk.Treeview(self.frame1)
        self.treeview['show'] = 'headings'

        self.treeview["columns"] = ("Driver_ID", "Driver_Name", "Driver_Address",
                        "Driver_Telephone", "Driver_PlateNumber", "Driver_CarModel", "Driver_Email", "Driver_Password")

        # assigning width, minwidth and anchor to the column

        self.treeview.column("Driver_ID", width=100, minwidth=80, anchor=CENTER)
        self.treeview.column("Driver_Name", width=130, minwidth=120, anchor=CENTER)
        self.treeview.column("Driver_Address", width=130, minwidth=100, anchor=CENTER)
        self.treeview.column("Driver_Telephone", width=100, minwidth=120, anchor=CENTER)
        self.treeview.column("Driver_PlateNumber", width=100, minwidth=120, anchor=CENTER)
        self.treeview.column("Driver_CarModel", width=90, minwidth=100, anchor=CENTER)
        self.treeview.column("Driver_Email", width=90, minwidth=100, anchor=CENTER)
        self.treeview.column("Driver_Password", width=90, minwidth=100, anchor=CENTER)


        # assigning texts and anchors to the headings

        self.treeview.heading("Driver_ID", text="Customer ID", anchor=CENTER)
        self.treeview.heading("Driver_Name", text="Name", anchor=CENTER)
        self.treeview.heading("Driver_Address", text="Address", anchor=CENTER)
        self.treeview.heading("Driver_Telephone", text="Telephone Number", anchor=CENTER)
        self.treeview.heading("Driver_PlateNumber", text="Liscense Plate", anchor=CENTER)
        self.treeview.heading("Driver_CarModel", text="Car Model", anchor=CENTER)
        self.treeview.heading("Driver_Email", text="Email", anchor=CENTER)
        self.treeview.heading("Driver_Password", text="Password", anchor=CENTER)

        vbooking = Driver()
        vb = BLDriver(vbooking)
        bb = vb.adminViewDbook()

        for i in range(len(bb)):
            self.treeview.insert(parent='', index='end', iid=i,
                values=(bb[i][0], bb[i][1], bb[i][2], bb[i][3], bb[i][4], bb[i][5], bb[i][6], bb[i][7]))

        # Pack Treeview
        self.treeview.pack()

        self.root.mainloop()

# Function for sending back to admin page while clicking on the back button
    def openAdmin(self):
        from FrontEndLayer.AdminPage import AdminPg
        login = AdminPg()
#AdmViewDriver()

