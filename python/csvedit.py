import numpy as np
import pandas as pd

dosya = r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\data\toyota.csv'   # tüm markalar icin yapilmali
dataFrame = pd.read_csv(dosya)
dataFrame = dataFrame.drop(columns=['model','tax'])
dataFrame['brand'] = 'toyota'
dataFrame = pd.get_dummies(data=dataFrame,columns=['transmission','fuelType'])

dataFrame.to_csv(r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\toyota.csv',index=False)

dosya2 = r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\toyota.csv'
dataFrame2 = pd.read_csv(dosya2)

dataFrame2['transmission_Automatic'] = dataFrame2['transmission_Automatic'].astype(int)
dataFrame2['transmission_Manual'] = dataFrame2['transmission_Manual'].astype(int)
dataFrame2['transmission_Semi-Auto'] = dataFrame2['transmission_Semi-Auto'].astype(int)
dataFrame2['fuelType_Diesel'] = dataFrame2['fuelType_Diesel'].astype(int)
dataFrame2['fuelType_Hybrid'] = dataFrame2['fuelType_Hybrid'].astype(int)
dataFrame2['fuelType_Petrol'] = dataFrame2['fuelType_Petrol'].astype(int)

try:
    dataFrame2['fuelType_Electric'] = dataFrame2['fuelType_Electric'].astype(int)
except KeyError:
    dataFrame2['fuelType_Electric'] = 0
    print('fuelType_Electric Bulundamadi')
try:
    dataFrame2['fuelType_Other'] = dataFrame2['fuelType_Other'].astype(int)
except KeyError:
    print('fuelType_Other Bulunamadi')
    dataFrame2['fuelType_Other'] = 0
try:
    dataFrame2['transmission_Other'] = dataFrame2['transmission_Other'].astype(int)
except KeyError:
    print('transmission_Other Bulundamadi')
    dataFrame2['transmission_Other'] = 0

dataFrame2 = dataFrame2[sorted(dataFrame2.columns)]    # sütunlari ayni siraya getiriyoruz
dataFrame2.to_csv(dosya2,index=False)