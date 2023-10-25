class Animal:
     def __init__(self,nome):
         self.__nome = nome #privado
    
     def emitirSom(self):
         print(f"{self.__nome} está emitindo um som.")

     def getNome(self) -> str: #exibir  (-> str quer dizer que ele vai retornar um string, não é obrigatório)
         return self.__nome
    
     def setNome(self, nome): #mudar
         self.__nome = nome

class Cachorro(Animal):
     def __init__(self, nome, cor):
         super().__init__(nome)
         self.__cor = cor
     def emitirSom(self):
         print(f"{self.getNome} está latindo.")


a = Cachorro("Toby", "branco")
print(a.getNome())
a.emitirSom()

#========== Atividede 6 ==========
class Livro:

    todos = {}

    def __init__(self, titulo:str, total:int, lidas:int):
        self.__titulo = titulo
        self.__totalPag = total
        self.__pagLida = lidas

        Livro.todos.update({titulo : [{"Total:": total, "Lidas: ": lidas}]})


    def sobreLivro(self):
        print(f"O livro {self.__titulo} tem {self.__totalPag} páginas no Total.")
    
    def verificarProgresso(self):
        porcentagem = (self.__pagLida * 100) / self.__totalPag
        print(f"O progresso do livro é de {round(porcentagem, 2)}%")

    def setLidas(self, lidas):
        Livro.todos.update({self.__titulo : [{"Total:": self.__totalPag, "Lidas: ": lidas}]})
        self.__pagLida = lidas

    def setTotalPag(self, total):
        Livro.todos.update({self.__titulo : [{"Total:": total, "Lidas: ": self.__pagLida}]})
        self.__totalPag = total

    def setTitulo(self, titulo):
        del Livro.todos[self.__titulo]
        self.__titulo = titulo
        Livro.todos.update({titulo : [{"Total:": self.__totalPag, "Lidas: ": self.__pagLida}]})

    def verBiblio(self):
        print(f"A Biblioteca possuí os livros: {Livro.todos}")

    

l1 = Livro("A Rainha Vermelha", 350, 100)
l2 = Livro("A Seleção", 100, 30)
l3 = Livro("Jogos Vorazes", 635, 600)

l2.setTitulo("Assim que acaba")
l2.setTotalPag(1000)
l3.setLidas(10)
l1.setLidas(300)
l2.sobreLivro()
l1.verBiblio()
l1.verificarProgresso()

#=================================

    
import os
import random
import time

class Pessoa:
    def __init__(self, nome:str, idade:int, genero:str):
        self.__nome = nome 
        self.__idade = idade
        self.__genero = genero

    def getNome(self): 
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade
    def setIdade(self, idade):
        self.__idade = idade

    def getGenero(self):
        return self.__genero
    def setGenero(self, genero):
        self.__genero = genero

class Funcionario(Pessoa):

    

    def __init__(self, nome: str, idade: int, genero: str, cargo:str, salario:int, numfuncionario:int):
        super().__init__(nome, idade, genero)
        self.__cargo = cargo
        self.__salario = salario
        self.__numFuncionario = numfuncionario

    def lista():
        todosfuncionarios = []
        
    def addFuncionario(self):
        Funcionario.todosfuncionarios.append({"Nome: ": self.getNome(), "Idade: ": self.getIdade(), "Gênero: ": self.getGenero(),
                                              "Cargo: ": self.__cargo, "Salário: ": self.__salario, "Número do funcionário: ": self.__numFuncionario})
    
    def getCargo(self): 
        return self.__cargo
    def setCargo(self, cargo):
        self.__cargo = cargo

    def getSalario(self):
        return self.__salario
    def setSalario(self, salario):
        self.__salario = salario

    def getNumFuncionario(self):
        return self.__numFuncionario
    def setNumFuncionario(self, numfuncionario):
        self.__numFuncionario = numfuncionario

    def calcularBonificação(self): #polimorfismo
        print(f"A bonificação do funcionário é de R${round((self.__salario /10),2)}")


class Gerente(Funcionario):
    def __init__(self, nome:str, idade:int, genero:str, cargo:str, salario:int, numfuncionario:int, setor:str):
        super().__init__(nome, idade, genero, cargo, salario, numfuncionario)
        self.__setor = setor

    def addGerente(self):
        Funcionario.todosfuncionarios.append({"Nome: ": self.getNome(), "Idade: ": self.getIdade(), "Gênero: ": self.getGenero(), "Cargo: ": self.getCargo(),
                                              "Salário: ": self.getSalario(), "Número do funcionário: ": self.getNumFuncionario(), "Setor: ": self.__setor})

    def getSetor(self): 
        return self.__setor
    def setSetor(self, setor):
        self.__setor = setor

    def calcularBonificação(self): #polimorfismo
        print(f"A bonificação do gerente é de R${round(((self.getSalario()*15)/100),2)}")

class Departamento:

    listaFuncionarios = []

    def __init__(self, nomeDepartamento:str):
        self.__nomeDepartamento = nomeDepartamento

    def adicionarFuncionario(self, funcionario):
        Departamento.listaFuncionarios.append(funcionario)
            
    def mostrarLista(self):
        print(f"Os funcionários da {self.__nomeDepartamento} são:", ", ".join(Departamento.listaFuncionarios))

    def removerFuncionario(self, funcionario):
        Departamento.listaFuncionarios.remove(funcionario)



class Choices(Gerente, Departamento):
     def __init__(self, nome: str, idade: int, genero: str, cargo: str, salario: int, numfuncionario: int, setor: str, nomeDepartamento:str):
         super().__init__(nome, idade, genero, cargo, salario, numfuncionario, setor, nomeDepartamento)
    

     def registrarFuncionario():
         os.system('cls')
         nome = input("Nome: ")
         idade = int(input("Idade: "))
         genero = input("Genero: ")
         cargo = input("Cargo: ")
         salario = int(input("Sálario: "))
         numfuncionario = random.randint(0, 1000000)
         p = Funcionario(nome, idade, genero, cargo, salario, numfuncionario)
         p.addFuncionario()
         print("Cadastrado com sucesso!!!")
         time.sleep(2)

     def registrarGerente():
         os.system('cls')
         nome = input("Nome: ")
         idade = int(input("Idade: "))
         genero = input("Genero: ")
         cargo = input("Cargo: ")
         salario = int(input("Sálario: "))
         numfuncionario = random.randint(0, 1000000)
         setor = input("Setor: ")
         p = Gerente(nome, idade, genero, cargo, salario, numfuncionario, setor)
         p.addGerente()
         print("Cadastrado com sucesso!!!")
         time.sleep(2)

     sair = 0
     tela = 0
     while sair == 0:
         os.system('cls')# importa a biblioteca "os" e faz esse comando para limpar o terminal 
         if tela == 0:
             print("---------------------------------------------------")
             print("|                                                 |")
             print("|     1 - Registrar Funcionário                   |")
             print("|     2 - Adicionar Funcionaria a departamento    |")
             print("|     2 - Remover Funcionaria a departamento      |")
             print("|     2 - Visualizar departamento                 |")
             print("|                                                 |")
             print("---------------------------------------------------")
             opc = int(input("Digite a aperação desejada: "))    

         match opc:
             case 1:
                 os.system('cls')
                
                 print("---------------------------------------------------")
                 print("|                                                 |")
                 print("|     1 - Funcionário                             |")
                 print("|     2 - Gerente                                 |")
                 print("|     3 - Voltar                                  |")
                 print("|                                                 |")
                 print("---------------------------------------------------")
                 tipo = int(input("> "))   

                 if tipo == 1:
                     registrarFuncionario()
                     print(Funcionario.todosfuncionarios)
                     time.sleep(10)


                 elif tipo == 2: 
                     registrarGerente()
                     print(Funcionario.todosfuncionarios)
                     time.sleep(10)

                 else:
                     tela = 0
                    

print(Funcionario.todosfuncionarios)



funcionario = Gerente("Dudu", 18, "M", "Gerente", 15833, 16723512, "Adiministrativo")
funcionario.calcularBonificação()
funcionario2 = Funcionario("Carla", 20, "F", "Gerente", 2000, 46174189)

d = Departamento("ETS")
d.adicionarFuncionario(funcionario2.getNome())
d.adicionarFuncionario(funcionario.getNome())
d.removerFuncionario(funcionario2.getNome())

d.mostrarLista()
    

