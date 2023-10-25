import random

class Aluno:

    nome: str 
    idade: int 
    matricula: int 
    sala: str 
    __loader__notas: list 

    def __init__(self, nome, idade, matricula, sala, notas):#construtor
        self.nome: str = nome
        self.idade: int = idade
        self.matricula: int = matricula
        self.__sala: str = sala
        self.__notas: list = notas #privado

#################

    @property #get
    def notas(self):
        return self.__notas
    
    @property #get
    def sala(self):
        return self.__sala
    
    @sala.setter #set
    def setsala(self, nova_sala: str):
        if nova_sala.startswith("ct"):
            self.__sala = nova_sala
        else:
            print("Não foi possivel mudar a sala")

    @sala.setter #set
    def setnotas(self, nova_nota: str):
        self.__notas = nova_nota
        


aluno = Aluno("OI", 43, 232, "101", [7, 8, 3])


print("\n",aluno.sala)
aluno.setsala = "222"
print(aluno.sala,"\n")

aluno.setsala = "ct222"
print(aluno.sala,"\n")

print(aluno.notas)
novanota = [ random.randint(0 ,10) for i in range(3)] #FOR COMPRIMIDO
aluno.setnotas = novanota
print(aluno.notas)
#################

