import pandas as pd

def limpar(df):

    print("Removendo Duplicatas...")
    df = df.drop_duplicates()

    print("Convertendo colunas para data...")
    df["Data"] = pd.to_datetime(df["Data"])

    print("Substituindo , por . nas colunas numéricas...")
    df["Sucata_kg"] = df["Sucata_kg"].str.replace(",", ".").astype(float)
    df["Custo_R$"] = df["Custo_R$"].str.replace(",", ".").astype(float)

    return df
