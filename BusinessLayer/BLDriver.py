import sys
from tkinter import messagebox
import re
from DatabaseLayer.DatabaseConnection import Dbconnect

class BLDriver():
    def __init__(self, driver):
        self.driver= driver

    def logDriver(self):
        conn = None
        sql = """SELECT * FROM driver_data WHERE Driver_Email = %s and Driver_Password= %s"""
        values = (self.driver.getDriverEmail(), self.driver.getDriverPassword())
        result = {'status': False, 'content': None}
        try:
            conn = Dbconnect()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            content = cursor.fetchall()
            if len(content) == 0 or content is None:
                result['status'] = False
                messagebox.showerror('Error','Invalid Email or Password')
            else:
                result['status'] = True
                result['content'] = content

        except:
            print("Error : ", sys.exc_info())
        finally:
            del values
            del sql
            del conn
            return result

    def driverReg(self):
        if not self.validemail():
            messagebox.showerror('Error!', 'Unable to Register. Please fill in the registration details or the email format is invalid.')
            return False
        conn = None
        sql = """INSERT INTO driver_data(Driver_Name, Driver_Address, Driver_Telephone, Driver_PlateNumber, Driver_CarModel, Driver_Email, 
           Driver_Password) VALUES (%s,%s,%s,%s,%s,%s,%s)"""

        values = (
            self.driver.getDriverName(), self.driver.getDriverAddress(), self.driver.getDriverTelephone(),
            self.driver.getDriverPlateNumber(),
            self.driver.getDriverCarModel(), self.driver.getDriverEmail(), self.driver.getDriverPassword())
        result = False
        try:
            conn = Dbconnect()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            cursor.close()
            result = True
            messagebox.showinfo('Done!', 'Your account has been registred successfully')

        except:
            print("Error : ", sys.exc_info())
            messagebox.showerror('Error!', 'Unable to Register. Please fill in the registration details')
        finally:
            del values
            del sql
            return result

    # Validation for email and password
    def validemail(self):
        regex = r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$"
        if re.match(regex, self.driver.getDriverEmail()):
            return True
        return False

#Function for showing all the customer data
    def adminViewDbook(self):
        conn = None
        sql = """SELECT * FROM driver_data"""

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

