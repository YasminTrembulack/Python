# |-----|-----|-----|
# |  CE |  CM |  CD |
# |-----|-----|-----|
# |  ME |  MO |  MD |
# |-----|-----|-----|
# |  BE |  BM |  BD |
# |-----|-----|-----|

# fileira = int(input("Quantas fileiras? "))
# coluna = int(input("Quantas colunas? "))

# for i in range(fileira):
#     for j in range(coluna):
#         print("X ", end="")
#     print()
def linhavelha():
    import time
    for i in range(3):
        print("|", end = "")
        for j in range(5):
            print("-", end="")
    print("|", end = "")    
    print()

posicoes = [1, 2, 3 ]
posicoes2 = [4, 5, 6]
posicoes3 = [ 7, 8, 9]

for i in range(1):
    linhavelha()
    print("|", end = "")
    for letras in posicoes:
       
        for k in range(1):
            print("  ", end = "")
            
        print(letras, end="")
        print("  ", end = "")
        print("|", end = "")
    print()
    
for i in range(1):
    linhavelha()
    print("|", end = "")
    for letras in posicoes2:
       
        for k in range(1):
            print("  ", end = "")
            
        print(letras, end="")
        print("  ", end = "")
        print("|", end = "")
    print()

for i in range(1):
    linhavelha()
    print("|", end = "")
    for letras in posicoes3:
       
        for k in range(1):
            print("  ", end = "")
            
        print(letras, end="")
        print("  ", end = "")
        print("|", end = "")
    print()
    linhavelha()
    
    

    

