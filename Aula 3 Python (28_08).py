    =========Exercício 2==========

ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
niver = int(input("Já fez aniversário esse ano? (1 - sim / 2 - não): "))

idade = ano_atual - ano_nascimento
idade2 = ano_atual - ano_nascimento - 1

if niver == 1:
    if idade < 16:
        print(f"Você tem {idade} anos.", "\nVocê não pode votar.")
    elif idade < 18:
        print(f"Você tem {idade} anos.", "\nSeu voto è facultativo!")
    elif idade > 70:
        print(f"Você tem {idade} anos.", "\nSeu voto è facultativo!")
    else:
        print(f"Você tem {idade} anos.", "\nVocê TEM que votar!")
else:
    if idade2 < 16:
        print(f"Você tem {idade2} anos.", "\nVocê não pode votar.")
    elif idade2 < 18:
        print(f"Você tem {idade2} anos.", "\nSeu voto è facultativo!")
    elif idade2 > 70:
        print(f"Você tem {idade2} anos.", "\nSeu voto è facultativo!")
    else:
        print(f"Você tem {idade2} anos.", "\nVocê TEM que votar!")

    =========Exercício 3==========

limite = int(input("Digite o limite: "))
n = 0
total = 0
while n < limite:
    n += 1
    total += n
    print(f"{n} +")
print(f"O valor total da soma é: {total}")

    =========Exercício 4==========

while True:
    numero = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    print("Digite:", "\n1 - Soma", "\n2 - Subtração", "\n3 - Multiplicação", "\n4 - Divisão", "\n0 - Sair.")
    operacao = int(input("Digite a operação desejada: "))
    if operacao == 0:
        print("Sessão finalizada!")
        break
    elif operacao == 1:
        soma = numero + numero2
        print(f"O resultado da soma é: {soma}")
    elif operacao == 2:
        subtracao = numero - numero2
        print(f"O resultado da subtracao é: {subtracao}")
    elif operacao == 3:
        multiplicacao = numero * numero2
        print(f"O resultado da multiplicacao é: {multiplicacao}")
    elif operacao == 4:
        if numero2 == 0:
            print("Não é possível dividir por zero.")
        else:
            divisao = numero / numero2
            print(f"O resultado da divisao é: {divisao}")
    parar = input("Digite 0 se quiser sair. ")
    if parar == "0":
        print("Sessão finalizada!")
        break

     =========Exercício 5==========
for numeros in range(31):
    if numeros % 2 == 0:
        print(numeros)
        
for n in range(0, 31, 2):
    print(n)
        
    =========Exercício 6==========
fileira = int(input("Quantas fileiras? "))
coluna = int(input("Quantas colunas? "))

for i in range(fileira):
    for j in range(coluna):
        print("X ", end="")
    print()

     =========Exercício 7==========
limite = int(input("Digite o limite: "))
anterior = 0 
proximo = 1
soma = 0 
for i in range(limite):
    print(soma)
    soma = proximo + anterior
    proximo = anterior
    anterior = soma
    #ou
qtd = int(input("> "))
lista = [0, 1]

for i in range(2, qtd):
    lista.append(lista[i-1] + lista[i-2])
print(lista[:qtd])

     =========Exercício 8==========
div =[]
num = int(input("Digite um número: "))
for i in range(1, (num + 1)):
    if num % i == 0:
        div.append(i)
        
if len(div) > 3:
    print("Não é primo")
else:
    print("É primo")
print(div)

 =========Exercício 9==========

import random

RECORDE = 0
while True:
    Vitórias = 0
    x = random.randint(0,10)
    jogador_num = int(input("Digite um número: "))
    par_impar = input("PAR OU IMPAR? ")
    soma = x + jogador_num
    if (soma % 2 ==0 and par_impar == "par") or (soma % 2 != 0 and par_impar == "impar"):
        Vitórias += 1
        if Vitórias > RECORDE:
            RECORDE = Vitórias
        print(f"O computador jogou: {x}")
        print("Você venceu!")
        print(f"\nVitórias = {Vitórias}")
        print(f"\nRECORDE = {RECORDE}")
    elif (soma % 2 == 0 and par_impar == "impar") or (soma % 2 != 0 and par_impar == "par"):
        print(f"O computador jogou: {x}")
        print("Você perdeu!")
        print(f"\nVitórias = {Vitórias}")
        print(f"\nRECORDE = {RECORDE}")
    parar = input("Digite 0 se quiser sair. ")
    if parar == "0":
        print(f"\nRECORDE = {RECORDE}")
        print("Jogo finalizado!")
        break