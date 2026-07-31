import pandas as pd

def ler_dados(caminho):

    df = pd.read_excel(caminho)

    return df
