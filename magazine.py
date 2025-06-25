from library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number, publisher):
        super().__init__(item_id, title)
        self.issue_number = issue_number
        self.publisher = publisher
        self._is_borrowed = False

    def display_details(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        return f"Magazine: {self.title}, Issue No: {self.issue_number}, Publisher: {self.publisher}, Status: {status}"

    def borrow(self):
        self._is_borrowed = True

    def return_item(self):
        self._is_borrowed = False

    @property
    def is_borrowed(self):
        return self._is_borrowed
