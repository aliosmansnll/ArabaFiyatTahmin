import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataFrame = pd.read_csv(r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\data.csv')

x = dataFrame.drop(columns='_price',axis=1).values
y = dataFrame['_price'].values




# Train ve Test olarak ayiriyoruz
from sklearn.model_selection import train_test_split
from joblib import dump
from sklearn.preprocessing import MinMaxScaler

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=40)
scale = MinMaxScaler()
scale.fit(x_train)
dump(scale, 'scaler.joblib')

print(len(x_test))
print(len(x_train))


# Verileri küçültüyoruz

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)


# Training
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print(x_train.shape)

model = Sequential()

model.add(Dense(12,activation='relu'))
model.add(Dense(12,activation='relu'))
model.add(Dense(12,activation='relu'))

model.add(Dense(1))
model.compile(optimizer='adam',loss='mse')

model.fit(x= x_train, y= y_train,validation_data= (x_test,y_test),batch_size= 350,epochs=400)

# Loss degerlerimizi inceleyelim
kayipVerisi = pd.DataFrame(model.history.history)
kayipVerisi.plot()
plt.show()


# Hata oranlarina bakalim
from sklearn.metrics import mean_absolute_error

modeltahmin = model.predict(x_test)
print(mean_absolute_error(y_test,modeltahmin))
modeltahmin = modeltahmin.flatten()

sonuc = pd.DataFrame({'Gerçek Değerler': y_test, 'Tahmin Edilen Değerler': modeltahmin})

sonuc.to_csv(r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\datachanged\tahminsonuclari.csv',index=False)

# Modeli Kaydedelim
from tensorflow.keras.models import load_model

model.save('araba_fiyat_tahmin.keras')

