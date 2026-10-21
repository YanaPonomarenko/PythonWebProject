from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, title, text, ext, pages):
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Кількість сторінок має бути додатним цілим числом.")
        self.title = title
        self.text = text
        self.ext = ext
        self.pages = pages

    def __str__(self):
        return f"{self.title}{self.ext} ({self.pages} стор.)"

    @abstractmethod
    def get_content(self):
        pass


class ExcellDocument(Document):
    def __init__(self, title, text, pages):
        super().__init__(title, text, ".xlsx", pages)

    def get_content(self):
        return f"Excel:\n{self.text}"


class WordDocument(Document):
    def __init__(self, title, text, pages):
        super().__init__(title, text, ".docx", pages)

    def get_content(self):
        return f"Word:\n{self.text}"


class HtmlDocument(Document):
    def __init__(self, title, text, pages):
        super().__init__(title, text, ".html", pages)

    def get_content(self):
        return f"HTML:\n{self.text}"


class Printer:
    def __init__(self, model):
        self.model = model

    def print_document(self, document):
        if not isinstance(document, Document):
            raise TypeError("Потрібен документ.")
        print(f"[{self.model}] {document}")
        print(document.get_content())
        print()


printer = Printer("Epson L3150")

printer.print_document(ExcellDocument("Склад", "A-01: 42", 2))
printer.print_document(WordDocument("Наказ", "Прийняти на роботу", 1))
printer.print_document(HtmlDocument("Профіль", "<p>Мій профіль</p>", 1))