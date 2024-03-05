from Book import Book
from Chapter import Chapter
import ChapterTransaction
import CoinTransaction
from Reader import Reader
from Reader import Writer
from Comment import Comment


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
                    
    def get_book_by_name(self, book_name):
        for writer in self.__writer_list:
            for book in writer.book:
                if book.name == book_name:
                    return book
                
    def get_user_by_username(self, username):
        for reader in self.__reader_list:
            if reader.username == username:
                return reader
        
        for writer in self.__writer_list:
            if writer.username == username:
                return writer
            
        return "User Not Found"
    
    def search_chapter_by_chapter_id(self,chapter_id):
        for writer in self.__writer_list:
            for book in writer.writing_list:
                for chapter in book.chapter_list:
                    if chapter.chapter_id == chapter_id:
                        return chapter
        return "Not found"

    def search_all_username_list(self):
        username_list = []
        for reader in self.__reader_list:
            username_list.append(reader.name)
        for writer in self.__writer_list:
            username_list.append(writer.name)
        return username_list
    
    @property
    def report_type_list(self):
        return self.__report_type_list
    @property
    def report_type_list(self):
        return self.__report_type_list

    def search_coin_promotion(self, code):
        pass

    def add_writer(self, writer):
        self.__writer_list.append(writer)

    def add_payment(self, payment):
        self.__payment_list.append(payment)

    def add_promotion(self, promotion):
        self.__promotion_list.append(promotion)

    def buy_chapter(self, chapter_id, book_name, username):
        book = self.get_book_by_name(book_name)
        chapter_list = book.get_chapter_list()

        for chapter in chapter_list:
            if chapter.chapter_id == chapter_id:
                cost = chapter.cost

        user = self.get_user_by_username(username)
        coin_balance = user.get_user_coin_balance()

        if coin_balance >= cost:
            user.deduct_coin(cost)
            user.add_chapter_transaction()
        else:
            return "Not enough coin"
        
    def show_coin(self, username):
        user = self.get_user_by_username(username)
        if user:
            return f"Golden Coin : {user.golden_coin.balance} | Silver Coin : {user.get_silver_coin_balance()}"
        return "User Not Found"
    
    def sign_in(self,username, password):
        user = self.search_user(username)
        if (isinstance(user,Reader) or isinstance(user,Writer)) and user.password == password:
            return "log in successfully"
        else:
            return "can not find username/password"
    
    def sign_up(self,username:str, password:str, birth_date: str):
        if username not in self.search_all_username_list:
            new_reader = Reader(username,password,birth_date)
            self.add_reader(new_reader)
            return {"User": "sign up successfully"}
        else : 
            return {"User": "invalid username"}
        
    def create_book(self,name:str, writer_name:str, tag_list: str, status: str, age_restricted: bool, prologue: str):
        writer = self.search_user(writer_name)
        if isinstance(writer,Writer):
            new_book = Book(name,writer,tag_list,status,age_restricted,prologue)
        if isinstance(new_book,Book)==True:
            return {"Book": "create book successfully"}
        else : 
            return {"Book": "please try again"}
        
    def create_comment(self, chapter_id, username, context):
        chapter = self.search_chapter_by_chapter_id(chapter_id)
        user = self.search_user(username)
        if isinstance(chapter,Chapter):
            new_comment = Comment(chapter,user,context)
        if isinstance(new_comment,Comment)==True:
            return {"Comment": "create comment success"}
        else : 
            return {"Comment": "please try again"}
        
    def show_my_page(self, username):
        writing_count = 0
        reads = 0
        writing_list = None
        pseudonym_list = None
        comments = None
        user = self.get_user_by_username(username)
        if isinstance(user, Writer):
            writing_count = len(user.get_writing_list())
            reads = user.get_viewer_count()
            writing_list = user.get_writing_name_list()
            pseudonym_list = user.get_pseudonym_list()
            comment_list = user.get_json_comment_list()
        else:
            return "User Not Found"
        return {"display_name" : user.display_name,
                "introduction" : user.introduction,
                "writing_count" : writing_count,
                "book_on_shelf_count" : len(user.get_book_shelf_list()),
                "followers" : len(user.get_follower_list()),
                "read_count" : len(user.get_recent_read_chapter_list()),
                "viewer_count" : reads,
                "writings" : writing_list,
                "pseudonyms" : pseudonym_list,
                "comments" : comment_list}
    
    def show_my_profile(self, username):
        writing_count = 0
        reads = 0
        writing_list = None
        pseudonym_list = None
        comments = None
        user = self.get_user_by_username(username)
        if isinstance(user, Writer):
            writing_count = len(user.get_writing_list())
            reads = user.get_viewer_count()
            writing_list = user.get_writing_name_list()
            pseudonym_list = user.get_pseudonym_list()
            comment_list = user.get_json_comment_list()
        else:
            return "User Not Found"
        return {"display_name" : user.display_name,
                "username" : user.username,
                "password" : "*" * len(user.password),
                "book_on_shelf_count" : len(user.get_book_shelf_list()),
                "followers" : len(user.get_follower_list()),
                "read_count" : len(user.get_recent_read_chapter_list()),
                "viewer_count" : reads,
                "writings" : writing_list,
                "pseudonyms" : pseudonym_list,
                "comments" : comment_list}
