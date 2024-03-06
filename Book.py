#Book.py
from datetime import datetime 
from Report import Report
from Comment import Comment
from Chapter import Chapter
# from Controller import Controller

class Book():
    viewer_count = 0
    add_to_shelf_count = 0

    def __init__(self, name, writer, tag_list, status, age_restricted, prologue):
        self.__name = name
        self.__writer = writer
        self.__tag = tag_list
        self.__status = status
        self.__age_restricted = age_restricted
        self.__prologue = prologue
        self.__chapter_list = []
        self.__comment_list = []
        self.__report_list = []
        self.__date_time = datetime.now()
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @property
    def writer(self):
        return self.__writer

    @property
    def tag(self):
        return self.__tag
    
    def add_tag(self,tag_list):
        self.__tag += tag_list

    def delete_tag(self,tag_list):
        new_tag_list = []
        for tag in self.__tag:
            if tag not in tag_list:
                new_tag_list.append(tag)
        self.__tag = new_tag_list

    
    @property
    def age_restricted(self):
        return self.__age_restricted
    @age_restricted.setter
    def age_restricted(self,new_age_restricted):
        self.__age_restricted = new_age_restricted

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,new_status):
        self.__status = new_status

    @property
    def prologue(self):
        return self.__prologue
    @prologue.setter
    def prologue(self,new_prologue):
        self.__prologue = new_prologue

    @property
    def date_time(self):
        return f"{self.__date_time.strftime("%x")} {self.__date_time.strftime("%X")}"
    @date_time.setter
    def date_time(self,now):
        self.__date_time = datetime.now()

    @property
    def chapter_list(self):
        return self.__chapter_list
    def add_chapter_list(self,chapter):
        if isinstance(chapter,Chapter):
            self.__chapter_list.append(chapter)

    @property
    def report_list(self):
        return self.__report_list
    def add_report_list(self,report):
        if isinstance(report,Report):
            self.__report_list.append(report)

    @property
    def comment_list(self):
        return self.__comment_list
    def add_comment_list(self,comment):
        if isinstance(comment,Comment):
            self.__comment_list.append(comment)


    def add_report_list(self, report):
        self.report_list.append(report)
        self.counting_date_time = datetime.now()

    def counting_report_from_type(self,type):
        report_count=0
        for report in self.__report_list:
            if report_count == 10:
                return type
            if report.report_type == type:
                report_count+=1

    def delete_report(self, report):
      if report in self.report_list:
          self.report_list.remove(report)
    
    def is_chapter_valid(self,chapter_number):
        for chapter in self.chapter_list:
            if chapter.chapter_number == chapter_number:
                return False
        return True
