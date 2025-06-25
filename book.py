from library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, item_id, title, author, isbn, year):
        super().__init__(item_id, title)
        self.author = author
        self.isbn = isbn
        self.year = year
        self._is_borrowed = False

    def display_details(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        return f"Book: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Year: {self.year}, Status: {status}"

    def borrow(self):
        self._is_borrowed = True

    def return_item(self):
        self._is_borrowed = False

    @property
    def is_borrowed(self):
        return self._is_borrowed
