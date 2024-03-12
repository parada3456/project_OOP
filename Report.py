from datetime import datetime

class Report:
    def __init__(self, book, user, report_type, context):
        self.__book = book
        self.__user = user
        self.__report_type = report_type
        self.__context = context
        self.__date_time = datetime.now()

    # report_type = ["violence", "harrasment"]
    @property
    def book(self):
        return self.__book
    @property
    def user(self):
        return self.__user
    @property
    def report_type(self):
        return self.__report_type
    @property
    def context(self):
        return self.__context
    @property
    def date_time(self):
        return f"{self.__date_time.strftime("%x")} {self.__date_time.strftime("%X")}"
