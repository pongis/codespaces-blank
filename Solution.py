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
        # Vergleich nur auf Basis von Attributen Author und title
        if isinstance(other, Book):
            return self.author == other.author and self.title == other.title
        return False 
    
    @classmethod
    def from_string(cls, author: Author, bookinfo: str):
        splitted = bookinfo.split(";")
        _hardcover = True if splitted[2] == "True" else False
        return cls(
            author,
            title=splitted[0],
            published=datetime.strptime(splitted[1], '%d%m%Y').date(),
            hardcover=_hardcover
        )

class Library:

    def __init__(self) -> None:
        self.books: List[Book] = []

    @property
    def authors(self) -> List[Author]:
        # Rückgabe aller einzigartigen Instanzen von Author
        unique_authors = []
        for book in self.books:
            author = book.author
            if author in unique_authors:
                continue
            unique_authors.append(book.author)
        return unique_authors

    def add_book(self, book: Book) -> None:
        if isinstance(book, Book):
            self.books.append(book)

    def __str__(self) -> str:
        return '\n'.join([str(book) for book in self.books])

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
    that_book = Book.from_string(max_muster, bookinfo="Großes, spannendes Buch;12042021;False")
    
    alexandria = Library()
    alexandria.add_book(boring_book)
    alexandria.add_book(awesome_book)
    alexandria.add_book(this_book)
    alexandria.add_book(that_book)
    
    assert len(alexandria.books) == 4, "Buchanzahl stimmt nicht"
    assert len(alexandria.authors) == 2, "Autorenanzahl stimmt nicht"
    print(alexandria)
