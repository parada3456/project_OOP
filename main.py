import uvicorn
from typing import Optional,Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel

from Chapter import Chapter
from Promotion import BookPromotion, CoinPromotion
from CoinTransaction import CoinTransaction
from ChapterTransaction import ChapterTransaction
from Book import Book
from Reader import Reader, Writer
from Controller import Controller
from Payment import OnlineBanking, TrueMoneyWallet, DebitCard
from datetime import datetime 


app = FastAPI()
WriteARead = Controller()


#create temporary instance
Mo = Writer("Mozaza", "namchakeawpun", "12/05/2000")
WriteARead.add_writer(Mo)
pint = Reader("Pinttttt", "sawasdee", "01/01/2005")
WriteARead.add_reader(pint)
WriteARead.add_reader(Reader("Pangrum", "ehehe", "02/01/2005"))
# WriteARead.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))

# for writer in WriteARead.writer_list:
#     print(writer.username)

# Book (self,name,writer,tag_list,status,age_restricted,prologue,date_time):

shin_chan_prologue = "Shin Chan is a 50-year-old boy"
Book1 = Book("Shin_chan", Mo, ["kids", "comedy","crime"], "publishing", True, shin_chan_prologue,)
Book2 = Book("Shinosuke", Mo, ["kids", "comedy","crime"], "publishing", False, shin_chan_prologue,)
Mo.add_writing_book_list(Book1)
Mo.add_writing_book_list(Book2)

#chapter_number, name, context, date_time, cost):
Chapter1_1 = Chapter("1", "first chapter of shinchan", "this is the first chapter of shinchan", "01/01/2020", 5)

book_sale = BookPromotion("01/01/2021", 50, [])
WriteARead.add_promotion(book_sale)

promotion_12_12 = CoinPromotion("01/01/2021", 40, "December")
promotion_11_11 = CoinPromotion("01/01/2021", 20, "November")
WriteARead.add_promotion(promotion_12_12)
WriteARead.add_promotion(promotion_11_11)


#----------------------------------create chapters----------------------------------
#Chapter("number", "name", "context", "dd/mm/yyyy", price)

Book1.add_chapter_list(Chapter( "Shin_chan","1","first_ch", "this is the first chapter of shincha", 184))

#----------------------------------create promotions----------------------------------
#BookPromotion("dd/mm/yyyy", discount, [book_list])
#CoinPromotion("dd/mm/yyyy", discount, "code")


book_sale = BookPromotion("01/01/2021",50, [])
WriteARead.add_promotion(book_sale)

free_coin = CoinPromotion("01/01/2021",40, "chakeawaroi")
WriteARead.add_promotion(free_coin)

#----------------------------------create transactions----------------------------------

# Mo.add_coin_transaction_list(CoinTransaction(OnlineBanking("012-3-45678-9"), 100, 100, 10, now))
# Mo.add_coin_transaction_list(CoinTransaction(TrueMoneyWallet("0123456789", "5174"), 200, 200, 20, now))

#----------------------------------add coin----------------------------------
Mo.add_silver_coin(20)
Mo.add_silver_coin(10)
Mo.add_silver_coin(50)
Mo.add_silver_coin(3)
Mo.add_silver_coin(100)
Mo.add_golden_coin(888)

#----------------------------------add to bookshelf----------------------------------
Mo.add_book_shelf_list(Book1)
Mo.add_book_shelf_list(Book2)

#---------------------------------------------------------------------------------------------------------------------
def show_book_info(book):
    str1 = {"name" : str(book.name),
            "writer_name" : str(book.writer.username),
            "tag_list" : str(book.tag),
            "status" : str(book.status),
            "age_restricted" : book.age_restricted,
            "prologue" : str(book.prologue),
            "date_time" : str(book.date_time)
            }

    return str1

def show_chapter_info(chapter):
    str1 = {"name" : str(chapter.name),
            "context" : str(chapter.context),
            "cost" : str(chapter.cost),
            "publish_date_time" : str(chapter.publish_date_time)
            }

    return str1

def show_comment_info(comment):
    str1 = {"user" : str(comment.commentator.username),
            "chapter" : str(comment.chapter.chapter_id),
            "context" : str(comment.context),
            "date_time" : str(comment.date_time)
            }

    return str1
#--------------------------------------------------------------------------------------------------------------------------
class dto_sign_up(BaseModel):
    username:str
    password:str
    birth_date: str
    role: str

class dto_create_book(BaseModel):
    name:str
    writer_name:str
    tag_list: str
    prologue: str
    age_restricted: bool
    status: str 

class dto_create_chapter(BaseModel):
    book_name:str
    chapter_number:int
    name:str
    context: str
    cost : int

class dto_create_comment(BaseModel):
    chapter_id:str
    username:str
    context: str
#--------------------------------------------------------------------------------------------------------------------------

@app.get("/")
def FirstPage():
     return "Welcome to WriteARead"

@app.get("/bookname or username", tags=['search bar'])
def searchBar(search_str:str):
    return {"Search": WriteARead.search_book_and_user_list(search_str)}

@app.get("/bookname", tags=['search bar'])
def SearchBook(search_str:str):
    return {"Search Book": show_book_info(WriteARead.get_book_by_name(search_str))}

# @app.get("/username", tags=['search bar'])
# def SearchUser(username:str):
#      return {"user": WriteARead.search_user_list_by_name(username)}

@app.get("/coin", tags=['coin'])
def ShowCoins(username:str):
     return WriteARead.show_coin(username)

@app.get("/sign_in", tags=['sign up/sign in'])
def SignIN(username:str, password:str):
    return WriteARead.sign_in(username, password)

@app.post("/sign_up", tags=['sign up/sign in'])
def SignUp(dto : dto_sign_up):
    return WriteARead.sign_up(dto.username, dto.password, dto.birth_date, dto.role)

@app.post("/book", tags=['Book'])
def CreateBook(dto : dto_create_book):
    return WriteARead.create_book(dto.name, dto.writer_name, dto.tag_list, dto.status, dto.age_restricted, dto.prologue)

@app.post("/chapter", tags=['Chapter'])
def CreateChapter(dto : dto_create_chapter):
    return WriteARead.create_chapter(dto.book_name, dto.chapter_number, dto.name, dto.context, dto.cost)

@app.post("/comment", tags=['Comment'])
def CreateComment(dto: dto_create_comment):
    return WriteARead.create_comment(dto.chapter_id, dto.username, dto.context)

# @app.put("/edit_book", tags=['Book'])
# def EditBookInfo(name: str, add_tag_list: Optional[list] = None, delete_tag_list: Optional[list] = None, \
#                  prologue: Optional[str] = None,status: Optional[str] = None, age_restricted: Optional[bool] = Query(False, enum=[False, True])):
#     book =  WriteARead.edit_book_info(name,add_tag_list,delete_tag_list,status,age_restricted,prologue)
#     if isinstance(book,Book):
#         return book
#     else:
#         return {"error": "Book not found"}

# @app.put("/edit_chapter", tags=['Chapter'])
# def EditChapterInfo(chapter_id:str, name: Optional[str] = None, context: Optional[str] = None, cost: Optional[int] = None):
#     chapter =  WriteARead.edit_chapter_info(chapter_id, name, context, cost)
#     if isinstance(chapter,Chapter):
#         return chapter
#     else:
#         return {"error": "Book not found"}

@app.get("/my_page", tags=['user'])
def ShowMyPage(username:str):
     return f"My Page : {WriteARead.show_my_page(username)}"

@app.get("/my_profile", tags=['user'])
def ShowMyProfile(username:str):
     return f"My Profile : {WriteARead.show_my_profile(username)}"

@app.get("/get_coin_transaction", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
    user = WriteARead.get_user_by_username(username)
    return {"Coin Transaction" : user.show_coin_transaction}

@app.get("/get_my_coin", tags=['My Coin'])
def get_my_coin(username:str):
    user = WriteARead.get_user_by_username(username)
    return {"Golden Coin balance" : user.golden_coin.balance, "Silver Coin balance" : user.silver_coin_balance}

@app.post("/post_payment_method", tags=['Buy Coin'])
def buy_coin(username:str, golden_coin_amount:int, payment_info: Annotated[str | None, Query(max_length = 10)],\
        payment_method:str = Query("Payment Method", enum = WriteARead.payment_list, description ='Choose your payment method'),code: Optional[str] = None):
    payment = WriteARead.create_payment_method(payment_method, payment_info)
    WriteARead.buy_coin(username, payment, code, golden_coin_amount)  
    return "Purchase successful, THANK YOU"

@app.get("/show_chapter_transaction", tags=['Chapter Transaction'])
def ShowChapterTransaction(username:str):
        user = WriteARead.get_user_by_username(username)
        if WriteARead.is_user_not_found(user): return user
        return {"Chapter Transaction" : user.show_chapter_transaction()}

# @app.put("/my_profile/change_password", tags=['user'])
# def ChangePassword(username:str,old_password:str, new_password:str):
#         return {"Change Password" : WriteARead.change_password(username, old_password, new_password)}

@app.post("/my_profile/psedonym", tags=["user"])
def AddPseudonym(username:str, new_pseudonym:str):
        return {"Add Pseudonym" : WriteARead.add_pseudonym(username, new_pseudonym)}

@app.get("/my_reading", tags=['user'])
def ShowMyReading(username:str):
        return {"My Reading" : WriteARead.show_my_reading(username)}

@app.post("/buy_chapter", tags=['chapter'])
def BuyChapter(username:str, chapter_id:str):
        return {"Buy Chapter" : WriteARead.buy_chapter(username, chapter_id)}


#----------------------------------test----------------------------------

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

# username = "pinttttt"
# password = "sawasdee"
# username = "Mozaza"
# password = "namchakeawpun"
    
print("------------------------------------------------------------------------------------------------------------------------------------")
WriteARead.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))
username = "Jueeen"
password = "whippedcream"
birth_date = 12/11/2004
print("search : ", WriteARead.search_book_and_user_list(username))
print("get user by name: ", WriteARead.get_user_by_username(username))
print("show coin: ", WriteARead.show_coin(username))
print("------------------------------------------------------------------------------------------------------------------------------------")
print("sign in: ", WriteARead.sign_in(username, password))
print("sign up : ", WriteARead.sign_up(username, password, birth_date,"reader"))
print("------------------------------------------------------------------------------------------------------------------------------------")
print("create book : ", show_book_info(WriteARead.create_book("what did OOP do?","Mozaza",["yaoi"],"publishing",True,"once in a blue moon, i died because of OOP")))
print("create chapter : ", show_chapter_info(WriteARead.create_chapter("what did OOP do?", 1, "prologue not real", "pee kra toey", 3)))
print("create comment : ", show_comment_info(WriteARead.create_comment("what did OOP do?/1","Mozaza","huhuhuhuuuhuuhuhuh")))
print("------------------------------------------------------------------------------------------------------------------------------------")
print("before edit book : ",show_book_info(WriteARead.get_book_by_name("what did OOP do?")))
print("edit book: ",show_book_info(WriteARead.edit_book_info("what did OOP do?",["boy love"],["yaoi"],None,False,None)))
print("------------------------------------------------------------------------------------------------------------------------------------")
print("before edit chapter : ",show_chapter_info(WriteARead.search_chapter_by_chapter_id("what did OOP do?/1")))
print("edit chapter: ",show_chapter_info(WriteARead.edit_chapter_info("what did OOP do?/1","edittttttttttt chapter",None,123)))
print("------------------------------------------------------------------------------------------------------------------------------------")
print("show my profile : ", WriteARead.show_my_profile("Mozaza"))
print("show my page", WriteARead.show_my_page("Mozaza"))
print("------------------------------------------------------------------------------------------------------------------------------------")
print("buy chapter", WriteARead.buy_chapter("Mozaza", "what did OOP do?/1"))
print("buy chapter", WriteARead.buy_chapter("Mozaza", "Shin_chan/1"))
print("------------------------------------------------------------------------------------------------------------------------------------")

# test = ShowMyProfile("Mozaza")
# print(test)