import tkinter as tk
from tkinter import ttk
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from joblib import load

scale = load('scaler.joblib')
model = load_model(r'C:\Users\alios\OneDrive\Masaüstü\VS Code Projects\ArabaFiyatTahmin\araba_fiyat_tahmin.keras')

def organizationComboBox(fuelType, vites, brand):
    global car_attributes

    match fuelType:
        case 0:
            car_attributes["electric"] = 1
        case 1:
            car_attributes["hybrid"] = 1
        case 2:
            car_attributes["diesel"] = 1
        case 3:
            car_attributes["petrol"] = 1
        case 4:
            car_attributes["other1"] = 1
    
    match vites:
        case 0:
            car_attributes["manuel"] = 1
        case 1:
            car_attributes["auto"] = 1
        case 2:
            car_attributes["other2"] = 1
        case 3:
            car_attributes["manuel"] = 1
    
    match brand:
        case 0:
            car_attributes["audi"] = 1
        case 1:
            car_attributes["bmw"] = 1
        case 2:
            car_attributes["ford"] = 1
        case 3:
            car_attributes["hybrid"] = 1
        case 4:
            car_attributes["mercedes"] = 1
        case 5:
            car_attributes["skoda"] = 1
        case 6:
            car_attributes["toyota"] = 1

def reset_car_attributes():
    for key in car_attributes:
        car_attributes[key] = 0    


def tahmin_et():
    try:
        reset_car_attributes()
        mil = int(mileage_entry.get())
        mpg = float(mpg_entry.get())
        year = int(year_entry.get())
        engineSize = float(engineSize_entry.get())
        fuelType = fuelType_dict.get(fuelType_combobox.get(),0)   # Anahtara karsilik gelen sayiyi donduruyor
        vites = vites_dict.get(vites_combobox.get(),0)
        brand = brand_dict.get(brand_combobox.get(),0)

        organizationComboBox(fuelType,vites,brand)

        girdi= np.array([[mil,mpg,year,car_attributes["audi"],car_attributes["bmw"],car_attributes["ford"],car_attributes["hyundai"],car_attributes["mercedes"],car_attributes["skoda"],car_attributes["toyota"],engineSize,car_attributes["diesel"],car_attributes["electric"],car_attributes["hybrid"],car_attributes["other1"],car_attributes["petrol"],car_attributes["auto"],car_attributes["manuel"],car_attributes["other2"],car_attributes["semi_auto"]]])
        
        scaledGirdi = scale.transform(girdi)
        tahmin = model.predict(scaledGirdi)[0][0]

        sonuc_label.config(text=f'Tahmin Sonucu : {tahmin} Dolar')
    except Exception as e:
        sonuc_label.config(text=f'Hata:{e}')
        print(e)



car_attributes = {
    "audi": 0,
    "bmw": 0,
    "ford": 0,
    "hyundai": 0,
    "mercedes": 0,
    "skoda": 0,
    "toyota": 0,
    "diesel": 0,
    "electric": 0,
    "hybrid": 0,
    "other1": 0,
    "petrol": 0,
    "auto": 0,
    "manuel": 0,
    "other2": 0,
    "semi_auto": 0
}


brand_dict = {'Audi':0, 'BMW':1,'Ford':2,'Hyundai':3,'Mercedes':4, 'Skoda':5, 'Toyota':6}
fuelType_dict = {'Elektrik':0,'Hybrid':1,'Diesel':2,'Benzin':3,'Other':4}
vites_dict = {'Manuel':0,'Otomatik':1,'Yari Otomatik':2,'Other':3}

root = tk.Tk()
root.title('Araba Fiyat Tahmini')


tk.Label(root, text='Mil:').grid(row=0,column=0)
mileage_entry = tk.Entry(root)
mileage_entry.grid(row=0,column=1)


tk.Label(root, text='Yas: ').grid(row=2,column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=2,column=1)


tk.Label(root, text='Motor Hacmi:').grid(row=4,column=0)
engineSize_entry = tk.Entry(root)
engineSize_entry.grid(row=4,column=1)


tk.Label(root, text='MPG:').grid(row=6,column=0)
mpg_entry = tk.Entry(root)
mpg_entry.grid(row=6,column=1)


tk.Label(root,text='Vites Türü').grid(row=8,column=0)
vites_combobox = ttk.Combobox(root,values=list(vites_dict.keys()))
vites_combobox.grid(row=8,column=1)
vites_combobox.set('Manuel')


tk.Label(root,text='Yakit Türü:').grid(row=10,column=0)
fuelType_combobox = ttk.Combobox(root,values=list(fuelType_dict.keys()))
fuelType_combobox.grid(row=10,column=1)
fuelType_combobox.set('Benzin')


tk.Label(root,text='Marka:').grid(row=12,column=0)
brand_combobox = ttk.Combobox(root,values=list(brand_dict.keys()))
brand_combobox.grid(row=12, column=1)
brand_combobox.set('Audi')


tahminButton = tk.Button(root,text='Fiyat Tahmini Yap',command=tahmin_et)
tahminButton.grid(row=16,column=4)

sonuc_label = tk.Label(root,text='Tahmin Sonucu')
sonuc_label.grid(row=16,column=8)

root.mainloop()