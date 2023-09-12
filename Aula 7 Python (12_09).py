# class ETS:
#     def __init__(self, *args):
#         if len(args)>3:
#             print("Inserindo alunos")
#         elif len(args)==1:  ou isinstance(args)==1:
#             print("Inserindo turma")
# algo = ETS("Turma nova", 1, 2, 3, 4)






#Implemente um programa no qual o usuário deverá informar o nome e a idade de três pessoas. O programa deverá informar o nome da pessoa que possuir a maior idade.
# Regras que deverão ser seguidas para a implementação do algoritmo:
# •	É obrigatório o uso de classe para representar uma pessoa e a mesma deverá possuir como propriedades (características) um nome e uma idade.
# •	A classe também deverá possuir um método chamado ExibirDados. Esse método deverá exibir o nome e a idade da pessoa em questão.
# •	Ao implementar a classe é obrigatório implementar dois construtores (Sobrecarga), um que não recebe parâmetro algum e outro que irá receber o nome e a idade de uma pessoa.

#========== Atividede 1 ==========

# class Pessoa:
#     def __init__(self, *args):
#         if len(args) == 0:
#             self.nome = "Alguém"
#             self.idade = 18
#         elif len(args) > 2:
#             for i in args:
#                 for j in range(len(args)):

#                     if i.isdigit():
#                         self.nome = args[j]
#                         print(self.nome)
#                         self.idade = args[j+1]
#                         print(self.idade)
#                     else:
#                         None
# a = Pessoa("Yas", 20, "duda", 19, "ju",30, "lucas", 12)

# class Pessoa:
#     def __init__(self, *args):
#         if len(args) == 0:
#             self.nome = "Alguém"
#             self.idade = 18
#         elif len(args) == 2:
#             self.nome = args[0]
#             print(self.nome)
#             self.idade = args[1]
#             print(self.idade)

# qnt = int(input("Quantas pessoas deseja adicionar: "))
# for i in range(qnt):
#     nome = input("Nome: ")  
#     idade = input("Idade: ") 
#     pessoa = Pessoa(nome, idade)
    






#========== Atividede 2 ==========

# class RetanguloQuadrado:
#     def __init__(self, altura, base):
#         self.altura = altura
#         self.base = base
#     def valores(self):
#         print(f"O quadrado/retangulo tem uma altura de {self.altura} m² e comprimento de base de {self.base} m².")
#     def area(self):
#         print(f"A área é de {self.altura * self.base} m².")

# altura = int(input("Digite a altura: "))
# base = int(input("Digite o comprimento da base: "))
# quadrado = RetanguloQuadrado(altura,base)
# quadrado.area()
# quadrado.valores()


#========== Atividede 3 ==========


# class Animal:
#     def __init__(self, nome, tipo, qntg = 0, qntc = 0, qntp = 0):
#         Animal.gato = 0
#         Animal.cachorro = 0
#         Animal.peixe = 0
#         self.__tipo = tipo
#         self.__nome = nome

#         if self.__tipo == "gato":
#             Animal.gato += 1
#         elif self.__tipo == "cachorro":
#             Animal.cachorro += 1
#         else:
#             Animal.peixe += 1
        
        
#     def exibir(self):
#         print(f"O nome do {self.__tipo} é {self.__nome} e tem {Animal.gato} do seu tipo.")

        
# gato1 = Animal("sla", "gato")
# gato3 = Animal("sla", "gato")
# gato4 = Animal("sla", "gato")
# gato2 = Animal("aaaaa", "gato")
# gato4.exibir()

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