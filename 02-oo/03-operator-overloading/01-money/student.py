class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount
        
    @property
    def currency(self):
        return self.__currency
    
    @currency.setter
    def currency(self, currency):
        self.__currency = currency
    
    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        raise RuntimeError()
    
    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        raise RuntimeError()
    
    def __mul__(self, other):
        return Money(self.amount * other, self.currency)
