from typing import Union, Optional, Annotated
import uvicorn
from fastapi import FastAPI, Query, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from pydantic import BaseModel
import requests
import json
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from pathlib import Path

from datetime import datetime, timedelta
from Controller import Controller
from Reader import Reader, Writer
from Book import Book
from Chapter import Chapter
from Payment import PaymentMethod, OnlineBanking, TrueMoneyWallet
from CoinTransaction import CoinTransaction
from Promotion import BookPromotion, CoinPromotion, Promotion
from Coin import GoldenCoin, SilverCoin
from Comment import Comment
from Report import Report

app = FastAPI()

templates = Jinja2Templates(directory="Templates")
app.mount("/Templates", StaticFiles(directory="Templates"), name="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")


write_a_read = Controller()

if __name__ == "__main__":
     uvicorn.run("main:app", host="127.0.0.1", port=5500, log_level="info")

now = datetime.now()
app.mount("/Templates", StaticFiles(directory="Templates"), name="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")
# app.mount("/assets", StaticFiles(directory="assets"), name="assets")
#uvicorn main:app --reload

#----------------------------------create users----------------------------------
#WriteARead.add_reader(Reader("username", "password", "dd/mm/yyyy"))
     
Mo = Writer("Mozaza", "12345678", "12/05/2000")
write_a_read.add_reader(Reader("Pinttttt", "sawasdee", "01/01/2005"))
write_a_read.add_reader(Reader("Pangrum", "ehehe", "02/01/2005"))
write_a_read.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))
write_a_read.add_writer(Writer("boss", "00112233", "02/01/2004"))
write_a_read.add_writer(Mo)

#----------------------------------create books----------------------------------
# Book( name, pseudonym, writer, genre, status, age_restricted, prologue)

shin_chan_prologue = "Shin Chan is a 50-year-old boy"
shinosuke_prologue = "Shinosuke is a 50-year-old boy"

book1 = Book("Shin_chan", "Mola", Mo, ["kids", "comedy","crime"], "publishing", False, shin_chan_prologue)
Mo.add_writing_list(book1)
print(book1.pseudonym)

book2 = Book("Shinosuke", "Mola", Mo, ["kids", "comedy","crime"], "publishing", True, shinosuke_prologue)
Mo.add_writing_list(book2)


#----------------------------------create chapters----------------------------------
#Chapter("number", "name", "context", "dd/mm/yyyy", price)
chapter1 = Chapter("Shin_chan", "1", "first_ch", "this is the first chapter of shincha", 184)
chapter2 = Chapter("Shin_chan", "2", "second_ch", "secooooooooooooooond chap", 104)
book1.add_chapter_list(chapter1)
book1.add_chapter_list(chapter2)
chapter3 = Chapter("Shinosuke", "1", "first_Shinosuke", "this is the first chapter of Shinosuke", 22)
chapter4 = Chapter("Shinosuke", "2", "second_Shinosuke", "secooooooooooooooond chap Shinosuke", 1)
book2.add_chapter_list(chapter3)
book2.add_chapter_list(chapter4)
# chapter1.writecreate_comment("Shin_chan-1", Mo, "first comment"))
write_a_read.create_comment("Shin_chan-1", "Mozaza", "first comment")
write_a_read.create_report('Shin_chan','Mozaza','violence','old man kid kids')
write_a_read.create_report('Shin_chan','Mozaza','violence','old man kid kid')
write_a_read.create_report('Shin_chan','Mozaza','violence','old man kid ks')
write_a_read.create_report('Shin_chan','Mozaza','violence','old man kids')
write_a_read.create_report('Shin_chan','Mozaza','violence','old maid kids')
write_a_read.create_report('Shin_chan','Mozaza','violence','old n kid kids')
write_a_read.create_report('Shin_chan','Mozaza','violence','o man kid sdvdsvkids')
write_a_read.create_report('Shin_chan','Mozaza','violence','oldman ksdvdvdewid kids')
# write_a_read.create_report('Shin_chan','Mozaza','violence','oldman sdvsdvvdskid ksdds')


#----------------------------------create promotions----------------------------------
#BookPromotion("dd/mm/yyyy", discount, [book_list])
#CoinPromotion("dd/mm/yyyy", discount, "code")


book_sale = BookPromotion("01/01/2021",50, [])
write_a_read.add_promotion(book_sale)

free_coin = CoinPromotion("01/01/2021",40, "chakeawaroi")
write_a_read.add_promotion(free_coin)

#----------------------------------create transactions----------------------------------

Mo.add_coin_transaction_list(CoinTransaction(OnlineBanking("012-3-45678-9"), 100, 100, 10, now))
Mo.add_coin_transaction_list(CoinTransaction(TrueMoneyWallet("0123456789"), 200, 200, 20, now))

#----------------------------------add coin----------------------------------
Mo.add_silver_coin(20)
Mo.add_silver_coin(10)
Mo.add_silver_coin(50)
Mo.add_silver_coin(3)
Mo.add_silver_coin(100)
Mo.add_golden_coin(888)

#----------------------------------add to bookshelf----------------------------------
Mo.add_book_shelf_list(book1)
Mo.add_book_shelf_list(book2)
# ____________________________________FastAPI___________________________________
# _________________________________________________ GET _________________________________________________

# @app.get("/")
# def FirstPage(req: Request):
#      return templates.TemplateResponse(name="index.html", context={"request":req})

@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
     with open("Templates/index.html") as f:
          html_content = f.read()
     return HTMLResponse(content=html_content, status_code=200)

@app.get("/book/{book_name}")
async def get_book_info(book_name: str, writer_name: str):
     return write_a_read.view_book(book_name, writer_name)
     
print(write_a_read.view_book("Shinosuke","Mozza"))
print("/n")
b=write_a_read.get_book_by_name("Shin_chan")
print("1",b)
print("2",{"name":b.name, "pseudonym":b.pseudonym, "genre":b.genre, "status":b.status, \
            "age_restricted":b.age_restricted, "prologue":b.prologue, "date_time":b.date_time_str,\
            "writer_name":b.writer.username})

# -----------------------------------------------------------------------------------------------
@app.get("/chapter/info/{chapter_id}")
async def get_chapter_info(chapter_id: str):
     chapter =write_a_read.get_chapter_by_chapter_id(chapter_id)
     print("chapterrrrrrrrrrrrrrrrrrrrr_id", chapter_id)
     if isinstance(chapter, Chapter):
          return chapter.show_chapter_info()
     else:
          raise HTTPException(status_code=404, detail="Chapter not found")

# -------------------------------------------------------------------------------------------------------

@app.get("/bookname", tags=['search bar'])
def searchBook(book_name:str):
     return {"Book": write_a_read.search_book_by_name(book_name)}


@app.get("/username", tags=['search bar'])
def SearchUser(username:str):
     return {"user": write_a_read.search_user(username)}

@app.get("/coin", tags=['coin'])
def MyCoin(username:str):
     return write_a_read.show_coin(username)

@app.get("/silver_coin", tags=['coin'])
def ShowSilverCoins(username:str):
     user = write_a_read.get_user_by_username(username)
     return {"Silver_Coin" :user.show_silver_coin_list()}

@app.get("/my_page", tags=['My Page'])
def ShowMyPage(username:str):
     return {"My Page" : write_a_read.show_my_page(username)}

@app.get("/my_profile", tags=['My Profile'])
def ShowMyProfile(username:str):
     return {"My Profile" : write_a_read.show_my_profile(username)}

@app.get("/get_coin_transaction", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
     user = write_a_read.get_user_by_username(username)
     return {"Coin Transaction" : user.show_coin_transaction()}

@app.get("/show_chapter_transaction", tags=['Chapter Transaction'])
def ShowChapterTransaction(username:str):
     user = write_a_read.get_user_by_username(username)
     if write_a_read.if_user_not_found(user): return user
     return {"Chapter Transaction" : user.show_chapter_transaction()}

@app.get("/my_reading", tags=['My Reading'])
def ShowMyReading(username:str):
     return {"My Reading" : write_a_read.show_my_reading(username)}

@app.get("/test", tags=['test'])
def Test(book_name:str):
     return {write_a_read.get_book_by_name(book_name)}

@app.get("/sign_in", tags=['sign up/sign in'])
def SignIN(username:str, password:str):
     return write_a_read.sign_in(username, password)

@app.get("/search_all/{search_str}", tags=['search bar'])
def searchBar(search_str:str):
     return {"Search": write_a_read.search_all_list(search_str)}

@app.get("/writeARead/{search_str}")
def get_all_book(search_str:str):
     return write_a_read.show_all_book_list()

print(write_a_read.show_all_book_list())

# ----------------------------------------------comment list---------------------------------------------------------------
@app.get("/chapter/comment/{chapter_id}", tags=['chapter'])
def show_comment_list(chapter_id:str):
     chapter = write_a_read.get_chapter_by_chapter_id(chapter_id)
     if isinstance(chapter,Chapter):
          return chapter.show_comment_list()
     elif isinstance(chapter,Book):
          return chapter.show_comment_list()
     else:
          return chapter
     
print("-------------------------------------")
chapter236 = write_a_read.get_chapter_by_chapter_id("Shin_chan")
print("show_comment_list",chapter236.show_comment_list() )
print("fi",(write_a_read.get_chapter_by_chapter_id("Shin_chan")).show_comment_list())
# -------------------------------------------------------------------------------------------------------------------
@app.get("/book/chapter/{book_name}", tags=['book'])
def show_chapter_list(book_name:str):
     book = write_a_read.get_book_by_name(book_name)
     if isinstance(book,Book):
          return book.show_chapter_list()
     else:
          return {"message" : "error"}

@app.get('/', response_class=HTMLResponse)
def main(request: Request):
     return templates.TemplateResponse('index.html', {'request': request})

# _________________________________________________ POST _________________________________________________

class dto_sign_up(BaseModel):
     username:str
     password:str
     birth_date: str
     role: str

@app.post("/sign_up", tags=['sign up/sign in'])
def SignUp(dto : dto_sign_up):
     return write_a_read.sign_up(dto.username, dto.password, dto.birth_date, dto.role)

#..........................................................................................................

class dto_add_pseudonym(BaseModel):
     username : str
     new_pseudonym : str


@app.post("/my_profile/psedonym", tags=["My Profile"])
def AddPseudonym(dto : dto_add_pseudonym):
     return {"Add Pseudonym" : write_a_read.add_pseudonym(dto.username, dto.new_pseudonym)}

#..........................................................................................................

class dto_buy_chapter(BaseModel):
     username : str
     chapter_id : str

@app.post("/buy_chapter", tags=['chapter'])
def BuyChapter(dto : dto_buy_chapter):
     return {"Buy Chapter" : write_a_read.buy_chapter(dto.username, dto.chapter_id)}

#..........................................................................................................

class dto_create_book(BaseModel):
     name:str
     writer_name:str
     genre: str
     prologue: str
     age_restricted: bool
     status: str 
     
@app.post("/book/", tags=['Book'])
def CreateBook(dto : dto_create_book):
     return write_a_read.create_book(dto.name, dto.writer_name, dto.genre, dto.status, dto.age_restricted, dto.prologue)

#..........................................................................................................

class dto_create_chapter(BaseModel):
     book_name:str
     chapter_number:int
     name:str
     context: str
     cost : int
     
@app.post("/chapter", tags=['Chapter'])
def CreateChapter(dto : dto_create_chapter):
     return write_a_read.create_chapter(dto.book_name, dto.chapter_number, dto.name, dto.context, dto.cost)

#..........................................................................................................

class dto_create_comment(BaseModel):
     chapter_id : str
     username : str
     context : str
     
@app.post("/comment/{chapter_id}", tags=['Comment'])
def CreateComment(dto: dto_create_comment):
     comment = write_a_read.create_comment(dto.chapter_id, dto.username, dto.context)
     if isinstance(comment,Comment):
          print("yes")
          # "message": "Comment created successfully", 
          return comment.show_comment()
     
     else:
          print("no")
          raise HTTPException(status_code=404, detail="Error creating comment")
     
write_a_read.create_comment("Shin_chan-1", "Mozaza", "55555")
chapter111 = write_a_read.get_chapter_by_chapter_id("Shin_chan-1")
print("commment: ", chapter111.show_comment_list())

#..........................................................................................................
class dto_create_report(BaseModel):
     book_name:str
     username:str
     report_type:str
     context: str
     
@app.post("/report/{book_name}", tags=['report'])
def CreateReport(dto : dto_create_report):
     report = write_a_read.create_report(dto.book_name, dto.username, dto.report_type, dto.context)
     if isinstance(report,Report):
          return {"massage":"report successfully"}
     else :
          return {"massage" : "! Cannot create report !"}

print("------------------------------------------------------------------------------------------report")
report11 = write_a_read.create_report('Shin_chan','Mozaza','violence','old man kid kids')
print(write_a_read.show_all_report("Shin_chan"))
print("report :",report11)
# print(report11.show_report())

@app.get("/report/{book_name}" )
def allReport(book_name:str):
     return write_a_read.show_all_report(book_name)

#..........................................................................................................
class dto_buy_coin(BaseModel):
     username:str
     golden_coin_amount:int
     payment_info: str
     payment_method:str 
     code: Optional[str]
     
@app.post("/buy_coin", tags=['Coin'])
def buy_coin(dto : dto_buy_coin):
     payment = write_a_read.create_payment_method(dto.payment_method, dto.payment_info)
     write_a_read.buy_coin(dto.username, payment, dto.code, dto.golden_coin_amount)  
     return "Purchase successful, THANK YOU"

# _________________________________________________ PUT _________________________________________________

class dto_edit_introduction(BaseModel):
     username : str
     text : str

@app.put("/my_page/edit_introduction", tags=["My Page"])
def EditIntroduction(dto : dto_edit_introduction):
     user = write_a_read.get_user_by_username(dto.username)
     return {"Edit Introduction" : user.edit_introduction(dto.text)}

# #..........................................................................................................

class dto_change_password(BaseModel):
     username : str
     old_password :str
     new_password : str

@app.put("/my_profile/change_password", tags=['My Profile'])
def ChangePassword(dto : dto_change_password):
     return {"Change Password" : write_a_read.change_password(dto.username, dto.old_password, dto.new_password)}

#..........................................................................................................

class dto_change_display_name(BaseModel):
     username : str
     new_display_name : str


@app.put("/my_page/change_display_name", tags=['My Page'])
def ChangeDisplayName(dto : dto_change_display_name):
     return {"Change Display Name" : write_a_read.change_display_name(dto.username, dto.new_display_name)}

#..........................................................................................................

class dto_edit_book(BaseModel):
     old_name : str = None
     writer_name : str = None
     new_name : str = None
     new_genre: str = None
     prologue: str = None
     age_restricted: bool = None
     status: str = None
     
@app.put("/edit_book", tags=['Book'])
def EditBookInfo(dto : dto_edit_book):
     return write_a_read.edit_book_info(dto.old_name, dto.writer_name, dto.new_name, dto.new_genre, dto.status, dto.age_restricted, dto.prologue)

     
#..........................................................................................................

class dto_edit_chapter(BaseModel):
     chapter_number : str = None
     chapter_id : str = None
     name : str = None
     context : str = None
     cost : int = None
     
@app.put("/edit_chapter", tags=['Chapter'])
def EditChapterInfo(dto : dto_edit_chapter):
     print("edit_chapter rr ii")
     chapter =  write_a_read.edit_chapter_info(dto.chapter_id, dto.name, dto.context, dto.cost)
     return chapter
     
print("\n\n")
print("editChapter :",write_a_read.edit_chapter_info("Shin_chan-1", "Mozaza", "too old", '12'))

print("\n")

@app.get("/check_writer/{username}")
def checkWriter(username:str):
     print(write_a_read.check_user_role(username))
     return {"role": write_a_read.check_user_role(username)}

# _________________________________________________ TEST _________________________________________________
# mo_username = "Mozaza"
# mo_password = "namchakeawpun"

book5 = write_a_read.get_book_by_name("Shin_chan")
print({"name":book5.name, "pseudonym":book5.pseudonym, "genre":book5.genre, "status":book5.status, \
            "age_restricted":book5.age_restricted, "prologue":book5.prologue,"date_time":book5.date_time_str,\
            "writer_name":book5.writer.username})

# print("________________________________________________sign in_______________________________________________")
# print(write_a_read.sign_in("Mozaza", "12345678"))

# print("_______________________________________________sign up_______________________________________________")
# print(write_a_read.sign_up("reader1", "12345678", "01/01/2000", "reader"))
# print(write_a_read.sign_up("writer1", "12345678", "01/01/2000", "reader"))

print("_______________________________________________search all_______________________________________________")
print(write_a_read.search_all_list("mo"))

# print("_______________________________________________My Page_______________________________________________")
# print(write_a_read.show_my_page("Mozaza"))

# print("_______________________________________________My Page____________________________________")
# print(write_a_read.show_my_profile("Mozaza"))

# print("_______________________________________________My Reading_______________________________________________")
# print(write_a_read.show_my_reading("Mozaza"))

# print("_______________________________________________Create Book_______________________________________________")
# print(write_a_read.create_book("SAO", "Mola", "Mozaza", "anime", "publishing", True, "Kirito<3Asuna"))

# print("_______________________________________________Edit Book_______________________________________________")
# print("----------Edit everything-----------")
# print(write_a_read.edit_book_info("SAO", "Shinnosuke", "lala", "fantasy", "hiding", False, "edited"))
# print("----------Edit tags-----------")
# print(write_a_read.edit_book_info("Shinnosuke", "Shinnosuke", "lala","romance", "hiding", False, "edited"))

# print("_______________________________________________Creat Chapter_______________________________________________")
# print(write_a_read.create_chapter("Shin_chan", "10", "second", "hihi", 50))

# print("_______________________________________________Edit Chapter_______________________________________________")
# print(write_a_read.edit_chapter_info("Shin_chan-10", "edited_name", "this is edited version", 99))


print("_______________________________________________Add Comment_______________________________________________")
print(write_a_read.create_comment("Shin_chan", "Mozaza", "this is amazing"))

# print("_______________________________________________View Chapter_______________________________________________\n")
# print(write_a_read.view_chapter("Shin_chan-1"))

# print("_______________________________________________View Book_______________________________________________\n")
# print(write_a_read.view_book("Shin_chan"))

# print("_______________________________________________Creat Chapter_______________________________________________")
# print(MyCoin("Mozaza"))

#________________________________________Error________________________________________
# print("_______________________________________________Buy Coin_______________________________________________")
# print(write_a_read.buy_coin("Mozaza", OnlineBanking, "chakeawaroi", 100))



write_a_read.create_report('Shin_chan','Mozaza','violence','old man kid kids')
write_a_read.create_report('Shin_chan','Mozaza','violence','old man kid kid')
write_a_read.create_report('Shin_chan','Mozaza','violence','old man kid ks')
write_a_read.create_report('Shin_chan','Mozaza','violence','old man kids')
write_a_read.create_report('Shin_chan','Mozaza','violence','old maid kids')

write_a_read.create_report('Shin_chan','Mozaza','violence','old n kid kids')
# write_a_read.create_report('Shin_chan','Mozaza','violence','o man kid sdvdsvkids')
# write_a_read.create_report('Shin_chan','Mozaza','violence','oldman ksdvdvdewid kids')
# write_a_read.create_report('Shin_chan','Mozaza','violence','oldman ksdvdvdewidvsdd kids')
print("book_info:",write_a_read.view_book("Shin_chan","Mozaza"))

print("--------------------------------------------------------------------------------------------------------------")
print("book_shelf_list",write_a_read.show_book_shelf("boss"))
write_a_read.add_book_list("boss","Shin_chan")
print("book_shelf_list",write_a_read.show_book_shelf("boss"))

class dto_add_book_shelf(BaseModel):
     username : str
     book_name :str

@app.put("/book_shelf/add")
def AddBookShelf(dto : dto_add_book_shelf):
     return {"book shelf" : write_a_read.add_book_list(dto.username, dto.book_name)}


@app.get("/book_shelf")
def show_book_shelf(username:str):
     return write_a_read.show_book_shelf(username)