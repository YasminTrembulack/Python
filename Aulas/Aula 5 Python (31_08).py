# while True:
#     try:
#         x = int(input("Digite um número: "))
#         break
#     except ValueError:
#         print("Valor inválido! Tente novamente...")

# def imprima_ordenado(colecao):
#     try:
#         colecao.sort()
#     except AttributeError:
#         print("Imutável")
#         pass
#     print(colecao, "\n")
    
# imprima_ordenado([3, 2, 1])
# imprima_ordenado((3, 2 ,1))
# imprima_ordenado("321")

# def exemplo(x):
#     if x <= 0:
#         raise StopIteration
#     x = x-1
#     return x

# x = 5

# while True:
#     try:
#         x = exemplo(x)
#         print(x)
#     except StopIteration:
#         break


# class NovoErro(Exception):
#     pass       

# import time
# def exemplo(x):
#     if x <= 0:
#         raise NovoErro
#     x = x-1
#     time.sleep(1)
#     return x
    
# x = 5
# while True:
#     try:
#         x = exemplo(x)
#         print(x)
#     except NovoErro:
#         print("Algo deu errado!")
#         break


# def calculadora():
#     while True:
#         try:
#             numero1 = int(input("Digite um número: "))
#             numero2 = int(input("Digite outro número: "))
#             print("Digite:", "\n1 - Soma", "\n2 - Subtração", "\n3 - Multiplicação", "\n4 - Divisão", "\n0 - Sair.")
#             operacao = int(input("Digite a operação desejada: "))
#         except ValueError:
#             print("Valor inválido! Tente novamente...")
        
#         if operacao == 0:
#             print("Sessão finalizada!")
#             break
#         elif operacao == 1:
#             soma = numero1 + numero2
#             print(f"O resultado da soma é: {soma}")
#         elif operacao == 2:
#             subtracao = numero1 - numero2
#             print(f"O resultado da subtracao é: {subtracao}")
#         elif operacao == 3:
#             multiplicacao = numero1 * numero2
#             print(f"O resultado da multiplicacao é: {multiplicacao}")
#         elif operacao == 4:
#             try:
#                 divisao = numero / numero2
                    
#             except ZeroDivisionError:
#                 print("Não é possível dividir por zero.")
#                 break
#         parar = input("Digite 0 se quiser sair. ")
#         if parar == "0":
#             print("Sessão finalizada!")
#             break

# calculadora()
# arquivo = open('arquivo.txt', 'w')
# arquivo.write("olá mundo")

# arquivo = open('arquivo.txt', 'r')
# print(arquivo.read())
#.close()

# arquivo = open('arquivo.txt', 'a') #append

musicaTOP =[]
with open('musica.txt', 'r') as arquivo:
    for linha in arquivo:
        substituirN = linha.replace("\n", " ")
        partes = substituirN.split(" ")
        for parte in partes:
            minusculo = parte.lower()
            print(parte)
            musicaTOP.append(minusculo)

print(musicaTOP)

escolhida = input("Digite uma palavra: ")
quantidade = 0
for palavras in musicaTOP:
    if palavras == escolhida:
        quantidade += 1
print(quantidade)








        