class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def is_new(self):
        return self.year >= 2020

    def __str__(self):
        return f'Book: {self.title}, Author: {self.author}, Year: {self.year}'

book1 = Book("Книга1", "Автор1", 1835)
book2 = Book("Книга2", "Автор2", 2005)
book3 = Book("Книга3", "Автор3", 2022)

print(book1)
print(book1.is_new())
print(book2)
print(book2.is_new())
print(book3)
print(book3.is_new())

class PositiveNumber:
    def __new__(cls, number):
        if number < 0:
            print("Від'ємне число заборонено")
            return None
        return super().__new__(cls)

    def __init__(self, number):
        self.value = number

    def __str__(self):
        return f'PositiveNumber: {self.value}'


a = PositiveNumber(10)
b = PositiveNumber(-5)

print(a.value)
print(b)