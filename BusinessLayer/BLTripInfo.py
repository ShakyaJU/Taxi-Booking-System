import sys
from tkinter import messagebox
from DatabaseLayer.DatabaseConnection import Dbconnect

class BLTripInfo():
    def __init__(self, trip):
        self.trip= trip

#function for booking a trip by entering the designated information
    def booktrip(self):
        conn= None
        sql= """INSERT INTO trip_information(Customer_ID, Pickup, Destination, Date, Time) VALUES (%s,%s,%s,%s,%s)"""

        values = (
           self.trip.getCust_ID(), self.trip.getPickup(), self.trip.getDestination(), self.trip.getDate(), self.trip.getTime())
        result = False
        try:
            conn = Dbconnect()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            cursor.close()
            result = True
            messagebox.showinfo('Done✓', 'Booked successfully. Please wait for the admin to assign your booking to the driver.')

        except:
            print("Error : ", sys.exc_info())
            messagebox.showerror('Error!', 'Unable to Book. Please fill the appropriate details.')
        finally:
            del values
            del sql
            return result

#Function for showing the booking done by the customer in customer page
    def viewbook(self):
        conn = None
        sql = """SELECT * FROM trip_information WHERE Customer_ID=%s"""
        values = (self.trip.getCust_ID(),)
        result = None
        try:
            conn = Dbconnect()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            content = cursor.fetchall()

            result = content

        except:
            print("Error : ", sys.exc_info())
        finally:
            del values
            del sql
            del conn
            return result

#Function for updating/chanding the bookings made by the customer
    def updatebook(self):
        conn= None
        sql = " Update  trip_information set Pickup= %s, Destination= %s,Date= %s,Time= %s where Booking_ID= %s"
        values = (self.trip.getPickup(), self.trip.getDestination(),
                  self.trip.getDate(), self.trip.getTime(), self.trip.getBooking_ID())
        result = False
        try:
            conn = Dbconnect()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            cursor.close()
            result = True
            messagebox.showinfo('Done!',
                    'Your booking has been updated successfully. Please relogin to view the updated details.')

        except:
            print("Error : ", sys.exc_info())
            messagebox.showerror('Error!', 'Unable to update. Please fill in the booking details.')
        finally:
            del values
            del sql
            return result

#Function for canceling the booking done by the customer
    def cancelbook(self):
        conn= None
        sql = " delete from trip_information where Booking_ID = %s"
        values = (self.trip.getBooking_ID(),)
        result = False
        try:
            conn = Dbconnect()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            cursor.close()
            result = True
            messagebox.showinfo('Done!', 'Your booking has been cancelled successfully')

        except:
            print("Error : ", sys.exc_info())
            messagebox.showerror('Error!', 'Unable to cancel.')
        finally:
            del values
            del sql
            return result

#function for viewing the booking assigned to a specific driver
    def view_driverbook(self):
        conn = None
        sql = """SELECT * FROM trip_information WHERE Driver_ID=%s"""
        values = (self.trip.getDriver_ID(),)
        result = None
        try:
            conn = Dbconnect()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            content = cursor.fetchall()

            result = content

        except:
            print("Error : ", sys.exc_info())
        finally:
            del values
            del sql
            del conn
            return result

    def assignDriver(self):
        conn= None
        sql = " Update trip_information set Driver_ID= %s where Booking_ID= %s"
        values = (self.trip.getDriver_ID(), self.trip.getBooking_ID())
        result = False
        try:
            conn = Dbconnect()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            cursor.close()
            result = True
            messagebox.showinfo('Done!', 'Booking has been assigned to the driver successfully')

        except:
            print("Error : ", sys.exc_info())
            messagebox.showerror('Error!', 'Unable to assign. Please fill in the details.')
        finally:
            del values
            del sql
            return result

    def admin_view_book(self):
        conn = None
        sql = """SELECT * FROM trip_information """

        result = None
        try:
            conn = Dbconnect()
            cursor = conn.cursor()
            cursor.execute(sql)
            content = cursor.fetchall()

            result = content

        except:
            print("Error : ", sys.exc_info())
        finally:

            del sql
            del conn
            return result

