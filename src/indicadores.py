def criar_indicadores(df):

    coluna_meta = "Meta" if "Meta" in df.columns else "Metas"

    df["Eficiencia"] = (
        df["Pecas_Produzidas"] /
        df[coluna_meta]
    ) * 100

    df["Taxa_Defeitos"] = (
        df["Defeitos"] /
        df["Pecas_Produzidas"]
    ) * 100

    return df
