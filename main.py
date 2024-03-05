import uvicorn
from Book import Book
import Chapter
import Payment
import Promotion
from Reader import Reader
from Reader import Writer
import Controller


WriteARead = Controller.Controller()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
    
#create temporary instance
Mo = Writer("Mozaza", "namchakeawpun", "12/05/2000")
WriteARead.add_writer(Mo)
pint = Reader("Pinttttt", "sawasdee", "01/01/2005")
WriteARead.add_reader(pint)
WriteARead.add_reader(Reader("Pangrum", "ehehe", "02/01/2005"))
WriteARead.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))

for writer in WriteARead.writer_list:
    print(writer.username)

# Book (self,name,writer,tag_list,status,age_restricted,prologue,date_time):

shin_chan_prologue = "Shin Chan is a 50-year-old boy"
Book1 = Book("Shin_chan", Mo, ["kids", "comedy","crime"], "publishing", 7, shin_chan_prologue, "01/01/2020")
Book2 = Book("Shinosuke", Mo, ["kids", "comedy","crime"], "publishing", 7, shin_chan_prologue, "01/01/2020")
Mo.add_writing_book_list(Book1)
Mo.add_writing_book_list(Book2)

#chapter_number, name, context, date_time, cost):
Chapter1_1 = Chapter.Chapter("1", "first chapter of shinchan", "this is the first chapter of shinchan", "01/01/2020", 5)

book_sale = Promotion.BookPromotion("01/01/2021", 50, [])
WriteARead.add_promotion(book_sale)

free_coin = Promotion.CoinPromotion("01/01/2021", 40, "chakeawaroi")

# print(WriteARead.search_book_by_name("Shin"))
print(pint.check_age_restricted())

# #--------------------------------------------------------------------------------------------------------------------------

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class BookCreate(BaseModel):
#     name: str
#     # writer: Optional[str] 
#     tag_list: Optional[str] 
#     status: Optional[str] 
#     age_restricted: Optional[bool] 
#     prologue: Optional[str] 
#     date_time: Optional[str] 

# class ReaderCreate(BaseModel):
#     username: str
#     password: Optional[str]
#     birth_date : Optional[str]

@app.get("/bookname")
def search_book(book_name: str):
    # Assuming WriteARead has a method to search for a book by name
    book = WriteARead.search_book_by_name(book_name)
    if book:
        return {"Book": book.dict()}
    else:
        return {"error": "Book not found"}
    
from typing import List

# print(WriteARead.search_writer_by_username("Mozaza"))
# @app.post("/create_book")
# async def create_book(book_data: BookCreate, writer_name: str):
#     # Search for writer by username
#     writer = WriteARead.search_writer_by_username(writer_name)
#     if writer:
#         # Create new book object
#         new_book = Book.Book(
#             name=book_data.name,
#             writer=writer,
#             tag_list=book_data.tag_list,
#             status=book_data.status,
#             age_restricted=book_data.age_restricted,
#             prologue=book_data.prologue,
#             date_time=book_data.date_time
#         )
#         writer.add_writing_book_list(new_book)
#         print("success")
#         return {"message": "New book added successfully"}
#     else:
#         print("error")
#         return {"error": "Writer not found"} 
    
# @app.get("/signup")
# def SignUp(username:str, password:str, birth_date: str):
#     return {"User": WriteARead.create_new_user(username,password,birth_date)}

# @app.post("/Create book")
# def CreateBook(name:str,writer_username:str,tag_list:list,status:str,age_restricted:bool,prologue:str,date_time:str):
#     writer= WriteARead.search_writer_by_username(writer_username)
#     if isinstance(writer,Reader.Writer):
#         new_book=writer.create_new_book(name,writer,tag_list,status,age_restricted,prologue,date_time)
#     if isinstance(new_book,Book.Book)==True:
#         return {"Book": "create book success"}
#     else : 
#         return {"Book": "please try again"}

@app.get("/")
def FirstPage():
     return "Welcome to WriteARead"

@app.get("/bookname", tags=['search bar'])
def searchBook(book_name:str):
    return {"Book": WriteARead.search_book_by_name(book_name)}

@app.get("/username", tags=['search bar'])
def SearchUser(username:str):
     return {"user": WriteARead.search_user(username)}

@app.get("/coin", tags=['coin'])
def ShowCoins(username:str):
     return WriteARead.show_coin(username)

@app.post("/signup", tags=['sign up/sign in'])
def SignUp(username:str, password:str, birth_date: str):
    return WriteARead.sign_up(username, password, birth_date)

@app.post("/Book", tags=['Book'])
def CreateBook(name:str, writer_name:str, tag_list: str, status: str, age_restricted: bool, prologue: str):
    return WriteARead.create_book(name,writer_name,tag_list,status,age_restricted,prologue)

@app.get("/My Page", tags=['user'])
def ShowMyPage(username:str):
     return f"My Page : {WriteARead.show_my_page(username)}"

@app.get("/My Profile", tags=['user'])
def ShowMyProfile(username:str):
     return f"My Profile : {WriteARead.show_my_profile(username)}"

@app.get("/get_coin_transacttion", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
    user = WriteARead.get_user_by_username(username)
    return {"Coin Transaction" : user.show_coin_transaction()}

#----------------------------------test----------------------------------

test = ShowMyProfile("Mozaza")
print(test)