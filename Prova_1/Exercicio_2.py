# 2. Escreva um programa que leia um número inteiro maior do que zero e devolva, a soma de
# todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2+5+1). Se
# o número lido não for maior que zero, o programa retornará com a mensagem “Número
# Inválido. Tente novamente”. (Utilize try/except)

class MenorQueZero(Exception):
    pass

try:
    int(input("Digite um número: "))
except:
    print("a")
