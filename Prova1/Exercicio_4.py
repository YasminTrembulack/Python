# 4. Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada
# pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu
# programa deve ter as seguintes funções:

# incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais
# telefones. Ela deve receber como argumentos o nome e os telefones.

# incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda. 
# Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-lo. 
# Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome.

# excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. 
# Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.

# excluirNome – essa função exclui uma pessoa da agenda.
# consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.

agenda_telefonica = {}

def IncluirNovoNome(nome, telefones):
    agenda_telefonica[nome] =telefones

def IncluirTelefone(nome, telefone):
    agenda_telefonica[nome] =telefone

def ExcluirTelefone(telefone):
    pass



while True:
    op = int(input('''Selecione uma opção: \n1 - Incluir novo nome. \n2 - Incluir Telefone. 
3 - Excluir telefone. \n4 - Excluir nome. \n5 - Sair.\n>'''))

    if op == 1:
        telefones = []
        nome = input("Nome: ")
        qnt = int(input("Quantos telefones deseja adicionar: "))

        for i in range(qnt):
            telefone = input("Digite o número: ")
            telefones.append(telefone)
    
        IncluirNovoNome(nome, telefones)

    elif op == 2:
        telefones = []
        nome = input("Nome: ")
        if nome not in agenda_telefonica:

            Nencontrado = input("Nome não encontardo, deseja adicionar como um novo? ")

            if Nencontrado == "sim":

                qnt = int(input("Quantos telefones deseja adicionar: "))

                for i in range(qnt):
                    telefone = input("Digite o número: ")
                    telefones.append(telefone)
        
                IncluirNovoNome(nome, telefones)
                print("Nome:", nome,"Telefones:",agenda_telefonica[nome])
        else:    
            telefonesCadas = agenda_telefonica[nome]
            print(f"Telefones: {agenda_telefonica[nome]}")

            telefone = input("Digite o número: ")
            telefonesCadas.append(telefone)

            IncluirTelefone(nome, telefonesCadas)
            print("Nome:", nome,"Telefones:",agenda_telefonica[nome])

    elif op == 3:
        nome = input("Nome: ")
        # excluirTelefone()
    elif op == 5: 
        break



