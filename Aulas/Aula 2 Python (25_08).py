    # ============Exercício 3============
nome_completo = input("Digite seu nome completo com letras minúsculas:")
nomeMaiusculo = nome_completo.title()
nomeContagem = nomeMaiusculo.replace(" ","")
print(nomeMaiusculo, "\nSeu nome tem {} letras.".format(len(nomeContagem)))

# yasmin trembulack agostinho


    # Ordenar lista
lista = [4, 8, 2, 3, 1]
lista.sort()
print(lista)

    # Subistituir valor da lista
lista[0] = "a"
print(lista)
    # Ver se tem algo na lista
print(9 in lista)

    # Concatenar lista
lista2 = ["YAS", "SLA"]
print(lista + lista2)

    #===========Exercício 4===========
soma = 0
listaNumeros = []
for i in range(10):
    soma += 1
    listaNumeros.append(int(input(f"Valor{soma}:")))
    listaNumeros.sort()
print(listaNumeros)

    # ou

listaNumeros = []
listaNumeros.append(int(input(f"Valor1:")))
listaNumeros.append(int(input(f"Valor2:")))    
listaNumeros.append(int(input(f"Valor3:")))    
listaNumeros.append(int(input(f"Valor4:")))    
listaNumeros.append(int(input(f"Valor5:")))    
listaNumeros.append(int(input(f"Valor6:")))    
listaNumeros.append(int(input(f"Valor7:")))    
listaNumeros.append(int(input(f"Valor8:")))    
listaNumeros.append(int(input(f"Valor9:")))    
listaNumeros.append(int(input(f"Valor10:")))
listaNumeros.sort()
print(len(listaNumeros))
print(listaNumeros)


    #=========Exercício 5==========
topRicos2023 = ("Elon Musk ($180 B)", "Jeff Bezos ($114 B)", "Larry Ellison ($107 B)", "Bill Gates ($104 B)",  "Warren Buffett ($106 B)", 
"Mark Zuckerberg ($ 112,8 B)", "Larry Page (S$ 112 B)", "Serguey Brin (S$ 106,3 B)", "Steve Ballmer ($102 B)")
print("Os 10 mais ricos são:", topRicos2023)
print("Os 3 mais ricos são:", topRicos2023[:3])
print("O mais rico do mundo é:", topRicos2023[0])

    #=========Exercício 6==========
total = 0
Menu = {"BatataFrita": 7 , "Hamburger": 12, "HotDog": 10, "Suco": 4, "Refrigerante": 5}
print(Menu)
n = int(input("Digite a quantidade de produtos que você deseja compra:"))
for i in range(n):
    comida = input("Digite a comida que deseja:")
    total += Menu[comida]
print(f"O valor total é de: R${total},00")
     
    #=========Exercício 1==========
numeroSecreto = "42"
print("JOGO DA ADIVINHAÇAÕ", "\n------------------------------------------------")

numero = input("Digite seu palpite:")
letra = numero.isdigit()
if letra == False:
    print("Isso não é um número!  >:(")
elif numero == numeroSecreto:
    print("Parabéns!! Você acertou :)")
else:
    print("Você errou. :(")  
