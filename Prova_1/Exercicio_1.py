# 1.Crie um programa que recebe o arquivo clientes.txt, que possui uma lista com nomes de
# clientes, onde alguns dados foram corrompidos, limpe os dados removendo todos os
# caractéres especiais ou números, com somentes a primeiras letra de cada palavra maiúscula e
# salve em um novo arquivo. Exiba quantos itens foram recuperados.

arquivo = open("Prova/clientes.txt", "r")
nomes = open("Prova/Nomes_limpos.txt", "w")

#with open("Prova/clientes.txt", "r") as arquivo:

lista_nomes = []
contador = 0

for linhas in arquivo:

    nome_limpo = ""

    for letras in linhas:
        if letras.isalpha():
            nome_limpo += letras
        elif letras == " ":
            nome_limpo += letras
    
    lista_nomes.append(nome_limpo.lower().title())
    contador += 1

nomes.write("\n".join(lista_nomes))
print(f"Foram recuperados {contador} dados.")    

arquivo.close()
nomes.close()