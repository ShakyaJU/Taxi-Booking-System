import mysql.connector
import sys
def Dbconnect():
    conn=None
    try:
        conn= mysql.connector.connect(host='localhost',
                                      port='3306',
                                      user='root',
                                      password='',
                                      database="tbs_assignment")
    except:
        print("Error :", sys.exc_info())
    finally:
        return conn