from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def info(self):
        pass

class Book(Item):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Book: {self.title}, Author: {self.author}")

class Magazine(Item):
    def __init__(self, title, issue):
        self.title = title
        self.issue = issue

    def info(self):
        print(f"Magazine: {self.title}, Issue: {self.issue}")
