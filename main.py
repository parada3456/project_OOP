import uvicorn
from typing import Optional
from fastapi import FastAPI

from Chapter import Chapter
# from Promotion import BookPromotion, CoinPromotion
from Book import Book
from Reader import Reader, Writer
from Controller import Controller


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

# #chapter_number, name, context, date_time, cost):
# Chapter1_1 = Chapter("1", "first chapter of shinchan", "this is the first chapter of shinchan", 5)

# book_sale = BookPromotion("01/01/2021", 50, [])
# WriteARead.add_promotion(book_sale)

# free_coin = CoinPromotion("01/01/2021", 40, "chakeawaroi")

# # print(WriteARead.search_book_by_name("Shin"))
# print(pint.check_age_restricted())

#---------------------------------------------------------------------------------------------------------------------
def show_book_info(book):
    str1 = {"name : " : str(book.name),
            "writer_name : " : str(book.writer.username),
            "tag_list : " : str(book.tag),
            "status: " : str(book.status),
            "age_restricted: " : str(book.age_restricted),
            "prologue: " : str(book.prologue),
            # "date_time: " : str(book.date_time)
            }

    return str1

def show_chapter_info(chapter):
    str1 = {"name : " : str(chapter.name),
            "context : " : str(chapter.context),
            "cost : " : str(chapter.cost),
            # "publish_date_time: " : str(chapter.publish_date_time)
            }

    return str1
#--------------------------------------------------------------------------------------------------------------------------

@app.get("/bookname")
def search_book(book_name: str):
    # Assuming WriteARead has a method to search for a book by name
    book = WriteARead.search_book_by_name(book_name)
    if book:
        return {"Book": book.dict()}
    else:
        return {"error": "Book not found"}
    

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

@app.post("/sign in", tags=['sign up/sign in'])
def SignIN(username:str, password:str):
    return WriteARead.sign_in(username, password)

@app.post("/signup", tags=['sign up/sign in'])
def SignUp(username:str, password:str, birth_date: str):
    return WriteARead.sign_up(username, password, birth_date)

@app.post("/Book", tags=['Book'])
def CreateBook(name:str, writer_name:str, tag_list: str, status: str, age_restricted: bool, prologue: str):
    return WriteARead.create_book(name,writer_name,tag_list,status,age_restricted,prologue)

@app.post("/Chapter", tags=['Chapter'])
def CreateChapter(book_name:str, chapter_number:int, name:str, context: str, cost : int):
    return WriteARead.create_chapter(book_name, chapter_number, name, context, cost)

@app.post("/Comment", tags=['Comment'])
def CreateComment(chapter_id:str, username:str, context: str):
    return WriteARead.create_comment(chapter_id,username,context)

@app.put("/EditBook", tags=['Book'])
def EditBookInfo(name: str, add_tag_list: Optional[list] = None, delete_tag_list: Optional[list] = None,\
                status: Optional[str] = None, age_restricted: Optional[bool] = None, prologue: Optional[str] = None):
                
    book =  WriteARead.edit_book_info(name,add_tag_list,delete_tag_list,status,age_restricted,prologue)
    if isinstance(book,Book):
        return {"Book": show_book_info(book)}
    else:
        return {"error": "Book not found"}

@app.put("/Edit Chapter", tags=['Chapter'])
def EditChapterInfo(chapter_id:str, name: Optional[str] = None, context: Optional[str] = None, cost: Optional[int] = None):
    chapter =  WriteARead.edit_chapter_info(name,chapter_id, name, context, cost)
    if isinstance(chapter,Chapter):
        return {"chapter": show_chapter_info(chapter)}
    else:
        return {"error": "Book not found"}

# @app.get("/My Page", tags=['user'])
# def ShowMyPage(username:str):
#      return f"My Page : {WriteARead.show_my_page(username)}"

# @app.get("/My Profile", tags=['user'])
# def ShowMyProfile(username:str):
#      return f"My Profile : {WriteARead.show_my_profile(username)}"

@app.get("/get_coin_transacttion", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
    user = WriteARead.get_user_by_username(username)
    return {"Coin Transaction" : user.show_coin_transaction()}

#----------------------------------test----------------------------------


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

# username = "pinttttt"
# password = "sawasdee"
# username = "Mozaza"
# password = "namchakeawpun"
WriteARead.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))
username = "Jueeen"
password = "whippedcream"
birth_date = 12/11/2004
print("search user: ", WriteARead.search_user_list_by_name(username))
print("get user by name: ", WriteARead.get_user_by_username(username))
print("show coin: ", WriteARead.show_coin(username))
print("sign in: ", WriteARead.sign_in(username, password))
print("sign up : ", WriteARead.sign_up(username, password, birth_date))
print("create book : ", WriteARead.create_book("what did OOP do?","Mozaza",["yaoi"],"publishing","true","once in a blue moon, i died because of OOP"))
print("create chapter : ", WriteARead.create_chapter("what did OOP do?", 1, "prologue not real", "pee kra toey", 3))
print("create comment : ", WriteARead.create_comment("what did OOP do?/1","Mozaza","huhuhuhuuuhuuhuhuh"))
print("edit book: ",show_book_info(WriteARead.edit_book_info("what did OOP do?",["boy love"],None,None,"eieieiei",None)))
# show_book_info(Book1)



# test = ShowMyProfile("Mozaza")
# print(test)