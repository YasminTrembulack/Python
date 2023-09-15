#Exercicio 1
#Com a programação orientada a objetos os códico fica mais organizado facilitando a compreneção.
#Evita ficar fazendo várias linhas repetitivas no código já que você pode reutiliza-las de uma melhor forma.

class Aluno:
    def __init__(self):
        self.__nome = input("Digite o nome do aluno: ")
        self.__idade = input("Digite a idade do aluno: ")
        self.__turma = input("Digite a turma do aluno: ")
        self.__planta = input("Digite a planta do aluno: ")
        
        Aluno.aluno = {"Nome": self.__nome, "Idade": self.__idade, "Turma":self.__turma, "Planta ": self.__planta}

    def addAluno(self):
        with open("alunos.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(str(Aluno.aluno))
        arquivo.close()


a =Aluno()
a.addAluno()








#Exercicio 2

class Livro():
    def __init__(self, titulo, autor, qtd_paginas:int, guardado=True):
        self.titulo = titulo
        self.autor = autor
        self.qtdPaginas = qtd_paginas
        self.guardado = guardado
        self.paginaAtual = 0

    def pegarLivro(self):
        if self.guardado == True:
            print("Você pegou o livro.")
            self.guardado = False
        else:
            print("Alguém já pegou o livro.")

    def devolverLivro(self):
        if self.guardado == False:
            print("Você devolveu o livro.")
            self.guardado = True
        else:
            print("Alguém já devolveu o livro.")

    def virarUmaPagina(self):
        if self.guardado == True:
            self.paginaAtual += 1
            if self.paginaAtual >= self.qtdPaginas:
                self.paginaAtual = self.qtdPaginas 
            print(f"Você está na página {self.paginaAtual} de {self.qtdPaginas}")
            
        else:
            print("O livro não está guardado.")

    
    def virarNpaginas(self,n):
        if self.guardado == True:
            self.paginaAtual += n
            if self.paginaAtual > self.qtdPaginas:
                self.paginaAtual = self.qtdPaginas 
            print(f"Você está na página {self.paginaAtual} de {self.qtdPaginas}")
            
        else:
            print("O livro não está guardado.")

    def voltarUmaPagina(self):
        if self.guardado == True:
            self.paginaAtual -= 1
            if self.paginaAtual <= 0:
                self.paginaAtual = 1 
            print(f"Você está na página {self.paginaAtual} de {self.qtdPaginas}")   
        else:
            print("O livro não está guardado.")
    
    def voltarNpaginas(self, n):
        if self.guardado == True:
            self.paginaAtual -= n
            if self.paginaAtual < 0:
                self.paginaAtual = 1
            print(f"Você está na página {self.paginaAtual} de {self.qtdPaginas}")
            
        else:
            print("O livro não está guardado.")
    
    def lerLivro(self):
        print(f"O livro é {self.titulo} de {self.autor}.")



l1 = Livro("A Rainha Vermelha","Victoria Aveyard", 350)

l1.pegarLivro()
l1.pegarLivro()

l1.devolverLivro()
l1.devolverLivro()

l1.virarUmaPagina()
l1.virarUmaPagina()
l1.virarNpaginas(360)
l1.voltarUmaPagina()
l1.voltarNpaginas(400)
l1.lerLivro()






#Exercicio 3

class Conta:
    
    NumeroContas = 0

    def __init__(self, nome, Nagencia, Nconta, saldo, tipo):
        self.__nome = nome
        self.__Nagencia = Nagencia
        self.__Nconta = Nconta
        self.__saldo = saldo
        self.__tipo = tipo
        Conta.NumeroContas += 1

    def Ncontas():
        print(f"O Banco tem {Conta.NumeroContas} contas.")
        
    def getNome(self):
        return self.__nome
    def setNome (self, nome):
        self.__nome = nome

    def getNagencia(self):
        return self.__Nagencia
    def setNagencia (self, Nagencia):
        self.__Nagencia = Nagencia
    
    def getNconta(self):
        return self.__Nconta
    def setNconta (self, Nconta):
        self.__Nconta = Nconta
    
    def getSaldo(self):
        return self.__saldo
    def setSaldo (self, saldo):
        self.__saldo = saldo

    def getTipo(self):
        return self.__tipo
    def setTipo (self, tipo):
        self.__tipo = tipo

      
c1 = Conta("yas", 1241, 143412, 5000, "Corrente")
c2 = Conta("dudu", 2432, 821213, 2000, "Poupança")

Conta.Ncontas()    









#Exercicio 4
class Empresa:
    def __init__(self):
        self.nome = "Bosch"
        self.CNPJ = 114141
        self.Nacionalidade = "BR"
        self.__NomeDoResponsavel = "Presidente"
        self.PaisesDeAtuacao = ["Brasil", "India", "EUA"]
        self.Produtos = {"chaves": ["nome do produto", "preço do produto", "descrição"]}

    def RetornarNomeResponsavel(self):
        return self.__NomeDoResponsavel
    
    def RetornarPaisesDeAtuacao(self):
        return self.PaisesDeAtuacao.copy
    
    def PesquisarPorUmPaisDeAtuacao(self, pais):
        sim = 0
        for p in self.PaisesDeAtuacao:
            if pais == p:
                sim += 1
        if sim >= 1:
            print("O país é um país de atuação.")
        else:
            print("O país não é um  pais de atuação.")
    def AdicionarProduto(self, chaves, nome, preco, descricao):
        self.Produtos.update({chaves: [nome, preco, descricao]})
        
    def RetornarRelatórioProdutos(self):
        print(f"Os produtos são {self.Produtos}.")

    def PesquisarProduto(self, produto):
        sim = 0
        for p in self.Produtos:
            if produto == p:
                sim += 1
            if sim >= 1:
                print(f"O produto foi encontrado: {self.Produtos[produto]}.")
            else:
                print("O país não é um  pais de atuação.")

class Area(Empresa):
    def __init__(self):
        super().__init__()
        self.Nome = "Novo"
        self.SiglaSetor = "AA"
        self.Função = "PT faz ferramentas"
        self.__NomeResponsavelArea = "Diretor"
        self.Lucro = 120000.50
        self.DataInicioAuditoria = ["5","julho","2022"]
        self.DataFimAuditoria = ["12","julho","2023"]
    def RetornarNomeResponsavel(self):
        return self.NomeResponsavelArea
    
    def RetornarRelatorioFinanceiro(self):
        print(f"O lucro foi de R${self.Lucro}.")
    
    def RetornarPeriodoAuditoria(self):
        # saber Data de Início e Fim de Auditoria E se está sendo auditada, ALÉM do responsável pela área)
        print(f"A auditoria começou no dia", " de ".join(self.DataInicioAuditoria), "e foi até o dia", " de ".join(self.DataFimAuditoria),".")
        print(f"O responsavel pela Área é o {self.__NomeResponsavelArea}.")

class Departamento(Area):

    funcionarioNovo = 0

    def __init__(self):
        super().__init__()
        self.Nome = "TESTE"
        self.SiglaSetorDepartamento = "T"
        self.Função = "QMM"
        self.__NomeResponsavelDepartamento = "Gestor"
        self.QuantidadeFuncionarios = 50000
    
    def RetornarNomeResponsavel(self):
        return self.__NomeResponsavelDepartamento
    
    def ContratarFuncionario(self):
        Departamento.funcionarioNovo += 1
        self.QuantidadeFuncionarios += 1
        print(f"O departamento tem {self.QuantidadeFuncionarios} funcionários.")

    def RealizarTreinamento(self):
        print(f"Foi treinado {Departamento.funcionarioNovo} funcionários novos.")


a = Area()
a.PesquisarPorUmPaisDeAtuacao("EUA")
a.AdicionarProduto("aaa", 1233, "teste", "bbbb")
a.RetornarRelatórioProdutos()
a.PesquisarProduto("aaa")
a.RetornarPeriodoAuditoria()








#Exercicio 5
#Classe é utilizada para representar um conjunto de objetos com características semelhantes. Por exemplo um carro e uma moto,
#eles são diferentes mas ambos podem ligar, desligar, ir pra frente, acender o farol assim podemos dizer que eles pertencem a classe automóveis.