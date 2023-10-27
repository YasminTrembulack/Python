# =====  1  =====
import os
import time
class Tamagotchi:
 


    def __init__(self, nome, fome : int = 0, saude : int = 10, idade :int = 0):
        self.__nome :str = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade
        
    def Salvar(self):
        try:
            arquivo = open("saves.txt","a")
            arquivo.write([self.__nome, self.__fome, self.__saude, self.__idade])
            arquivo.close()
        except:
            print("Arquivo não encontrado.")

    @staticmethod
    def Verificar(nome):
        try:
            with open("saves.txt", "r") as file:
                conteudo = file.readlines()
                for linha in conteudo:
                        if nome not in linha :
                            return False
                        else:
                            return True
        except:
            print("Arquivo não encontrado.")


    @staticmethod
    def verificarHumor(getfome, getsaude):
        if getfome >= 6 and getsaude >= 6:
            print("Feliz")
        elif getfome < 6 and getsaude >= 6:
            print("Com fome")
        elif getsaude < 6 and getfome >= 6:
            print("Doente")
        else:
            print("Com fome e doente")

    @staticmethod
    def verificarStatus(getfome, getsaude):
        if getfome == 10 and getsaude == 0:
            print("Falecido")
        else:
            print("Vivo")
        

    @property
    def humor(self):
        return self.__humor

    @property
    def nome(self):
        return self.__nome
    
    @property
    def fome(self):
        return self.__fome
    
    @property
    def saude(self):
        return self.__saude
    
    @property
    def idade(self):
        return self.__idade
    
    @nome.setter
    def nome(self, novo):
        self.__nome = novo

    @fome.setter
    def fome(self, novo:str):
        self.__fome = novo

    @saude.setter
    def saude(self, novo):
        self.__saude = novo

    @idade.setter
    def idade(self, novo):
        self.__idade = novo
    
    @humor.setter
    def humor(self, novo):
        self.__humor = novo

sair = 0

while sair == 0:
    nomeT = input("Digite o nome do seu Tamagotchi: ")
    nomeT = Tamagotchi(nomeT)

    try:
        arquivo = open("saves.txt","r")
        data = arquivo.readlines()
        
        for linha in data: 
            if nomeT.nome in linha :
                print('Encontrado')  
                break
        else:
            pass
        arquivo.close() 
    except:
        print("Arquivo não encontrado.")
        

             
                         
    # while True:
    #     print(f"====Status===\n-- {nomeT.nome}\nFome: {nomeT.fome}\nSaude: {nomeT.saude}\n-----------")
    #     nomeT.verificarStatus(nomeT.fome, nomeT.saude)
    #     op = int(input("\n1 - Renomear \n2 - Alimentar \n3 - Medicar \n4 - Banhar \n5 - Verificar humor \n6 - Verificar idade \n7 - Sair\n>"))
    #     if op == 1:
    #         novoNome = str(input("Digite o novo nome: "))
    #         nomeT.nome = novoNome
    #         print("Nome cadastrado.")
    #         print(nomeT.nome)
    #         time.sleep(5)
    #         os.system('cls')
                                
    #     elif op == 2:
    #         nomeT.fome -= 2
    #         if nomeT.fome > 10:
    #             nomeT.fome = 10
    #         elif nomeT.fome < 0:
    #             nomeT.fome = 0
    #         print(f"{nomeT.nome} alimentado.")
    #     elif op == 3:
    #         nomeT.saude += 2
    #         if nomeT.saude > 10:
    #             nomeT.saude = 10
    #         print(f"{nomeT.nome} medicado.")
    #     elif op == 4:
    #         nomeT.saude += 5
    #         if nomeT.saude > 10:
    #             nomeT.saude = 10
    #         print(f"{nomeT.nome} banhou :).")
    #     elif op == 5:
    #         print("Humor:")
    #         nomeT.verificarHumor(nomeT.fome, nomeT.saude)
    #     elif op == 6:
    #         print(f"Idade: {nomeT.idade} anos.")
    #     elif op == 7: 
    #         sair += 1

    #         break
    #     nomeT.Salvar()
    #     nomeT.fome += 2
    #     nomeT.saude -= 1
    #     nomeT.idade += 1
    #     if nomeT.fome > 10:
    #         nomeT.fome = 10
    #     elif nomeT.fome < 0:
    #         nomeT.fome = 0
    #     if nomeT.saude < 0:
    #         print("Falecido")

                            
                        
    



# op = int(input("1 - Estatus. \n2 - "))

