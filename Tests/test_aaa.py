from Python.Tests.arquivo_funcoes import verificar_email, Calculadora

def is_positive(num):
    return num > 0

def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(-5) is False
    
def test_email():
    assert verificar_email("exemplo@gmail.com") is True, "esse email é válido"
    assert verificar_email("exemplo.com") is False, "O email precisa ter @"
    assert verificar_email("exemplo@gmail") is False, "O email precisa ter ."
    
def test_calculadora():
    calculadora = Calculadora()
    
    assert calculadora.somar(5, 2) == 7
    assert calculadora.subtrair(12, 6) == 6
    assert calculadora.multiplicar(9,9) == 81
    assert calculadora.dividir(4,2) == 2