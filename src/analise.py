def criar_analises(df):


    print("="*60)
    resultado_planta = df.groupby("Planta")["Pecas_Produzidas"].sum()
    print(resultado_planta)
    print("="*60)

    print("="*60)
    resultado_modelo_tempo_parado = df.groupby("Modelo")["Tempo_Parada_min"].mean()
    print(resultado_modelo_tempo_parado)
    print("="*60)

    print("="*60)
    resultado_turno_defeitos = df.groupby("Turno")["Defeitos"].sum()
    print(resultado_turno_defeitos)
    print("="*60)





