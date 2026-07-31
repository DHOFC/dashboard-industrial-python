import matplotlib.pyplot as ptl
import seaborn as sns

def producao_por_plantas(df):

    sns.barplot(
        data=df,
        x="Planta",
        y="Pecas_Produzidas"
    )

    ptl.show
