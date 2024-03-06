from datetime import datetime
class Chapter:
    __chapter_id = 1

    def __init__(self,book_name, chapter_number, name, context, cost):
        self.__chapter_id = str(book_name) + "/" + str(chapter_number)
        self.__chapter_number = chapter_number
        self.__name = name
        self.__context = context
        self.__publish_date_time = datetime.now()
        self.__viewer_count = 0
        self.__comment_list = []
        self.__cost = cost

    @property
    def chapter_id(self):
        return self.__chapter_id
    @property
    def cost(self):
        return self.__cost
    @property
    def name(self):
        return self.__name
    @property
    def context(self):
        return self.__context
    
    @property
    def chapter_number(self):
        return self.__chapter_number

    @property
    def publish_date_time(self):
        return f"{self.__publish_date_time.strftime("%x")} {self.__publish_date_time.strftime("%X")}"
    
    @publish_date_time.setter
    def publish_date_time(self,now):
        self.__publish_date_time = datetime.now()

    def add_comment(self, comment):
        self.__comment_list.append(comment)

    def add_viewer_count(self):
        self.__viewer_count += 1

    def update_cost(self, new_cost):
        self.__cost = new_cost

    def update_name(self, new_name):
        self.__name = new_name

    def update_context(self, context):
        self.__context = context