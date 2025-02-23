import pandas as pd
import numpy as np

dataFrame = pd.read_csv(r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\mergeddata.csv')

dataFrame = dataFrame[dataFrame['_year']!=2060]   # 2006 yerine 2060 yapılan degeri sildik

print(dataFrame.groupby('_year').mean()['_price'])