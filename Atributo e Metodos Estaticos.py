class Animal:
    
    peixe = 0
    cachorro = 0
    gato = 0
    
    def __init__(self, nome, tipo='peixe'):
        self.__nome = nome
        
        if tipo == 'cachorro':
            Animal.cachorro += 1
            self.__tipo = tipo
        elif tipo == 'gato':
            Animal.gato += 1
            self.__tipo = tipo
        else:
            Animal.peixe += 1
            self.__tipo = 'peixe'

    @staticmethod
    def mostrar():
        print(f'Peixes: {Animal.peixe}')
        print(f'Cachorros: {Animal.cachorro}')
        print(f'Gatos: {Animal.gato}')

a1 = Animal('Garfield', 'gato')
a2 = Animal('Marlim', 'peixe')
a3 = Animal('Cezar', 'macaco')
    
Animal.mostrar()


