class Vehicle:
 
    def __init__(self):
        self.__engine_type()
 
    def vehicle_type(self):
        print 'Car'
 
    def __engine_type(self):
        print 'Petrol'
 
V = Vehicle()
V.vehicle_type()
V.__engine_type()
# V._Vehicle__engine_type()