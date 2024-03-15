import pandas as pd

df_tickers = pd.read_excel("../data/tickers.xlsx")

TICKERS = df_tickers.to_dict()["tickers"]

print(TICKERS)
