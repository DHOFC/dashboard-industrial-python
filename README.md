# Análise de Dados de Produção

Este projeto realiza uma análise básica de dados de produção a partir de um arquivo Excel, calculando indicadores como eficiência e taxa de defeitos.

## Estrutura do projeto

- `main.py`: ponto de entrada da análise.
- `src/`: módulos com funções de leitura, limpeza e indicadores.
- `dados/`: arquivos de dados usados no projeto.
- `notebooks/`: notebooks para exploração e análise.
- `relatorios/`: pastas para relatórios gerados.

## Requisitos

- Python 3.10+
- Dependências:
  - pandas
  - openpyxl

## Como executar

1. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install pandas openpyxl
```

3. Execute o projeto:

```bash
python main.py
```

## Exemplo de saída

O script imprime as primeiras linhas do DataFrame com os indicadores calculados.
