class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Reader(Person):
    def __init__(self, name, age, reader_id):
        super().__init__(name, age)
        self.reader_id = reader_id

    def display_info(self):
        print(f"Reader: {self.name}, Age: {self.age}, ID: {self.reader_id}")
