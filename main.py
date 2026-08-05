from src.leitura import ler_dados
from src.limpeza import limpar
from src.indicadores import criar_indicadores
from src.analise import criar_analises

sheet_id = "19AOiYL1XfeRLCD9fPN5AA43ZaD4TT5CywFbLvsTQrSM"
gid = "971134971"
caminho = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
print("="*60)
print("INSPECIONANDO OS DADOS BRUTOS")
print("="*60)

df = ler_dados(caminho)

print(df.info())
print("\n")
print(df.head())

df = limpar(df)

print("="*60)
print("INSPECIONANDO OS DADOS LIMPOS")
print(df.info())
print("="*60)

print("\n")
print("\n")

print("="*60)
print("INSPECIONANDO OS DADOS COM INDICADORES")
df = criar_indicadores(df)
print(df.head())
print("="*60)

print("\n")
print("\n")

print("="*60)
print("ANALISE DOS DADOS")
df = criar_analises(df)
print("="*60)



