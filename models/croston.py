import pandas as pd
import numpy as np
import models.take_dataframe as td

class Croston:
    def __init__(self, alpha=0.1):
        self.alpha = alpha
        self.s = None
        self.y = None
        self.forecast = None

    def fit(self, data):
        demand = np.array(data)
        n = len(demand)

        if n == 0:
            self.s = np.array([0.1])
            self.y = np.array([0.0])
            return

        s = np.zeros(n)
        y = np.zeros(n)
        s[0] = demand[0]
        y[0] = 1.0 

        for t in range(1, n):
            if demand[t] > 0:
                s[t] = s[t - 1] + self.alpha * (demand[t] - s[t - 1])
                y[t] = y[t - 1] + self.alpha * (1 - y[t - 1])
            else:
                s[t] = s[t - 1]
                y[t] = y[t - 1] + self.alpha * (0 - y[t - 1])

        self.s = s
        self.y = y
        self.forecast = s[-1] / y[-1]

    def predict(self, steps):
        if self.s is None or self.y is None:
            raise ValueError("Model has not been fitted.")

        forecast_values = np.zeros(steps)
        for i in range(steps):
            forecast_values[i] = self.forecast
            self.forecast = (self.alpha * 0) + (1 - self.alpha) * self.forecast
        return forecast_values


def take_croston_pred():
    veri = td.take_ronaldo()
    
    tahminler_df = pd.DataFrame(columns=['Yedek Parça Kodu'] + [f'Ay_{i+1}' for i in range(12)])
    
    for idx, row in veri.iterrows():
        yedek_parca_kodu = row['Row Labels']
        yedek_parca_verisi = row[1:].dropna().values 
        
        model = Croston(alpha=0.1)
        model.fit(yedek_parca_verisi)
        tahminler = model.predict(12)
        
        yeni_satir = {'Yedek Parça Kodu': yedek_parca_kodu}
        for i, tahmin in enumerate(tahminler):
            yeni_satir[f'Ay_{i+1}'] = int(tahmin)
        
        tahminler_df = pd.concat([tahminler_df, pd.DataFrame(yeni_satir, index=[0])], ignore_index=True)
        
    return tahminler_df
