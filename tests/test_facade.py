
def test_sistema_facade():
    facade = SistemaFacade()
    facade.cadastrar_produto("desktop", modelo="X1", cor="Preto", 
                            preco=2500, potenciaDaFonte=500)
    relatorio = facade.gerar_relatorio()
    assert relatorio['total_produtos'] == 1