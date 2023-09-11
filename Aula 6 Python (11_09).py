#classe e objeto
# class Casa:
#     None

# casaDom = Casa()
# casaLuis = Casa()



#Métodos
# class Carro:
#     def __init__(self, numPortas):#Método construtor
#         self.ligado = False
#         self.portas = numPortas

#     def ligar(self):
#         if self.ligado == False:
#             self.ligado = True #Declarando um atributo. Altera as "estatísticas"(tipo caractesristicas q sempre vão estar, tipo determinar a vida,
#             print("Ligando...")# se o objeto está ligado naturalmente).
#         else:                  
#             print("Já está ligado.")

#     def desligar(self):
#         if self.ligado == False:#Método construtor
#             print("Já está desligado.")
#         else:
#             print("Desligando...")

# carroDom = Carro()
# carroLuis = Carro()

# carroDom.ligar()
# carroDom.desligar()

# carroLuis.desligar()




# class Carro:
#     def __init__(self, numPortas):#Método construtor
#         self.portas = numPortas
#     def mostrar(self):
#         print(f"Esse carro tem {self.portas} portas.")

# carroDom = Carro(4)
# carroLuis = Carro(2)

# print(carroDom.portas)
# print(carroLuis.portas)

# carroDom.mostrar()



# class Carro:
#     def __init__(self, portas=4):#Método construtor
#         self.portas = portas

#     def mostrar(self):
#         print(f"Esse carro tem {self.portas} portas.")

# carroDom = Carro()
# print(carroDom.portas)

# carroDom.portas = 8
# print(carroDom.portas)


#========== Atividede 1 ==========

# class Casa:
#     def __init__(self, area = 60, rua = "Rua Almirante", nome = "alguem", cor = "Branca"):
#         #self.cor = input("Digite a cor da casa: ")
#         self.cor = cor
#         self.area = area
#         self.rua = rua
#         self.nome = nome
#     def mostrar(self):
#         print(f"A casa do(a) {self.nome} é {self.cor}, tem {self.area} metros2 e está localizada na {self.rua}.")

# casaYas = Casa()
# casaYas.cor = "verde"
# casaYas.mostrar()


# casaDuda = Casa(100, "Rua Torres", "Duda", "Azul")
# casaDuda.mostrar()

#=================================
#ENCAPSULAMENTO

# class Banco:
#     def __init__(self):
#         self.__saldo = 10000#com o anderline eu não consigo alterar fora da classe nem visualizar.
#     def pagar(self, valor):
#         if valor > self.__saldo:
#             print("Dinheiro insuficiente.")
#         else:
#             self.__saldo -= valor
#     def saldo(self):
#         print(self.__saldo)
# conta1 = Banco()
# conta1.saldo()

# conta1.pagar(10000)
# conta1.saldo()

# conta1.pagar(1)

#HERANÇA
# class InstrumentoDeEscrita:
#     def escrever(self):
#         None
#     def desenhar(self):
#         None
# class Lapis:
#     InstrumentoDeEscrita

# class Caneta:
#     InstrumentoDeEscrita

# class Lapiseira:
#     InstrumentoDeEscrita

# class InstrumentoDeEscrita:#classe mãe
#     def __init__(self, material):
#         self._material = material #dois __ privado _ protegido nenhum é público
#     def escrever(self):
#         print("Escrevendo...")
#     def pintar(self):
#         print("Pintando...")
#     def MostrarMaterial(self):
#         print(self._material)


# class Lapis(InstrumentoDeEscrita):#o lapis usa como base a classe mãe
#     def __init__(self, material, grafiteN = 0.7):
#         self.grafite_tam = grafiteN
#         super().__init__(material)# muda o atributo material da classe mãe (InstrumentoDeEscrita)

# lapis1 =Lapis("grafite", 0.7)
# lapis1.MostrarMaterial()


#========== Atividede 2 ==========

# class Calculadora:
#     def __init__(self, valor1, valor2):
#         self.valorA = valor1
#         self.valorB = valor2
#         self.resultado = 0
#     def soma(self):
#         self.resultado = self.valorA + self.valorB
#         print(f"O resultado da soma é {self.resultado}.")

#     def subtracao(self):
#         self.resultado = self.valorA - self.valorB
#         print(f"O resultado da subtração é {self.resultado}.")

#     def multiplicacao(self):
#         self.resultado = self.valorA * self.valorB
#         print(f"O resultado da multiplicação é {self.resultado}.")

#     def multiplicacao(self):
#         if self.valorB == 0:
#             print("Nenhum número pode ser dividido por zero.")
#         else:
#             self.resultado += self.valorA / self.valorB
#             print(f"O resultado da multiplicação é {self.resultado}.")

# class CalculadoraCientifica(Calculadora):
#     def __init__(self, valor1, valor2):    

#         super().__init__(valor1, valor2)
        
#     def RaizQuadrada(self):
#         self.resultado = self.valorA**0.5
#         print(f"O resultado  da raiz do valor A é {self.resultado}.")
#         self.resultado = self.valorB**0.5
#         print(f"O resultado  da raiz do valor B é {self.resultado}.")

#     def Potencia(self):
#         self.resultado = self.valorA ** 2
#         print(f"O resultado da potencia ao quadrado do valor A é {self.resultado}.")
#         self.resultado = self.valorB ** 2
#         print(f"O resultado da potencia ao quadrado do valor B é {self.resultado}.")


# A = CalculadoraCientifica(10, 20)
# A.RaizQuadrada()

#========== Atividede 3 ==========
class Conta:
    def __init__(self):
        self.conta = False
        self.__valor = 0
    def AbrirConta(self):
        if self.conta == False:
            self.conta = True
            print("Conta aberta com sucesso!!")
        else:
            print("Você já possuí uma conta.")
    def FecharConta(self):
        if self.conta == True:
            self.conta = False
            print("Conta fechada com secesso!")
        else:
            print("Você não possuí uma conta.")   

class Corrente(Conta):
    def __init__(self):

class Salario(Conta):
              
class Poupanca(Conta):

      
      