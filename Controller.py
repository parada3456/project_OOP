import Book
import Chapter
import ChapterTransaction
import CoinTransaction
import Reader


class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__payment_list = []
        self.__promotion_list = []
        self.__report_type_list = ["violence","harrasment"]

    def add_reader(self, reader):
        self.__reader_list.append(reader)

    def search_book_by_name(self, book_name):
        search_list=[]
        for writer in self.__writer_list:
            for book in writer.writing_book_list:
                if book_name.lower() in book.name.lower():
                    search_list.append(book.name)
                    
        if search_list==[]:
            return "huhuuuu"
        else:
            return search_list
          
    def search_user(self, username):
        search_list = []
        for reader in self.__reader_list:
            if username.lower() in reader.username.lower():
                search_list.append(reader.username)
        
        for writer in self.__writer_list:
            if username.lower() in writer.username.lower() and writer.username not in search_list:
                search_list.append(writer.username)

        if search_list == []:
            return "user not found"
        else:
            return search_list
        
    def search_writer_by_username(self,writer_username):
        for writer in self.__writer_list:
            if writer_username.lower() == writer.username.lower() :
                return writer
        return "Not found writer"
    

    # def create_new_user(self,username,password,birth_date):
    #     new_reader = Reader.Reader(username,password,birth_date)
    #     if isinstance(new_reader,Reader.Reader)==True:
    #         self.add_reader(new_reader)
    #         return "sign up success"
    #     else : 
    #         return "please try again"
    

    @property
    def report_type_list(self):
        return self.__report_type_list
    
    @property
    def writer_list(self):
        return self.__writer_list

    def search_coin_promotion(self, code):
        pass

    def add_writer(self, writer):
        self.__writer_list.append(writer)

    def add_payment(self, payment):
        self.__payment_list.append(payment)

    def add_promotion(self, promotion):
        self.__promotion_list.append(promotion)

    def buy_chapter(self, chapter_id, book_id, user_id):
        pass

