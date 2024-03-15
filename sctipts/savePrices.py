import pandas as pd
from moexalgo import Ticker
from getTickers import TICKERS


COL = [
    "open",
    "close",
    "begin"
]

ticker = Ticker(TICKERS[0])

df = pd.DataFrame(ticker.candles(date='2023-01-01', till_date='2023-12-31', period="1D"))
df = df[COL]

for i in range(1,len(TICKERS)):
    try:
        ticker = Ticker(TICKERS[i])
        current_df = pd.DataFrame(ticker.candles(date='2023-01-01', till_date='2023-12-31', period="1D"))
        if not current_df.empty:
            current_df = current_df[COL]
            current_df = current_df.rename(columns={"open": f"open_{i}", "close": f"close_{i}"})
            df = pd.merge(df,current_df, how="outer", on='begin')
        else:
            print(TICKERS[i])
            del TICKERS[i]
    except:
        continue


df = df.rename(columns={"open":"open_0","close":"close_0"})

df.to_excel("../data/prices.xlsx")



