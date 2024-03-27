# 


from dataclasses import dataclass
from datetime import date, datetime
from typing import List

@dataclass
class Author:
    firstname: str
    lastname: str
    age: int

    def __str__(self) -> str:
        return f"{self.lastname}, {self.firstname}"

@dataclass
class Book:
    author: Author
    title: str
    published: date
    hardcover: bool

    def __eq__(self, other: object) -> bool:
        # TODO: Vergleich nur auf Basis von Attributen Author und title
        pass

class Library:

    def __init__(self) -> None:
        self.books: List[Book] = []

    @property
    def authors(self) -> List[Author]:
        # TODO: Rückgabe aller einzigartigen Instanzen von Author, was macht eine Instanz von Author einzigartig?
        return []

    def add_book(self, book: Book) -> None:
        if isinstance(book, Book):
            self.books.append(book)


if __name__ == '__main__':
    
    # Autoren
    john_doe = Author(
        firstname="John",
        lastname="Doe",
        age=43)

    max_muster = Author("Max", "Muster", 22)
    
    # Buecher    
    boring_book = Book(
        author=john_doe, 
        title="The boring book", 
        published=datetime.strptime('24052011', '%d%m%Y').date(), 
        hardcover=False
        )
    
    awesome_book = Book(john_doe, "The awesome book", datetime.strptime('12052023', '%d%m%Y').date(), True)
    this_book = Book(max_muster, "Musterbook", published=datetime.strptime('12042011', '%d%m%Y').date(), hardcover=False)
    
    # TODO: Muss scheinbar als Buch Instanz angelegt werden 
    that_book = "Max Muster - Großes, spannendes Buch"
    
    # Buecherei
    alexandria = Library()
    alexandria.add_book(boring_book)
    alexandria.add_book(awesome_book)
    alexandria.add_book(this_book)
    alexandria.add_book(that_book)
    
    
    assert len(alexandria.books) == 4, "Buchanzahl stimmt nicht"
    assert len(alexandria.authors) == 2, "Autorenanzahl stimmt nicht"