import pandas as pd
from moexalgo import Market

stocks = Market("shares/TQBR")
all_stocks = pd.DataFrame(stocks.tickers(),index=None)
all_stocks = all_stocks["SECID"]

all_stocks.to_excel("../data/tickers.xlsx")