import random
numeroCirculos = 5
with open("imagem.svg", "w") as imagem:
    imagem.write('<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">')
    imagem.write('\n<circle cx = "100" cy = "100" r ="100" fill = "red"/>')

    for i in range(numeroCirculos):
        CY = random.randint(0,201)
        CX = random.randint(0,201)
        imagem.write(F'\n<circle cx = "{CX}" cy = "{CY}" r ="1" fill = "blue"/>')
        
    imagem.write('\n</svg>')
    imagem.close()