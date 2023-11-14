import strawberry 
from typing import List
from .type import BookType
from book.models import Book

@strawberry.type
class Mutation():

    @strawberry.field
    def create_book(self, title:str, author:str) -> BookType:
        book = Book(title=title,  author=author)
        book.save()
        return book
    

    @strawberry.field
    def update_book(self, book_id:int, title:str, author:str) -> BookType:
        book = Book.objects.get(book_id=book_id)
        book.title = title
        book.author = author
        book.save()
        return book
    
    @strawberry.field
    def delete_book(self, book_id:int) -> bool:
        book = Book.objects.get(book_id=book_id)
        
        try:
            book.delete()
            return True
        except:
            return False