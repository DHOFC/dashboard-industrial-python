import pandas as pd

def ler_dados(caminho):

    df = pd.read_csv(caminho)
    df.to_csv("dados/bruto/Base_Simulada_Producao_Industria.csv", index=False)

    return df
