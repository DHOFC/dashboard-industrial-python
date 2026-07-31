from src.leitura import ler_dados
from src.limpeza import limpar
from src.indicadores import criar_indicadores
from src.analise import total_produzidos

caminho = "dados/bruto/Base_Simulada_Producao_Industria.xlsx"

print("="*60)
print("ANÁLISE DA PRODUÇÃO")
print("="*60)

df = ler_dados(caminho)

df = limpar(df)

df = criar_indicadores(df)

print(df.head().to_string(index=False))

print("="*60)
print("TOTAL DE PEÇAS PRODUZIDAS")
print("="*60)

df = total_produzidos(df)
print(f"Total de peças produzidas: {df}")

