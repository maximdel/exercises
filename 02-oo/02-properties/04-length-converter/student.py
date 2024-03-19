class LengthConverter:
    def __init__(self):
        self.__length_in_meter = 0

    @property
    def meter(self):
        return self.__distance_in_meter
    
    @meter.setter
    def meter(self, distance):
        self.__distance_in_meter = distance
        
        
    @property
    def inch(self):
        return self.__distance_in_meter * 39.3701

    @inch.setter
    def inch(self, distance):
        self.__distance_in_meter = distance / 39.3701
    
    
    @property
    def feet(self):
        return self.__distance_in_meter * 3.28084
    
    @feet.setter
    def feet(self, distance):
        self.__distance_in_meter = distance / 3.28084