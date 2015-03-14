####################################################################
#        Parking Lot                                               #                 
####################################################################

class ParkingLot(object):
    _carcount=0    
    def __init__(self,space):
       self.sp=space
       
       	
    @classmethod
    def park(self,cls):
        ParkingLot._carcount+=1
        	
        
        Car.car_slot(cls)        
        print ("Car count from classmethod",str(ParkingLot._carcount))
        
    def __str__(self):
        print ("Car count str",str(self._carcount))
        return (self._carcount)
    
####################################################################
#         Car Object                                               #                 
####################################################################

    
        
class Car(ParkingLot):
    
    def __init__(self,yr,model,make):        
        self.__make=make
        self.__model=model
        self.__yr=yr
        self.items =self.__make+" "+self.__model+" "+self.__yr
        
        	
        
    def  __iter__(self):
        for i in self.items:
            yield i
            
    def __str__(self):
        return (self.items)
    
    @classmethod
    def car_slot(cls,carlist):
        for yr,model,make in carlist:
            yield cls(yr,model,make)
####################################################################
#         Out put Section                                          #                 
####################################################################
lot=ParkingLot(2)

car = Car('Audi','R8', '2010')
ParkingLot.park(car)

car = Car('Honda', 'Vanagon', '1981')
ParkingLot.park(car)


car = Car('Buick','Regal', '1988')
car_lst=(('Audi','R8', '2010'),('VW', 'Vanagon', '1981'),('Buick','Regal', '1988'))
ParkingLot.park(car)
print(car)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
