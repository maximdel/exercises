class Queue:
    def __init__(self):
        self.__queue = []
    
    def add(self, item):
        self.__queue.append(item)
    
    def next(self):
        next = self.__queue[0]
        del self.__queue[0]
        return next
    
    def is_empty(self):
        return len(self.__queue) == 0