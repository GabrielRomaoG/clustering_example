import pandas as pd


def preprocess_localiza_data(carros_csv: str, vendas_csv: str):
    carros_df = pd.read_csv(carros_csv, delimiter=";").dropna()

    vendas_df = pd.read_csv(vendas_csv, delimiter=";", low_memory=False).dropna()

    final_df = pd.merge(
        vendas_df, carros_df, left_on="MODELO", right_on="MODELO"
    ).rename(columns=lambda x: x.lower().replace(" ", "_"))

    final_df["modelo"] = final_df["modelo"].str.lstrip("MODELO").str.strip()
    final_df["marca"] = final_df["marca"].str.lstrip("MARCA").str.strip()

    dtype_mapping = {
        "modelo": "category",
        "genero": "category",
        "idade": "uint8",
        "tempo_no_estoque": "uint32",
        "kilometragem": "uint32",
        "valor_a_vista": "float32",
        "desconto_percentual": "float64",
        "valor_parcela": "float64",
        "qt_parcelas": "uint16",
        "recomprador": "uint8",
        "carro_na_troca": "uint8",
        "comprou_na_cidade_que_mora": "uint8",
        "marca": "category",
        "carroceria": "category",
        "preco_padrao": "float64",
    }

    return final_df.astype(dtype_mapping)
