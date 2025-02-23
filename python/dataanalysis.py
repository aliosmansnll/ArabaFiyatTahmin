import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

dosya = r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\mergeddata.csv'
dataFrame = pd.read_csv(dosya)

print(dataFrame['_price'].describe())    # price analizi

print(dataFrame.isnull().sum())         # null deger var mi kontrol ediyoruz.

print(dataFrame.corr()['_price'])

# sbn.scatterplot(x='_mileage',y='_price',data=dataFrame)
# plt.show()

print(dataFrame.sort_values('_price',ascending=False).head(20))   # ascending False oldugu zaman buyukten kucuge siralar True kucukten buyuge

yuzde99 = pd.read_csv(r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\cleandata.csv')
print(yuzde99.groupby('_year').mean()['_price'])
