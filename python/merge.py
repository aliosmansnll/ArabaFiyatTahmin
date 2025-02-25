import pandas as pd
import numpy as np
from sklearn.utils import shuffle

dosya1 = r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\audi.csv'
dosya2 = r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\bmw.csv'
dosya3 = r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\ford.csv'
dosya4 = r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\hyundi.csv'
dosya5 = r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\merc.csv'
dosya6 = r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\skoda.csv'
dosya7 = r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\toyota.csv'

dataFrame1 = pd.read_csv(dosya1)
dataFrame2 = pd.read_csv(dosya2)
dataFrame3 = pd.read_csv(dosya3)
dataFrame4 = pd.read_csv(dosya4)
dataFrame5 = pd.read_csv(dosya5)
dataFrame6 = pd.read_csv(dosya6)
dataFrame7 = pd.read_csv(dosya7)

dataFrame = pd.concat([dataFrame1,dataFrame2,dataFrame3,dataFrame4,dataFrame5,dataFrame6,dataFrame7],ignore_index=True)

dataFrame = shuffle(dataFrame,random_state=42)
dataFrame = pd.get_dummies(data=dataFrame,columns=['brand'])

brandFalseTrue = dataFrame.select_dtypes(exclude=['number'])
dataFrame[brandFalseTrue.columns] = dataFrame[brandFalseTrue.columns].astype(int)

dataFrame = dataFrame.rename(columns={'price':'_price'})
dataFrame = dataFrame.rename(columns={'mileage':'_mileage'})
dataFrame = dataFrame.rename(columns={'mpg':'_mpg'})
dataFrame = dataFrame.rename(columns={'year':'_year'})

dataFrame = dataFrame[sorted(dataFrame.columns)]
dataFrame.to_csv(r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\mergeddata.csv',index=False)


