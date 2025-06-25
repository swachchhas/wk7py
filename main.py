from library import Library
from book import Book
from magazine import Magazine
from library_member import LibraryMember

def main():
    library = Library()
    book1 = Book("B1", "1984", "George Orwell", "9780451524935", 1949)
    magazine1 = Magazine("M1", "Time", "March 2025", "Time Inc.")

    library.add_item(book1)
    library.add_item(magazine1)

    member1 = LibraryMember("M101", "Alice")
    library.register_member(member1)

    library.borrow_item("M101", "B1")
    library.borrow_item("M101", "M1")
    library.return_item("M101", "B1")
    library.display_all_items()

if __name__ == "__main__":
    main()
