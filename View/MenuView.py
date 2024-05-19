from View.BookView import BookView
#Esse import os é para deixar o terminal mais organizado
import os

class MenuView:

    def start(self):
        print("### Welcome to the Personal Library Sytem ###")
        self.show_menu()

    def show_options(self):
        print("1 - Add a new book")
        print("2 - Show all books in my personal library")
        print("3 - Update information about one book")
        print("4 - Remove a book from my personal library")
        print("0 - Exit")

    #Esse método é para que o menu não apareça imediatamente para o usuário
    def pause(self):
        input("Press any key to see the menu again: ")
        os.system('cls')

    #Menuzinho while True
    def show_menu(self):
        while True:
            self.show_options()
            option = input()

            if option == "0":
                print("Leaving the System...")
                break
            elif option == "1":
                BookView().add_new_book()
                print("Book successfully registered.")
                self.pause()
            elif option == "2":
                BookView().show_books()
                self.pause()
            