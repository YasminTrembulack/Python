# class Animal:
#     def __init__(self,nome):
#         self.__nome = nome #privado
    
#     def emitirSom(self):
#         print(f"{self.__nome} está emitindo um som.")

#     def getNome(self) -> str: #exibir  (-> str quer dizer que ele vai retornar um string, não é obrigatório)
#         return self.__nome
    
#     def setNome(self, nome): #mudar
#         self.__nome = nome

# class Cachorro(Animal):
#     def __init__(self, nome, cor):
#         super().__init__(nome)
#         self.__cor = cor
#     def emitirSom(self):
#         print(f"{self.getNome} está latindo.")


# a = Cachorro("Toby", "branco")
# print(a.getNome())
# a.emitirSom()

#========== Atividede 6 ==========
#=================================


class Livro:

    todos = {}

    def __init__(self, titulo:str, total:int, lidas:int):
        self.__titulo = titulo
        self.__totalPag = total
        self.__pagLida = lidas

        Livro.todos.update({titulo : [{"Total:": total, "Lidas: ": lidas}]})


    def sobreLivro(self):
        print(f"O livro {self.__titulo} tem {self.__totalPag} páginas no Total.")

    def setLidas(self, lidas):
        del Livro.todos[self.__titulo]
        self.__pagLida = lidas
        Livro.todos.update({self.__titulo : [{"Total:": self.__totalPag, "Lidas: ": lidas}]})

    def setTotalPag(self, total):
        del Livro.todos[self.__titulo]
        self.__totalPag = total
        Livro.todos.update({self.__titulo : [{"Total:": total, "Lidas: ": self.__pagLida}]})

    def setTitulo(self, titulo):
        del Livro.todos[self.__titulo]
        self.__titulo = titulo
        Livro.todos.update({titulo : [{"Total:": self.__totalPag, "Lidas: ": self.__pagLida}]})

    def verBiblio(self):
        print(f"A Biblioteca possuí os livros: {Livro.todos}")

    def verificarProgresso(self):
        porcentagem = (self.__pagLida * 100) / self.__totalPag
        print(f"O progresso do livro é de {round(porcentagem, 2)}%")


l1 = Livro("A Rainha Vermelha", 350, 100)
l2 = Livro("A Seleção", 100, 30)
l3 = Livro("Jogos Vorazes", 635, 600)

l2.setTitulo("Assim que acaba")
l2.setTotalPag(1000)
l3.setLidas(10)
l2.sobreLivro()
l1.verBiblio()
l1.verificarProgresso()

#=================================



    

    

