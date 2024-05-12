#Criação da classe Book
#Recebe os atributos title, author, year_publication, genre, reading_progress

class Book:
    def __init__(self, title:str, author:list, year_publication:int, genre:str, reading_progress:str):
        self.title = title
        self.author = author
        self.year = year_publication
        self.genre = genre
        self.progress = reading_progress

    def __repr__(self) -> str:
        return f'''[Book]
        Title: {self.title}
        Author: {self.author}
        Year of Publication: {self.year}
        Book Genre: {self.genre}
        My reading progress: {self.progress}'''