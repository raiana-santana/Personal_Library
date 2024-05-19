#Importações

from Model.Book import Book
from DAO.Database import Database

#Criação da classe BookController, onde fazemos adição na lista books com o .append, e retornamos uma cópia dessa lista com o .copy()
class BookController:

    def save(self, title:str, author:list, year_publication:int, genre:str, reading_progress:str):
        book = Book(title, author, year_publication, genre, reading_progress)
        Database.Books.append(book)

    def show_all(self):
        return Database.Books.copy()
    