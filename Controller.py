from Comment import Comment
from Chapter import Chapter
from Book import Book
from Reader import Reader, Writer


class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__payment_list = []
        self.__promotion_list = []
        self.__report_type_list = ["violence","harrasment"]

    def add_reader(self, reader):
        self.__reader_list.append(reader)

    def search_book_and_user_list(self, search_str):
        search_book_list=[]
        search_reader_list=[]
        search_writer_list=[]
        for writer in self.__writer_list:
            for book in writer.writing_list:
                if search_str.lower() in book.name.lower():
                    search_book_list.append(book.name)

        for reader in self.__reader_list:
            if search_str.lower() in reader.username.lower():
                search_reader_list.append(reader.username)
        
        for writer in self.__writer_list:
            if search_str.lower() in writer.username.lower():
                search_writer_list.append(writer.username)

        search_dict = {"Book": search_book_list,"Reader": search_reader_list, "Writer": search_writer_list}

        if search_book_list == [] and search_reader_list == [] and search_writer_list == []:
            return "huhuuuu"
        else:
            return search_dict
          
    # def search_user_list_by_name(self, username):
        # search_list = []
        # for reader in self.__reader_list:
        #     if username.lower() in reader.username.lower():
        #         search_list.append(reader.username)
        
        # for writer in self.__writer_list:
        #     if username.lower() in writer.username.lower() and writer.username not in search_list:
        #         search_list.append(writer.username)

        # if search_list == []:
        #     return "user not found"
        # else:
        #     return search_list
                    
    def get_book_by_name(self, book_name):
        for writer in self.__writer_list:
            for book in writer.writing_list:
                if book.name == book_name:
                    return book
                
    def get_user_by_username(self, username):
        for reader in self.__reader_list:
            if reader.username.lower() == username.lower():
                return reader
        
        for writer in self.__writer_list:
            if writer.username.lower() == username.lower():
                return writer
            
        return "User Not Found"
    
    def search_chapter_by_chapter_id(self,chapter_id):
        for writer in self.__writer_list:
            for book in writer.writing_list:
                for chapter in book.chapter_list:
                    if chapter.chapter_id == chapter_id:
                        return chapter
        return "Not found"
    
    def search_book_by_chapter(self,insert_chapter):
        for writer in self.__writer_list:
            for book in writer.writing_list:
                for chapter in book.chapter_list:
                    if chapter == insert_chapter:
                        return book
        return "Not found"

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
        # print(user)
        if user:
            return f"Golden Coin : {user.golden_coin.balance} | Silver Coin : {user.silver_coin_balance}"
        return "User Not Found"
    
    def sign_in(self,username, password):
        user = self.get_user_by_username(username)
        print(user.username, user.password, user.birth_date)
        if (isinstance(user,Reader) or isinstance(user,Writer)):
            if user.password == password:
                return "log in successfully"
            else: 
                return "wrong password"
        else:
            return "can not find username/password"
    
    def sign_up(self,username:str, password:str, birth_date: str, role: str):
        user = self.get_user_by_username(username)
        if isinstance(user,Reader) == False or isinstance(user,Writer) == False:
            if role.lower() == "reader":
                new_reader = Reader(username,password,birth_date)
                self.add_reader(new_reader)
            if role.lower() == "writer":
                new_writer = Writer(username,password,birth_date)
                self.add_writer(new_writer)
            return {"User": "sign up successfully"}
        else : 
            return {"User": "invalid username"}
        
    def create_book(self, name:str, writer_name:str, tag_list: str, status: str, age_restricted: bool, prologue: str):
        writer = self.get_user_by_username(writer_name)
        book = self.get_book_by_name(name)
        if isinstance(writer,Writer) and isinstance(book,Book) == False:
            new_book = Book(name,writer,tag_list,status,age_restricted,prologue)
            writer.add_writing_book_list(new_book)
            return new_book
        else : 
            return {"Book": "please try again"}
    
    def create_chapter(self,book_name,chapter_number, name, context, cost):
        book = self.get_book_by_name(book_name)
        if isinstance(book,Book) and book.is_chapter_valid(chapter_number):
            chapter = Chapter(book_name,chapter_number, name, context, cost)
            book.add_chapter_list(chapter)
            return chapter
        else : 
            return {"Chapter": "please try again"}
        
    def create_comment(self, chapter_id, username, context):
        chapter = self.search_chapter_by_chapter_id(chapter_id)
        user = self.get_user_by_username(username)
        # print(chapter)
        if isinstance(chapter,Chapter):
            new_comment = Comment(chapter,user,context)
            #find book and append in book 
            book = self.search_book_by_chapter(chapter)
            book.add_comment_list(new_comment)
            chapter.add_comment(new_comment)
            return new_comment
        else : 
            return {"Comment": "please try again"}
        
    def edit_book_info(self, name, add_tag_list, delete_tag_list, status, age_restricted, prologue):
        book = self.get_book_by_name(name)
        if name:
            book.name = name
        if add_tag_list:
            book.add_tag(add_tag_list)
        if delete_tag_list:
            book.delete_tag(delete_tag_list)
        if status:
            book.status = status
        if age_restricted != None:
            book.age_restricted = age_restricted
        if prologue:
            book.prologue = prologue
        # book.date_time(0)
        return book
            
    def edit_chapter_info(self,chapter_id, name, context, cost):
        chapter = self.search_chapter_by_chapter_id(chapter_id)
        if name != None:
            chapter.update_name(name)
        if context != None:
            chapter.update_context(context)
        if cost != None:
            chapter.update_cost(cost)
        # chapter.publish_date_time(0)
        return chapter

    # def show_my_page(self, username):
        # writing_count = 0
        # reads = 0
        # writing_list = None
        # pseudonym_list = None
        # comments = None
        # user = self.get_user_by_username(username)
        # if isinstance(user, Writer):
        #     writing_count = len(user.get_writing_list())
        #     reads = user.get_viewer_count()
        #     writing_list = user.get_writing_name_list()
        #     pseudonym_list = user.get_pseudonym_list()
        #     comment_list = user.get_json_comment_list()
        # else:
        #     return "User Not Found"
        # return {"display_name" : user.display_name,
        #         "introduction" : user.introduction,
        #         "writing_count" : writing_count,
        #         "book_on_shelf_count" : len(user.get_book_shelf_list()),
        #         "followers" : len(user.get_follower_list()),
        #         "read_count" : len(user.get_recent_read_chapter_list()),
        #         "viewer_count" : reads,
        #         "writings" : writing_list,
        #         "pseudonyms" : pseudonym_list,
        #         "comments" : comment_list}
    
    # def show_my_profile(self, username):
    #     writing_count = 0
    #     reads = 0
    #     writing_list = None
    #     pseudonym_list = None
    #     comments = None
    #     user = self.get_user_by_username(username)
    #     if isinstance(user, Writer):
    #         writing_count = len(user.writing_list())
    #         reads = user.get_viewer_count()
    #         writing_list = user.writing_name_list()
    #         pseudonym_list = user.pseudonym_list()
    #         comment_list = user.json_comment_list()
    #     else:
    #         return "User Not Found"
    #     return {"display_name" : user.display_name,
    #             "username" : user.username,
    #             "password" : "*" * len(user.password),
    #             "book_on_shelf_count" : len(user.book_shelf_list()),
    #             "followers" : len(user.follower_list()),
    #             "read_count" : len(user.recent_read_chapter_list()),
    #             "viewer_count" : reads,
    #             "writings" : writing_list,
    #             "pseudonyms" : pseudonym_list,
    #             "comments" : comment_list}

    def counting_report(self,book):
        for report_type in self.__report_type_list:
            if book.counting_report_from_type(report_type) in self.__report_type_list:
                #send to web master
                book.status = "hiding"
                return f"your book has been reported 10 times in {report_type}"