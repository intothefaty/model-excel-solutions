import pandas as pd
import numpy as np
import models.take_dataframe as td

class SimpleMovingAverage:
    def __init__(self, window_size=3):
        self.window_size = window_size
        self.forecast = None

    def fit(self, data):
        demand = np.array(data)
        n = len(demand)

        if n == 0:
            return

        if n < self.window_size:
            raise ValueError("Data size is smaller than window size.")

        moving_avg = np.convolve(demand, np.ones(self.window_size)/self.window_size, mode='valid')
        self.forecast = np.mean(moving_avg)

    def predict(self, steps):
        if self.forecast is None:
            raise ValueError("Model has not been fitted.")

        forecast_values = np.array([self.forecast for _ in range(steps)])
        return forecast_values



def take_sma_pred():
    veri = td.take_ronaldo()
    
    tahminler_df = pd.DataFrame(columns=['Yedek Parça Kodu'] + [f'Ay_{i+1}' for i in range(12)])
    
    for idx, row in veri.iterrows():
        yedek_parca_kodu = row['Row Labels']
        yedek_parca_verisi = row[1:].dropna().values 
        
        tahminler = []
        model = SimpleMovingAverage(window_size=len(yedek_parca_verisi))
        
        for _ in range(12):
            model.fit(yedek_parca_verisi)
            tahmin = model.predict(1)[0]  # Bir sonraki ay için tahmin
            tahminler.append(int(tahmin))
            yedek_parca_verisi = np.append(yedek_parca_verisi[1:], tahmin)  # Tahmin edilen değeri veriye ekle
           
        yeni_satir = {'Yedek Parça Kodu': yedek_parca_kodu}
        for i, tahmin in enumerate(tahminler):
            yeni_satir[f'Ay_{i+1}'] = tahmin
        
        tahminler_df = pd.concat([tahminler_df, pd.DataFrame(yeni_satir, index=[0])], ignore_index=True)
        
    return tahminler_df



