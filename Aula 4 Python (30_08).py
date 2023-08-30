def escrever():
    print("começo")
    a = 5+2
    print(a)
    print()

import random, time

print("Começo")
time.sleep(2)
print("Finalizando")

def soma(valor1, valor2):
    a = valor1 + valor2
    print(a)

soma(10, 20)


     ==========Exercício 1============
import time
def contador(inicio, fim, passo):
    for i in range(inicio, fim+1, passo):
        print(i)
        time.sleep(0.5)
        
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
passo = int(input("Digite o passo do contador: "))
contador(inicio, fim ,passo)
    =================================
def soma(a, b):
    s = a + b
    return s, a, b
resultado = soma(10, 20)
print(resultado)

def mostrar(nome = "yas"):
    print("O nome é", nome)

mostrar()
mostrar("dudu")

     ==========Exercício 2============

import math
def operacoes(numero):
    raiz = math.sqrt(numero)
    fatorial = math.factorial(numero)
    quadrado = numero * numero
    inverso = 1 / numero
    print("Raiz quadrada: ", raiz, 
          "\nFatorial: ", fatorial,
          "\nNúmero ao quadrado: ", quadrado,
          "\nInverso: ", inverso)

while True:
    n = int(input("Digite um valor: "))
    operacoes(n)
    parar = input("Digite 0 para parar a operação: ")
    if parar == "0":
        break

      ou
    
import math
def operacoes():
    while True:
        numero = int(input("Digite um valor: "))
        raiz = math.sqrt(numero)
        fatorial = math.factorial(numero)
        quadrado = numero * numero
        inverso = 1 / numero
        print("Raiz quadrada: ", raiz, 
              "\nFatorial: ", fatorial,
              "\nNúmero ao quadrado: ", quadrado,
              "\nInverso: ", inverso)
        parar = input("Digite 0 para parar a operação: ")
        if parar == "0":
            break

      ou

import math
def operacoes():
    while True:
        numero = int(input("Digite um valor: "))
        operacoes = {"Raiz Quadrada": math.sqrt(numero) , "Fatorial": math.factorial(numero), 
  "Número ao quadrado": numero * numero, "Inverso": 1 / numero}
        for i in operacoes:
            print(i, end=": ")
            print(operacoes[i])
            
        parar = input("Digite 0 para parar a operação: ")
        if parar == "0":
            break
operacoes()
        =================================
        ==========Exercício 3============
        
import random
def lista_ordenada(limite_inferior, limite_superior, tamanho):
    lista_aleatoria = []
    for i in range(tamanho):
        lista_aleatoria.append(random.randint(limite_inferior, limite_superior))
        
    fim = {"Lista: ": lista_aleatoria.copy()}

    for k in range(tamanho):
        for j in range(tamanho - 1):
            if lista_aleatoria[j] > lista_aleatoria[j+1]:
                lista_aleatoria.append(lista_aleatoria[j])
                lista_aleatoria.remove(lista_aleatoria[j])
                
    fim.update({"Lista ordenada: ": lista_aleatoria})
    for l in fim:
        print(l, end=": ")
        print(fim[l])
            
        
lista_ordenada(0, 50, 5)
        =================================