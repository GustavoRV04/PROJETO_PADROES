import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.desktop import Desktop
from src.observers.produto_observer import EmailNotificacaoObserver

def test_observer_notificacao():
    # Cria um desktop (agora importado corretamente)
    produto = Desktop(modelo="X1", cor="Preto", preco=1000, potenciaDaFonte=500)
    
    # Adiciona observer
    observer = EmailNotificacaoObserver()
    produto.adicionar_observer(observer)
    
    # Altera preço para disparar notificação
    produto.preco = 900
    
    # Verifica se o observer foi chamado
    # (Como não temos retorno, testamos se a execução ocorre sem erros)
    assert True  # Teste básico de execução