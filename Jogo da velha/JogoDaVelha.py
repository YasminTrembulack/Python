def linhavelha():
    import time
    for i in range(3):
        print("|", end = "")
        for j in range(5):
            print("-", end="")
    print("|", end = "")    
    print()
    
    
# posicoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
# def desenhar_jogo_da_velha():
#     numero = 1 
#     linhavelha()
#     for linha in range(6):
#         if linha % 2 == 0:
#             print("|", end = "")
#             for coluna in range(6):
#                 if coluna % 2 == 0:
#                     print("  ", end ="")
#                     print(numero, end="")
#                     print("  ", end ="")
#                     numero += 1
#                 else:
#                     print("|", end = "")
#             print()
#         else:
#             linhavelha()

tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#            0  1  2  3  4  5  6  7  8
def desenhar_jogo_da_velha2():
    
    linhavelha()
    for i in range (len(tabuleiro)):
        print("|", end = "")
        print("  ", end ="")        
        if i % 3 == 2:           
            print(tabuleiro[i], end ="  |" )
            if i < 8:
                print()
                linhavelha()
        else:
            print(tabuleiro[i], end = "")
            print("  ", end ="")      
    print()
    linhavelha()


import random

import random
import time

def jogar_jogo_da_velha():
    desenhar_jogo_da_velha2()
    while True:
        jogada = int(input("Digite a posição que deseja jogar: "))
        computador = random.randint(1, 9)        
        for i in tabuleiro:
            if i == jogada:
                del tabuleiro[i-1]
                tabuleiro.insert(i-1, "X")
                desenhar_jogo_da_velha2() 
                print(tabuleiro)
                time.sleep(1.5)
        for i in tabuleiro:
            if i == computador:
                del tabuleiro[i-1]
                tabuleiro.insert(i-1, "@")
                desenhar_jogo_da_velha2() 
                print(tabuleiro)
                
        if tabuleiro[0] == "X" and tabuleiro[4] == "X" and tabuleiro[8] == "X" :
            print(tabuleiro)
            print("Você ganhou!")
            break
        elif tabuleiro[2] == "X" and tabuleiro[4] == "X" and tabuleiro[6] == "X" or tabuleiro[2] == "@" and tabuleiro[4] == "@" and tabuleiro[6] == "@":
            print(tabuleiro)
            print("Você ganhou!")
            break
        elif tabuleiro[0] == "X" and tabuleiro[1] == "X" and tabuleiro[2] == "X" or tabuleiro[0] == "@" and tabuleiro[1] == "@" and tabuleiro[2] == "@":
            print(tabuleiro)
            print("Você ganhou!")
            break
        elif tabuleiro[3] == "X" and tabuleiro[4] == "X" and tabuleiro[5] == "X" or tabuleiro[3] == "@" and tabuleiro[4] == "@" and tabuleiro[5] == "@":
            print(tabuleiro)
            print("Você ganhou!")
            break
        elif tabuleiro[6] == "X" and tabuleiro[7] == "X" and tabuleiro[8] == "X" or tabuleiro[6] == "@" and tabuleiro[7] == "@" and tabuleiro[8] == "@":
            print(tabuleiro)
            print("Você ganhou!")
            break
        elif tabuleiro[0] == "X" and tabuleiro[3] == "X" and tabuleiro[6] == "X" or tabuleiro[0] == "@" and tabuleiro[3] == "@" and tabuleiro[6] == "@":
            print(tabuleiro)
            print("Você ganhou!")
            break
        elif tabuleiro[1] == "X" and tabuleiro[4] == "X" and tabuleiro[7] == "X" or tabuleiro[1] == "@" and tabuleiro[4] == "@" and tabuleiro[7] == "@":
            print(tabuleiro)
            print("Você ganhou!")
            break
        elif tabuleiro[2] == "X" and tabuleiro[5] == "X" and tabuleiro[8] == "X" or tabuleiro[2] == "@" and tabuleiro[5] == "@" and tabuleiro[8] == "@":
            print(tabuleiro)
            break
        if tabuleiro[0] == "@" and tabuleiro[4] == "@" and tabuleiro[8] == "@":
            pass

jogar_jogo_da_velha()
print(tabuleiro)
