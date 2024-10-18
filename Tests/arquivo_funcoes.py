def verificar_email(email):
    return "@" in email and "." in email


class Calculadora:
    def __init__(self) -> None:
        pass
    
    def somar(self, num1, num2) -> float:
        return num1 + num2
    
    def subtrair(self, num1, num2) -> float:
        return num1 - num2
    
    def dividir(self, num1, num2) -> float:
        return num1 / num2
    
    def multiplicar(self, num1, num2) -> float:
        return num1 * num2