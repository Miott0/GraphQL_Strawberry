import strawberry 
from book.models import Book
import datetime

@strawberry.django.type(Book)
class BookType: 
    book_id: int
    title: str
    author: str
