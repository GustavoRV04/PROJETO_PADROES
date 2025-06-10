from src.factories.produto_factory import ProdutoFactory
from src.core.cadastro_manager import CadastroManager
from src.core.sistema_facade import SistemaFacade
from src.decorators.produto_decorator import GarantiaEstendidaDecorator

def main():
    factory = ProdutoFactory()
    cadastro = CadastroManager()
    sistema = SistemaFacade()

    # Criar um Desktop
    desktop = factory.criar_produto("desktop", modelo="Gamer X", cor="Preto", preco=4200.0, potenciaDaFonte=600)
    cadastro.adicionar_produto(desktop)

    # Criar um Notebook
    notebook = factory.criar_produto("notebook", modelo="UltraBook Y", cor="Prata", preco=5800.0, tempoDeBateria=10)
    cadastro.adicionar_produto(notebook)

    # Listar produtos cadastrados
    print("Produtos cadastrados:")
    for info in cadastro.listar_produtos():
        print("-", info)

    # Cadastrar produtos através da fachada
    desktop = sistema.cadastrar_produto("desktop", modelo="Gamer X", cor="Preto", 
                                      preco=4200.0, potenciaDaFonte=600)
    
    notebook = sistema.cadastrar_produto("notebook", modelo="UltraBook Y", cor="Prata", 
                                       preco=5800.0, tempoDeBateria=10)
    
    # Aplicar decorator e adicionar ao cadastro
    notebook_com_garantia = GarantiaEstendidaDecorator(notebook, 24)
    sistema.adicionar_produto_existente(notebook_com_garantia)
    
    # Gerar relatório
    relatorio = sistema.gerar_relatorio()
    print("Relatório do Sistema:")
    print(f"Total de produtos: {relatorio['total_produtos']}")
    for produto in relatorio['produtos']:
        print("-", produto)

if __name__ == "__main__":
    main()
