#Criação da classe User
#Recebe os atributos name ->Passível de alterações<-

class User:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"[User] Name: {self.name}"