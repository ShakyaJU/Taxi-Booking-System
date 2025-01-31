class TripInfo(object):
    Booking_ID= Cust_ID= Pickup= Destination= Date= Time= Driver_ID=None
    def __init__(self, Pickup= None, Destination= None, Date= None, Time= None):
        self.Book_ID= 0
        self.Cust_ID= 0
        self.Pickup= Pickup
        self.Destination= Destination
        self.Date= Date
        self.Time= Time
        self.Driver_ID= 0

    def getCust_ID(self):
        return self.Cust_ID
    def setCust_ID(self, Cust_ID):
        self.Cust_ID= Cust_ID

    def getBooking_ID(self):
        return self.Book_ID
    def setBooking_ID(self, Booking_ID):
        self.Book_ID= Booking_ID

    def getPickup(self):
        return self.Pickup
    def setPickup(self, Pickup):
        self.Pickup= Pickup

    def getDestination(self):
        return self.Destination
    def setDestination(self, Destination):
        self.Destination= Destination

    def getDate(self):
        return self.Date
    def setDate(self, Date):
        self.Date= Date

    def getTime(self):
        return self.Time
    def setTime(self, Time):
        self.Time= Time

    def getDriver_ID(self):
        return self.Driver_ID
    def setDriver_ID(self, Driver_ID):
        self.Driver_ID = Driver_ID






