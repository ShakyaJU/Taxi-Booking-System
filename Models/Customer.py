class Customer(object):
    Cust_ID= Name= Address= Telephone= Email= Password= None
    def __init__(self, Customer_Name= None, Customer_Address= None,
        Customer_Telephone= None, Customer_Email= None, Customer_Password= None):
        self.Cust_ID= 0
        self.Name= Customer_Name
        self.Address= Customer_Address
        self.Telephone= Customer_Telephone
        self.Email= Customer_Email
        self.Password= Customer_Password

    def getCust_ID(self):
        return self.Cust_ID
    def setCust_ID(self, Customer_ID):
        self.Cust_ID= Customer_ID

    def getName(self):
        return self.Name
    def setName(self, Customer_Name):
        self.Name= Customer_Name

    def getAddress(self):
        return self.Address
    def setAddress(self, Customer_Address):
        self.Address= Customer_Address

    def getTelephone(self):
        return self.Telephone
    def setTelephone(self, Customer_Telephone):
        self.Telephone= Customer_Telephone

    def getEmail(self):
        return self.Email
    def setEmail(self, Customer_Email):
        self.Email= Customer_Email

    def getPassword(self):
        return self.Password
    def setPassword(self, Customer_Password):
        self.Password= Customer_Password






