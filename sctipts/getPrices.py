import pandas as pd
import numpy as np

COUNT = 125 # ориг - 247
time1 = "2023-01-03"
time2 = "2023-01-11"


df = pd.read_excel("../data/prices.xlsx",index_col=None)
df.drop(columns='Unnamed: 0', inplace=True)

def getPrices(d):
    try:
        ind = df[df["begin"] == d].index[0]  # индекс даты
        row = df.iloc[ind].to_dict()

        prices = {}
        for i in range(COUNT):
            try:
                if not pd.isnull(row[f"close_{i}"]):
                    prices[i] = row[f"close_{i}"]
            except:
                continue

        return prices
    except:
        print("Date error")

def equalKeys(price1, price2):
    if len(price1) != len(price2):
        return False

    for key in price1.keys():
        try:
            if price2[key]:
                pass
        except:
            return False
    return True

def deleteUnequal(price1,price2):
    diff = []
    keysToRemove1 = [key for key in price1.keys() if key not in price2.keys()]
    for key in keysToRemove1:
        price1.pop(key)
        diff.append(key)

    keysToRemove2 = [key for key in price2.keys() if key not in price1.keys()]
    for key in keysToRemove2:
        price2.pop(key)
        diff.append(key)

    return (price1,price2,diff)



firstPrices = getPrices(time1)


secondPrices = getPrices(time2)

addDict = deleteUnequal(firstPrices,secondPrices)
firstPrices = addDict[0]
secondPrices = addDict[1]
diff = addDict[2]

if not equalKeys(firstPrices,secondPrices):
    print("ГДЕ-ТО ОШИБКА")

usedTickers = firstPrices.keys()
print(diff)
print(len(usedTickers))



# "2023-01-03" на этих двух происходит ну что-то очень странное
# "2023-05-22"