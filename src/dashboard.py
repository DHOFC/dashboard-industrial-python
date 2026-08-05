import streamlit as st
import plotly.express as px

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.leitura import ler_dados
from src.limpeza import limpar
from src.indicadores import criar_indicadores


# Configuração da página do Streamlit
st.set_page_config(
    page_title="Dashboard de Produção Industrial",
    page_icon="🏭",
    layout="wide",
)

# Título do dashboard
st.title("🏭 Painel de Controle - Produção Industrial")
st.markdown("----")


sheet_id = "19AOiYL1XfeRLCD9fPN5AA43ZaD4TT5CywFbLvsTQrSM"
gid = "971134971"
caminho = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

st.sidebar.text("Plantas disponíveis:")
df_bruto = ler_dados(caminho)
df_limpo = limpar(df_bruto)
df = criar_indicadores(df_limpo)

# NOVO: FILTRO NA BARRA LATERAL
# ==========================================
st.sidebar.markdown("---") # Uma linhazinha para separar
st.sidebar.header("Filtros")

# 1. Pegamos todas as plantas únicas que existem nos dados e adicionamos a opção "Todas"
lista_plantas = ["Todas"] + list(df["Planta"].unique())

# 2. Criamos a caixa de seleção na barra lateral
planta_selecionada = st.sidebar.selectbox("Selecione a Planta:", lista_plantas)

# 3. A mágica do Pandas: Se o usuário não escolher "Todas", nós filtramos o df!
if planta_selecionada != "Todas":
    df = df[df["Planta"] == planta_selecionada]
# ==========================================

st.subheader("Base de Dados Tratada")
st.dataframe(df.head(15))

st.markdown("---")

# ==========================================
# 1. CARDS DE KPI (Resumo Rápido)
# ==========================================
st.subheader("💡 Indicadores Principais")

# O Streamlit permite dividir a tela. Vamos criar 3 colunas:
col1, col2, col3 = st.columns(3) 

# Calculando os totais globais da nossa fábrica
total_pecas = df["Pecas_Produzidas"].sum()
total_defeitos = df["Defeitos"].sum()
tempo_parada_total = df["Tempo_Parada_min"].sum()

# Exibindo os números em destaque nos "Cards"
col1.metric("Peças Produzidas", f"{total_pecas:,.0f}".replace(",", "."))
col2.metric("Total de Defeitos", f"{total_defeitos:,.0f}".replace(",", "."))
col3.metric("Horas de Parada", f"{(tempo_parada_total / 60):.0f} h")

st.markdown("---")

# ==========================================
# 2. GRÁFICOS INTERATIVOS LADO A LADO
# ==========================================
# Definindo duas colunas para os gráficos
col_grafico1, col_grafico2 = st.columns(2)

with col_grafico1:
    st.subheader("🏭 Produção por Planta")
    
    # 1. groupby para somar a produção por planta
    producao_planta = df.groupby("Planta")["Pecas_Produzidas"].sum().reset_index()
    
    # 2. Criação do gráfico
    fig1 = px.bar(producao_planta, 
                  x="Planta", 
                  y="Pecas_Produzidas", 
                  color="Planta", # Uma cor para cada planta
                  text_auto='.2s', # Mostra o número abreviado na barra (ex: 888k)
                  title="Total de Peças Produzidas")
    
    # 3. Mandamos o Streamlit exibir o gráfico do Plotly
    st.plotly_chart(fig1, use_container_width=True)

with col_grafico2:
    st.subheader("⏱️ Parada Média por Modelo")
    
    parada_modelo = df.groupby("Modelo")["Tempo_Parada_min"].mean().reset_index()
    
    fig2 = px.bar(parada_modelo, 
                  x="Tempo_Parada_min", # Vamos inverter os eixos para fazer barras horizontais!
                  y="Modelo", 
                  color="Modelo",
                  orientation='h', # Barra horizontal fica mais elegante
                  text_auto='.1f', # Mostra 1 casa decimal
                  title="Tempo Médio de Parada (min)")
    
    st.plotly_chart(fig2, use_container_width=True)