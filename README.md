Projeto: Cadastro de Produtos com Padrões Criacionais

## Padrões de Projeto Utilizados:

### 1. Factory Method
### 2. Singleton

---

## Por que escolhemos esses padrões

### Factory Method
Escolhi o padrão Factory Method para **centralizar a lógica de criação dos objetos `Desktop` e `Notebook`**. Isso permite criar objetos com diferentes atributos sem precisar modificar o código da aplicação principal. Além disso, facilita a extensão futura com novos tipos de produtos, como `Tablet`, sem alterar o código cliente.

### Singleton
Utilizei o padrão Singleton para garantir que exista apenas **uma instância global do gerenciador de cadastros (`CadastroManager`)**. Isso é útil para manter um repositório centralizado dos objetos criados durante a execução, permitindo consistência e controle único sobre os dados.

---

## Como os padrões foram implementados

### Factory Method

```python
# src/factories/produto_factory.py
from src.models.desktop import Desktop
from src.models.notebook import Notebook

class ProdutoFactory:
    def criar_produto(self, tipo, **kwargs):
        if tipo == "desktop":
            return Desktop(**kwargs)
        elif tipo == "notebook":
            return Notebook(**kwargs)
        else:
            raise ValueError("Tipo de produto inválido.")

##  Padrões Implementados - Fase 2

### 1. Decorator
Permite adicionar novas funcionalidades a objetos existentes dinamicamente, sem alterar sua estrutura. 
Aplicado para adicionar serviços como garantia estendida aos produtos.

### 2. Facade
Fornece uma interface simplificada para um subsistema complexo (cadastro, fábrica, relatórios). 
Centraliza as operações principais do sistema em uma única classe.

## Testes
Novos testes para os padrões estruturais foram adicionados:
```bash
pytest tests/test_decorator.py
pytest tests/test_facade.py
