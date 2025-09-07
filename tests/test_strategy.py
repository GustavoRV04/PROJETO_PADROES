import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.strategies.desconto_strategy import DescontoBlackFriday, DescontoEstudante

def test_desconto_black_friday():
    strategy = DescontoBlackFriday()
    assert strategy.calcular_desconto(1000) == 250  # 25% de 1000 = 250

def test_desconto_estudante():
    strategy = DescontoEstudante()
    assert strategy.calcular_desconto(1000) == 150  # 15% de 1000 = 150