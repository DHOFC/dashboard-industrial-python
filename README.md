# Dashboard Industrial em Python

Este projeto cria um dashboard interativo em Streamlit para analisar dados de produção industrial com base em uma planilha pública exportada do Google Sheets.

## O que o projeto faz

- carrega os dados diretamente do link remoto do Google Sheets;
- limpa e organiza a base;
- calcula indicadores de produção, defeitos e eficiência;
- exibe gráficos interativos e métricas em uma interface web.

## Estrutura do projeto

- `src/dashboard.py`: aplicação principal do dashboard.
- `src/leitura.py`: leitura e persistência dos dados.
- `src/limpeza.py`: limpeza e conversão das colunas.
- `src/indicadores.py`: criação dos indicadores.
- `main.py`: versão de linha de comando para análise.
- `requirements.txt`: dependências do projeto.

## Requisitos

- Python 3.10+
- Dependências principais:
  - streamlit
  - pandas
  - plotly

## Como executar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run src/dashboard.py
```

## Deploy no Streamlit Cloud

1. envie este repositório para o GitHub;
2. crie um novo app no Streamlit Cloud;
3. selecione o repositório e use `app.py` ou `src/dashboard.py` como entrypoint;
4. defina o comando de execução como:

```bash
streamlit run app.py
```
