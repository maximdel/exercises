class Cycle:
    def __init__(self, item):
        self.__item = list(item)
        self.__index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.__index = (self.__index + 1) % len(self.__item)
        return self.__item[self.__index]
