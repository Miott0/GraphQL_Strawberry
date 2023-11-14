import strawberry 
from typing import List
from .type import BookType
from book.models import Book

@strawberry.type
class Query():
    @strawberry.field
    def books(self, author:str = None) -> List[BookType]:
        if author:
            books = Book.objects.filter(author=author)
            return books
        return Book.objects.all()