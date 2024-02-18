# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import models.take_dataframe as td


class TSB:
    def __init__(self, alpha=0.1, beta=0.1):
        self.alpha = alpha
        self.beta = beta
        self.s = None
        self.b = None
        self.forecast = None

    def fit(self, data):
        demand = np.array(data)
        n = len(demand)

        if n == 0:
            self.s = np.array([0.1])
            self.b = np.array([0.0])
            return

        s = np.zeros(n)
        b = np.zeros(n)
        s[0] = demand[0]
        b[0] = demand[1] - demand[0]

        for t in range(1, n):
            s[t] = self.alpha * demand[t] + (1 - self.alpha) * (s[t - 1] + b[t - 1])
            b[t] = self.beta * (s[t] - s[t - 1]) + (1 - self.beta) * b[t - 1]

        self.s = s
        self.b = b
        self.forecast = s[-1] + b[-1]

    def predict(self, steps):
        if self.s is None or self.b is None:
            raise ValueError("Model has not been fitted.")

        forecast_values = np.zeros(steps)
        for i in range(steps):
            forecast_values[i] = self.s[-1] + (i + 1) * self.b[-1]  # Simple linear extrapolation
        return forecast_values


def take_tsb_pred():
    veri = td.take_ronaldo()
    
    tahminler_df = pd.DataFrame(columns=['Yedek Parça Kodu'] + [f'Ay_{i+1}' for i in range(12)])
    
    for idx, row in veri.iterrows():
        yedek_parca_kodu = row['Row Labels']
        yedek_parca_verisi = row[1:].dropna().values 
        
        model = TSB(alpha=0.1, beta=0.1)
        model.fit(yedek_parca_verisi)
        tahminler = model.predict(12)
        
        yeni_satir = {'Yedek Parça Kodu': yedek_parca_kodu}
        for i, tahmin in enumerate(tahminler):
            yeni_satir[f'Ay_{i+1}'] = int(tahmin)
        
        tahminler_df = pd.concat([tahminler_df, pd.DataFrame(yeni_satir, index=[0])], ignore_index=True)
        
        tahmin_sutunlari = tahminler_df.columns[1:]  # Parça Kodu sütununu hariç tutuyoruz
        tahminler_df[tahmin_sutunlari] = tahminler_df[tahmin_sutunlari].applymap(lambda x: max(0, x))
        
    return tahminler_df
