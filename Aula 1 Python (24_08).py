INÍCIO
print("Olá Mundo")
print("Vamos programar!")

um = 1
print(type(um))
print (um) #funciona com espaço entre o print e o parentese

print("Minha váriavel é:", um)
print(f"Minha váriavel é: {um}")


        String
nome = input("Digite seu nome:")
vazio = input()
print(nome)

minha_string = '''linha1
linha2
linha3
'''
print(minha_string)

print('McDonald\'s')


        Deixar string maiuscula e minuscula
variavelp = "python"
print(variavelp.upper()) #Maiusculo

variavelp2 = "PYTHON"
print(variavelp2.lower()) #Minusculo


        Numerico
idade = int(input("Digite sua idade:"))
print(f"A sua idade é: {idade}")

TrueFalse = bool(input("É verdadeiro?"))
print(TrueFalse)


        Exercício 1
TCelsius = float(input("Digite a temperatura em Celsius:"))
TFahrenheint = TCelsius * 1.8 +32
print(f"Temperatura em Fahrenheint: {TFahrenheint}°F")


        Posição da letra na palavra/string
fruta = "banana"
letra = fruta[0]
letra2 = fruta[0:4] #o primeiro é sempre 0 , ex:
                    0 1 2 3 4
                    b a n a n (ele vai mostras do 0 até o número digitado -1).
print(letra)
print(letra2)


        Quantidade de letra na palavra/string
print(len(fruta))


        Concatenar (soma de palavras/string)
texto1 = "bana"
texto2 = "na"
print(texto1 + texto2)
print(texto2 * 3)


        Manipulação de string
variavel2 = "n o m-e"
print(variavel2.split(" "))
print(variavel2.split("-")) #ele separa uma string conforme o critério adotado (está
                      localizado entre as ""), devolveno formato de lista.


print(",".join("abc"))
print("-".join(["robert", "bosch", "curitiba"])) # junta cada item do string 
                                                  com um delimitador especifico.


        Exercício2
seu_nome = input("Digite seu nome:")
letra3 = seu_nome[:3]
print(letra3.upper())
    ou    
print(seu_nome[0:3].upper()) 