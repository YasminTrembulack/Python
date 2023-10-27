# 2. Escreva um programa que leia um número inteiro maior do que zero e devolva, a soma de
# todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2+5+1). Se
# o número lido não for maior que zero, o programa retornará com a mensagem “Número
# Inválido. Tente novamente”. (Utilize try/except)

class MenorQueZero(Exception):
    pass

while True:
    try:
        numero = input("Digite um número: ")
        soma = 0

        if int(numero) < 0:
            raise MenorQueZero
        else:
            for n in numero:

                soma += int(n)
            
            print(f"A soma dos algarismos é {soma}.")
            break   

    except MenorQueZero:
        print("Número menor que zero. Tente novamente...")
