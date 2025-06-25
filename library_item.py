#library_item.py
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self.__item_id = item_id
        self.__title = title

    @property
    def item_id(self):
        return self.__item_id

    @property
    def title(self):
        return self.__title

    @abstractmethod
    def display_details(self):
        pass