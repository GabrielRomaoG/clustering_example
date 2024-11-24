import pandas as pd


def preprocess_localiza_data(carros_csv: str, vendas_csv: str):
    carros_df = pd.read_csv(carros_csv, delimiter=";").dropna()

    vendas_df = pd.read_csv(vendas_csv, delimiter=";", low_memory=False).dropna()

    final_df = pd.merge(
        vendas_df, carros_df, left_on="MODELO", right_on="MODELO"
    ).rename(columns=lambda x: x.lower().replace(" ", "_"))

    final_df["modelo"] = final_df["modelo"].str.lstrip("MODELO").str.strip()
    final_df["marca"] = final_df["marca"].str.lstrip("MARCA").str.strip()

    return final_df
