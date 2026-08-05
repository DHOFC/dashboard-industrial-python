def criar_indicadores(df):


    df["Atingimento_Meta"] = (
        df["Pecas_Produzidas"] /
        df["Meta"]    ) * 100


    df["Eficiencia"] = (
        df["Pecas_Produzidas"] /
        df["Meta"]
    ) * 100

    df["Taxa_Defeitos"] = (
        df["Defeitos"] /
        df["Pecas_Produzidas"]
    ) * 100

    return df
