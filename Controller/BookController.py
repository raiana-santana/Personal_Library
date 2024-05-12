#Importações

from Model.Book import Book
from DAO.Database import Database

#Criação da classe BookController, onde fazemos adição na lista books com o .append, e retornamos uma cópia dessa lista com o .copy()
class BookController:
    def save(self, book):
        Database.books.append(book)

    def show_all(self):
        return Database.books.copy()