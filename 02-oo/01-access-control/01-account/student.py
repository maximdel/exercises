class Account:
    def __init__(self, login, password):
        self.__password = password
        self.login = login
    
    def is_correct_password(self, pw):
        return self.__password == pw

