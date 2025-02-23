import pandas as pd
import numpy as np


dataFrame = pd.read_csv(r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\mergeddata.csv')

dataFrame = dataFrame[dataFrame['_year']!=2060]   # 2006 yerine 2060 yapılan degeri sildik
dataFrame = dataFrame[dataFrame['_year']!=1970]   # 1970 yilinda sacma bir fiyat var

print(len(dataFrame) * 0.01)

yuzde99 = dataFrame.sort_values('_price',ascending=False).iloc[703:]

yuzde99.to_csv(r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\cleandata.csv',index= False)
