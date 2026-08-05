# 🏭 Dashboard de Produção Industrial (End-to-End)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-150458?logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Data_Viz-3F4F75?logo=plotly&logoColor=white)

## 🌐 Acesse o Projeto Online
👉 **[CLIQUE AQUI PARA VER O DASHBOARD INTERATIVO](https://dashboard-industrial-python.streamlit.app/)**

---

## 📋 Sobre o Projeto
Este é um projeto completo de Análise de Dados desenvolvido em Python, construído com uma visão de "Ponta a Ponta" (End-to-End). 
O objetivo é monitorar o desempenho de uma fábrica através da leitura de dados em nuvem, tratamento automático da base e exibição de indicadores de performance (KPIs) em uma interface web interativa.

## 🚀 Principais Funcionalidades
- **Conexão em Nuvem:** Os dados são extraídos diretamente do link remoto do Google Sheets.
- **Pipeline de ETL:** Limpeza e organização da base usando Pandas (tratamento nulos, conversão de colunas).
- **Métricas de KPI:** Cálculo de Peças Produzidas, Total de Defeitos e Eficiência de Parada.
- **Gráficos Interativos:** Visualização de dados dinâmicos utilizando a biblioteca Plotly.
- **Filtros Dinâmicos:** Barra lateral com filtros que recalcula todos os gráficos e KPIs instantaneamente.

## 📂 Estrutura do Projeto
O código segue as melhores práticas de organização, separando responsabilidades:
- `src/dashboard.py`: Aplicação principal e front-end do dashboard.
- `src/leitura.py`: Script responsável por conectar na Nuvem e extrair os dados brutos.
- `src/limpeza.py`: Motor de regras de tratamento (limpeza de caracteres, tipagem, nulos).
- `src/indicadores.py`: Criação de variáveis e cruzamentos para a regra de negócio.
- `main.py`: Versão de linha de comando para análise estrutural.
- `requirements.txt`: Lista de dependências do projeto para deploy.

---

## 💻 Como executar localmente (Para Desenvolvedores)

Se você deseja clonar o projeto e rodar na sua própria máquina, siga os passos abaixo:

**1. Crie e ative o ambiente virtual:**
```bash
python -m venv .venv
.venv\Scripts\activate
