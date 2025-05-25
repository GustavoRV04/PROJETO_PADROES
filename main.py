from src.factories.produto_factory import ProdutoFactory
from src.core.cadastro_manager import CadastroManager

def main():
    factory = ProdutoFactory()
    cadastro = CadastroManager()

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

if __name__ == "__main__":
    main()
