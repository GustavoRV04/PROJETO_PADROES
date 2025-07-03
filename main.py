#from src.factories.produto_factory import ProdutoFactory
#from src.core.cadastro_manager import CadastroManager
from src.core.sistema_facade import SistemaFacade
from src.decorators.produto_decorator import GarantiaEstendidaDecorator
from src.strategies.desconto_strategy import DescontoBlackFriday, DescontoEstudante
from src.observers.produto_observer import EmailNotificacaoObserver, LogObserver

def main():
    sistema = SistemaFacade()
    
    print("\n=== CADASTRO DE PRODUTOS ===")
    desktop = sistema.cadastrar_produto("desktop", modelo="Gamer X", cor="Preto", 
                                      preco=4200.0, potenciaDaFonte=600)
    notebook = sistema.cadastrar_produto("notebook", modelo="UltraBook Y", cor="Prata", 
                                       preco=5800.0, tempoDeBateria=10)
    print("PRODUTO: ", desktop.modelo, "FOI CADASTRADO")
    print("PRODUTO: ", notebook.modelo, "FOI CADASTRADO")
    
    print("\n=== CONFIGURAÇÃO DE OBSERVERS ===")
    # Adiciona observers e força uma notificação inicial
    desktop.adicionar_observer(EmailNotificacaoObserver())
    desktop.adicionar_observer(LogObserver())
    notebook.adicionar_observer(LogObserver())
    
    # Força notificação ao alterar um atributo (sem mudar o valor real)
    temp = desktop.preco
    desktop.preco = temp  # Isso disparará os observers
    
    print("\n=== APLICAÇÃO DE DESCONTOS ===")
    estrategia_black_friday = DescontoBlackFriday()
    estrategia_estudante = DescontoEstudante()
    
    # Aplica descontos (já vai disparar observers)
    desktop.preco = desktop.preco - estrategia_black_friday.calcular_desconto(desktop.preco)
    notebook.preco = notebook.preco - estrategia_estudante.calcular_desconto(notebook.preco)
    
    # Aplica decorator
    notebook_com_garantia = GarantiaEstendidaDecorator(notebook, 24)
    sistema.adicionar_produto_existente(notebook_com_garantia)
    
    print("\n=== RELATÓRIO FINAL ===")
    relatorio = sistema.gerar_relatorio()
    print(f"Total de produtos: {relatorio['total_produtos']}")
    for produto in relatorio['produtos']:
        print(f"- {produto}")
    
    print("\n=== TESTE ADICIONAL DE OBSERVERS ===")
    print("Alterando preço do notebook...")
    notebook.preco = notebook.preco - 100

if __name__ == "__main__":
    main()
