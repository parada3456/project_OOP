#Coin.py
from datetime import datetime, timedelta
class GoldenCoin:
    def __init__(self,balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,new_balance):
        self.__balance = new_balance

class SilverCoin(GoldenCoin):
    def __init__(self,balance):
        super().__init__(balance)
        self.__exp_date_time = datetime.today() + timedelta(days=10)

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,amount):
        self.__balance -= amount 
    
    @property
    def exp_date_time(self):
        return self.__exp_date_time
    
    