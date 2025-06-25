class LibraryMember:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_items = []

    @property
    def member_id(self):
        return self.__member_id

    @property
    def name(self):
        return self.__name

    @property
    def borrowed_items(self):
        return self.__borrowed_items

    def borrow_item(self, item):
        self.__borrowed_items.append(item)

    def return_item(self, item):
        if item in self.__borrowed_items:
            self.__borrowed_items.remove(item)

    def __str__(self):
        return f"Member ID: {self.__member_id}, Name: {self.__name}, Borrowed Items: {self.__borrowed_items}"
