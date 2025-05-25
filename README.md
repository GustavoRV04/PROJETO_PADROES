# Projeto de Padrões de Projeto – Fase 1: Padrões Criacionais

## 📌 Padrões Utilizados

### 1. Factory Method
Utilizado para encapsular a criação dos objetos `Desktop` e `Notebook`, centralizando a lógica e permitindo fácil extensão futura.

### 2. Singleton
Aplicado na classe `CadastroManager`, garantindo uma única instância de controle dos cadastros no sistema.

## 📁 Estrutura
- `src/models/`: contém as classes de produto.
- `src/factories/`: fábrica de produtos.
- `src/core/`: gerenciador de cadastro (Singleton).
- `tests/`: testes automatizados.

## 🧪 Testes
```bash
pip install pytest
pytest
```

## 🚀 Execução
Crie um script ou interface externa que utilize `ProdutoFactory` e `CadastroManager` para gerenciar os produtos.
