import pytest
import requests
from unittest.mock import MagicMock
import requests
from atividade01 import *

@pytest.fixture

def mock_banco(mocker):
    # Simula uma chamada de API
    banco = BancoDeDados()
    mocker.patch.object(banco, 'buscar_pedido', return_value = ({"id": 1, "cliente": "joão"}))
    return banco

def test_calcular_o_valor_total(mocker):
    mocker_resposta = mocker.patch('requests.get')
    mocker_resposta.return_value.json.return_value = [{"produto": "Produto 1", "preco": 15.0, "quantidade": 2},
                                                      {"produto": "Produto 2", "preco": 20.0, "quantidade": 1}]
    total = calcular_valor_total(1)
    assert total == 50.0
    

def test_obter_pedido_com_valor_total(mocker, mock_banco):
    mocker_resposta = mocker.patch('requests.get')
    mocker_resposta.return_value.json.return_value = [{"produto": "Produto 1", "preco": 15.0, "quantidade": 2},
                                                      {"produto": "Produto 2", "preco": 20.0, "quantidade": 1}]
    
    pedido = obter_pedido_com_valor_total(1, mock_banco)
    assert pedido == {"id": 1, "cliente": "joão", "valor_total": 50.0}