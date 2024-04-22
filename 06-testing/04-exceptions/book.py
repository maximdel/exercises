import re

class Book:
    def __init__(self, title, isbn):
        if not Book.__is_valid_isbn(isbn):
            raise RuntimeError("Invalid isbn")
        if not Book.__is_valid_title(title):
            raise RuntimeError("Invalid title")
        self.__title = title
        self.__isbn = isbn
    
    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    
    
    @staticmethod
    def __is_valid_title(title):
        return len(title) > 0
    
    @staticmethod
    def __is_valid_isbn(isbn):
        isbn = re.sub(r'(\D)', '', isbn)
        isbn = list(isbn[:])

        for i in range(len(isbn)):
            isbn[i] = int(isbn[i])
            if i % 2 != 0:
                isbn[i]= isbn[i] * 3
        return sum(isbn) %10 == 0
        

