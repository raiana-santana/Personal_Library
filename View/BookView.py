from Model.Book import Book
from Controller.BookController import BookController

class BookView:

    #Adicionar um novo livro, captando os inputs necessários
    def add_new_book(self):
        title = input("Enter the name of the book: ")
        author = input("Enter the name of the author: ")
        year_publication = int(input("Enter the year of publication of the book: ")) 
        genre = input("Enter the genre of the book: ")
        reading_progress = input("Enter your reading progress of the book (Beginning, In Progress, Finished): ")
        BookController().save(title, author, year_publication, genre, reading_progress)
    
    #Percorrendo a nossa lista de livros com um for e mostrando ao usuário
    def show_books(self):
        books = BookController().show_all()
        for book in books:
            print(book)