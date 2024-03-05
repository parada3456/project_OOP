import Controller
import Reader
import main

class Payment:
    def __init__(self):
        self.__coin_promotion = []
    #=================================
    @property
    def coin_promotion(self):
        return self.__coin_promotion

class OnlineBanking(Payment):
    def __init__(self, account_id):
        self.__account_id = account_id
    #==================================
    @property
    def account_id(self):
        return self.__account_id
    #==================================method
    def buy_coin(self, username, code, coin_amount):
        coin_cost = coin_amount * 2
        user = Controller.search_user(username)
        if(code != None):
            coin_promotion = Controller.search_coin_promotion(code)
            if(coin_promotion != None):
                coin_cost = (100 - coin_promotion.discount) / 100 * coin_cost #ลดราคา 


            else:
                return "Your code is expired or not exist"

class DebitCard(Payment):
    def __init__(self, card_id, exp_date, cvv):
        self.__card_id = card_id
        self.__exp_date = exp_date
        self.__cvv = cvv
    #==================================
    @property
    def card_id(self):
        return self.__card_id
    @property
    def card_id(self):
        return self.__card_id
    @property
    def card_id(self):
        return self.__card_id
    #==================================method
    def buy_coin(self, user_name, code, amount):
        pass


class TrueMoneyWallet(Payment):
    def __init__(self, phone_number, otp_number):
        self.__phone_number = phone_number
        self.__otp_number = otp_number
    #==================================
    @property
    def phone_number(self):
        return self.__phone_number
    @property
    def otp_number(self):
        return self.__otp_number
    #==================================method
    def buy_coin(self, user_name, code, amount):
        pass

