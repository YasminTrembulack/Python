class ETS:
    def __init__(self, *args):
        if len(args)>3:
            print("Inserindo alunos")
        elif len(args)==1:  #ou isinstance(args)==1:
            print("Inserindo turma")
algo = ETS("Turma nova", 1, 2, 3, 4)





# #========== Atividede 1 ==========



class Pessoa:
    def __init__(self, *args):
        if len(args) == 0:
            self.nome = "Alguém"
            self.idade = 18
        elif len(args) > 2:
            for i in args:
                for j in range(len(args)):

                    if i.isdigit():
                        self.nome = args[j]
                        print(self.nome)
                        self.idade = args[j+1]
                        print(self.idade)
                    else:
                        None
a = Pessoa("Yas", 20, "duda", 19, "ju",30, "lucas", 12)

class Pessoa:
    def __init__(self, *args):
        if len(args) == 0:
            self.nome = "Alguém"
            self.idade = 18
        elif len(args) == 2:
            self.nome = args[0]
            print(self.nome)
            self.idade = args[1]
            print(self.idade)

qnt = int(input("Quantas pessoas deseja adicionar: "))
for i in range(qnt):
    nome = input("Nome: ")  
    idade = input("Idade: ") 
    pessoa = Pessoa(nome, idade)
    


#========== Atividede 2 ==========



class RetanguloQuadrado:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def valores(self):
        print(f"O quadrado/retangulo tem uma altura de {self.altura} m² e comprimento de base de {self.base} m².")
    def area(self):
        print(f"A área é de {self.altura * self.base} m².")

altura = int(input("Digite a altura: "))
base = int(input("Digite o comprimento da base: "))
quadrado = RetanguloQuadrado(altura,base)
quadrado.area()
quadrado.valores()


#========== Atividede 3 ==========


class Animal:
    def __init__(self, nome, tipo):
        Animal.gato = []
        Animal.cachorro = []
        Animal.peixe = []
        self.__tipo = tipo
        self.__nome = nome
        
    def exibir(self):
        print(f"O nome do {self.__tipo} é {self.__nome} e tem {len(Animal.gato)} do seu tipo.")
        print(Animal.gato)
    def cat(self):
        if self.__tipo == "gato":
            Animal.gato.append(self.__nome)
    def dog(self):
        if self.__tipo == "cachorro":
            Animal.cachorro.append(self.__nome)
    def fish(self):
        if self.__tipo == "peixe":
            Animal.peixe.append(self.__nome)


        
gato1 = Animal("sla", "gato")
gato1.cat()

gato2 = Animal("aaaa", "gato")
gato2.cat()
gato3 = Animal("bbb", "gato")
gato3.cat()

gato4 = Animal("ccccc", "gato")
gato4.cat()
gato4.exibir()
print(gato4.gato)



#=================================



#   ->    CORRETO



class Animal:
    def __init__(self, nome, tipo):
        self.__nome = nome

        if tipo == "cachorro":
            Animal.cachorro.append(nome)
            self.__tipo = tipo
        elif tipo == "gato":
            Animal.gato.append(nome)
            self.__tipo = tipo
        else:
            Animal.peixe.append(nome)
            self.__tipo = "peixe"

    @staticmethod
    def contabilizar(): #metodo estático
        Animal.peixe = []
        Animal.cachorro = []
        Animal.gato = []

    @staticmethod
    def mostrar(): #metodo estático
        print(f"Peixes: {len(Animal.peixe)} = {Animal.peixe}")
        print(f"Cachorros: {len(Animal.cachorro)} = {Animal.cachorro}")
        print(f"Gatos: {len(Animal.gato)} = {Animal.gato}")

Animal.contabilizar()
#inicia o atributo estatico para setar os valores inicias de cada tipo de animal
a1 = Animal("Garfield", "gato")
a2 = Animal("Marlin", "peixe")
a3 = Animal("Cezar", "macaco")
a4 = Animal("Tobby", "cachorro")
#depois ele define os objetos verifica qual o tipo no __init__ e adiciona +1 nos atributos já definidos anteriormente.
a1.mostrar()
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA



#=================================



class Animal:
    def __init__(self, nome, tipo):
        self.__tipo = tipo
        self.__nome = nome   
        
    def exibir(self):
        print(f"O nome do {self.__tipo} é {self.__nome} e tem {len(Animal.gato)} do seu tipo.")
        print(Animal.gato)
    def inf(self):
        return self.__tipo

    def dog(self):
        if self.__tipo == "cachorro":
            Animal.cachorro.append(self.__nome)
    def fish(self):
        if self.__tipo == "peixe":
            Animal.peixe.append(self.__nome)

class Tipos(Animal):
    def __init__(self, nome, tipo):
        super().__init__(nome, tipo)
        self.gato = []
        self.cachorro = []
        self.peixe = []

    def cadastrar(self):
        if  self.inf == "gato":
            self.gato.append(self.inf)
        
    def mostrar(self):
        print(self.gato)


gato1 = Tipos("sla", "gato")
gato1.cadastrar()

gato2 = Tipos("aaaa", "gato")
gato2.cadastrar()

gato3 = Tipos("bbb", "gato")
gato3.cadastrar()

gato4 = Tipos("ccccc", "gato")
gato4.cadastrar()

gato4.mostrar()




#========== Atividede 4 ==========




import random

class Jogador :
    def __init__(self, id: int, nome:str, apelido: str):
        self.id = id
        self.nome = nome
        self.apelido = apelido

class Plantel:
    def __init__(self):
        self.lista = []

    def cadastrarJogadores(self, jogador):
        self.lista.append(jogador)
    def mostrar(self):
        for i in range(len(self.lista)):
            print(f"Nome: {self.lista[i].nome}" +
                  f" e Apelido: {self.lista[i].apelido}")


nome = input("Digite o nome: ")        
apelido = input("Digite o apelido: ")
j1 = Jogador(random.randint(0,1000), nome, apelido )

p1 = Plantel()
p1.cadastrarJogadores(j1)
p1.mostrar()
