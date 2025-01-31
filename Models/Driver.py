class Driver(object):
    driver_ID= driver_Name= driver_Address= driver_Telephone= driver_Email= driver_Password= driver_Platenum= driver_Carmodel= None
    def __init__(self, driver_Name= None, driver_Address= None, driver_Telephone= None,
        driver_Email= None, driver_Password= None, driver_Platenum= None, driver_Carmodel= None):
        self.driver_ID= 0
        self.driver_Name= driver_Name
        self.driver_Address= driver_Address
        self.driver_Telephone= driver_Telephone
        self.driver_Email= driver_Email
        self.driver_Password= driver_Password
        self.driver_Platenum= driver_Platenum
        self.driver_Carmodel= driver_Carmodel

    def getDriver_ID(self):
        return self.driver_ID
    def setDriver_ID(self, driver_ID):
        self.driver_ID= driver_ID

    def getDriverName(self):
        return self.driver_Name
    def setDriverName(self, driver_Name):
        self.driver_Name= driver_Name

    def getDriverAddress(self):
        return self.driver_Address
    def setDriverAddress(self, driver_Address):
        self.driver_Address= driver_Address

    def getDriverTelephone(self):
        return self.driver_Telephone
    def setDriverTelephone(self, driver_Telephone):
        self.driver_Telephone= driver_Telephone

    def getDriverEmail(self):
        return self.driver_Email
    def setDriverEmail(self, driver_Email):
        self.driver_Email= driver_Email

    def getDriverPassword(self):
        return self.driver_Password
    def setDriverPassword(self, driver_Password):
        self.driver_Password= driver_Password

    def getDriverPlateNumber(self):
        return self.driver_Platenum
    def setDriverPlateNumber(self, driver_Platenum):
        self.driver_Platenum= driver_Platenum

    def getDriverCarModel(self):
        return self.driver_Carmodel
    def setDriverCarModel(self, driver_Carmodel):
        self.driver_Carmodel= driver_Carmodel






