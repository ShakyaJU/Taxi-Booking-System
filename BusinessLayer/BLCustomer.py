import sys
from tkinter import messagebox
from DatabaseLayer.DatabaseConnection import Dbconnect
import re

class BLCustomer():
    def __init__(self, customer):
        self.customer= customer

    def logCustomer(self):
        conn = None
        sql = """SELECT * FROM customer_data WHERE Customer_Email = %s and Customer_Password= %s"""
        values = (self.customer.getEmail(), self.customer.getPassword())
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

    def cust(self):
        if not self.validemail():
            messagebox.showerror('Error!', 'Unable to Register. Please fill in the registration details.')
            return False
        conn = None
        sql = """INSERT INTO customer_data(Customer_Name, Customer_Address, Customer_Telephone, Customer_Email, 
        Customer_Password) VALUES (%s,%s,%s,%s,%s)"""

        values = (
        self.customer.getName(), self.customer.getAddress(), self.customer.getTelephone(), self.customer.getEmail(),
        self.customer.getPassword())
        result = False
        try:
            conn = Dbconnect()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            cursor.close()
            result = True
            messagebox.showinfo('Done!', 'Your account has been registred successfully. Please login to book your Taxi.')

        except:
            print("Error : ", sys.exc_info())
            messagebox.showerror('Error!', 'Unable to Register. Please fill in the registration details.')
        finally:
            del values
            del sql
            return result



    #Validation for email and password
    def validemail(self):
        regex = r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$"
        if re.match(regex, self.customer.getEmail()):
            return True
        return False

#Function for showing all the customer data
    def adminViewCbook(self):
        conn = None
        sql = """SELECT * FROM customer_data"""

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


