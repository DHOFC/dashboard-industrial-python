import pandas as pd

def limpar(df):

    print("Limpando dados...")
    df = df.drop_duplicates()

    print("Removendo valores nulos...")
    df = df.dropna()

    return df
