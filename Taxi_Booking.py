import math

class Taxi():
     
        
    def __init__(self,taxicount):
        self.booked = 'false'
        self.currentSpot = "A"
        self.freeTime = 6
        self.totalEarning = 0
        self.trips = []
        self.id = taxicount
   
    def setDetails(self,booked,currentSpot,freeTime,totalEarnings,tripDetails):
        self.booked = booked
        self.currentSpot = currentSpot
        self.freeTime = freeTime
        self.totalEarnings = totalEarnings
        self.trips.append(tripDetails)

   
    def printDetails(self):
        print('_____________________________________________________________________________________________')
        print(f"Taxi - {self.id} Total Earnings - {self.totalEarning}")
        print('')
        print("TaxiID    BookingID    CustomerID    From    To    PickupTime    DropTime    Amount")
        for trip in self.trips:
            print(f"{self.id}          {trip}")
        print("--------------------------------------------------------------------------------------------")
        print('')
                  

   
    def printTaxiDetails(self):
        print(f"Taxi - {self.id}  Total Earnings - {self.totalEarning}  Current spot - {self.currentSpot}  Free Time - {self.freeTime}")
        print('')
    
                  
                  
def createTaxis(n):
    taxis = []
    taxicount = 1
    for i in range(n):
        j = i+1
        t = Taxi(taxicount)
        taxis.append(t)
        taxicount = taxicount + 1
    return taxis



def getFreeTaxis(taxis,pick_tm,pickup_pt):
    freeTaxis = []
    for t in taxis:

        if(t.freeTime <= pick_tm and math.trunc((ord(t.currentSpot)) - (ord(pickup_pt))) <= (pick_tm - t.freeTime)):
            freeTaxis.append(t)
            
    return freeTaxis        
                  
                  
                  
def bookTaxi(customerID,pickup_pt,drop_pt,pick_tm,freeTaxis):
    min = 100  #to find nearest
    dbpnd = 0  #distance between pickup and drop 
    earning = 0  #this trip earning
    nft = 0     #next free time
    ns = 'Z'     #next spot
    bookedTaxi = 'null'
    td = ''       #all details of current trip as string
    
    for t in freeTaxis:
        
        dbct = math.trunc(ord(t.currentSpot) - ord(pickup_pt))*15
        if(dbct < min):
            bookedTaxi = t
            dbpnd = math.trunc(ord(drop_pt) - ord(pickup_pt)) * 15
            earning = (dbpnd - 5)*10 + 100
            drop_tm = pick_tm + dbpnd/15
            nft = drop_tm
            ns = drop_pt
            
            td = str(customerID) + "               " + str(customerID) + "          " + str(pickup_pt) +  "      " + str(drop_pt) + "       " + str(pick_tm) + "          " + str(drop_tm) + "           " + str(earning)
            min = dbct; 
    te = bookedTaxi.totalEarning + earning        
    bookedTaxi.setDetails('true',ns,nft,te,td)
    print('')
    print(f"Taxi {bookedTaxi.id} booked")
    print('')
taxis =[]
taxicount = 0
taxis = createTaxis(4)
id = 1
taxis[0].printTaxiDetails()
while('true'):
    print('0 -> Book Taxi')
    print('1 -> Print Taxi Details')
    choice = int(input())
    if(choice == 0):
        customerID = id
        pickup_pt = input('Enter Pickup point --> ')
        drop_pt = input('Enter Drop point --> ')
        pick_tm = int(input('Enter Pickup time --> '))
        
        if(pickup_pt < 'A' or pickup_pt > 'F' or drop_pt < 'A' or drop_pt > 'F'):
            print('Taxis are only available to travel from "A" to "F"')
            break
        
        freeTaxis = getFreeTaxis(taxis,pick_tm,pickup_pt)
        
        if(len(freeTaxis) == 0):
            print('No Taxi is available')
            brea1
            k
        
        #sort the free taxis based on their total earning
        
        #get free taxi nearest to us
        bookTaxi(id,pickup_pt,drop_pt,pick_tm,freeTaxis)
        id = id+1
    elif(choice == 1):
            for t in taxis:
                 t.printTaxiDetails()
            for t in taxis:
                 t.printDetails() 
    else:
        print('==> Please Enter 0 or 1')
        break