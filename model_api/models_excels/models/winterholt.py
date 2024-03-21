# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import models_excels.models.take_dataframe as td

class WinterHolt:
    def __init__(self, alpha=0.1, beta=0.1, gamma=0.1, period=12):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.period = period
        self.level = None
        self.trend = None
        self.seasonal = None
        self.forecast = None

    def fit(self, data):
        demand = np.array(data)
        n = len(demand)

        if n == 0:
            return

        if n < self.period:
            raise ValueError("Data size is smaller than the seasonal period.")

        level = np.mean(demand[:self.period])
        trend = (np.mean(demand[self.period:2*self.period]) - np.mean(demand[:self.period])) / self.period

        seasonal = np.zeros(self.period)
        for i in range(self.period):
            seasonal[i] = np.mean([demand[j] for j in range(i, n, self.period)]) - level

        for i in range(n):
            if i >= self.period:
                level_prev = level
                trend_prev = trend
                seasonal_prev = seasonal[i % self.period]

                level = self.alpha * (demand[i] - seasonal_prev) + (1 - self.alpha) * (level_prev + trend_prev)
                trend = self.beta * (level - level_prev) + (1 - self.beta) * trend_prev
                seasonal[i % self.period] = self.gamma * (demand[i] - level) + (1 - self.gamma) * seasonal_prev

        self.level = level
        self.trend = trend
        self.seasonal = seasonal
        self.forecast = level + trend + seasonal[-1]

    def predict(self, steps):
        if self.level is None or self.trend is None or self.seasonal is None:
            raise ValueError("Model has not been fitted.")

        forecast_values = np.zeros(steps)
        for i in range(steps):
            forecast_values[i] = self.level + self.trend * (i + 1) + self.seasonal[(i + 1) % self.period]
        return forecast_values





def take_wh_pred(df):
    veri = td.take_ronaldo(df)
    
    tahminler_df = pd.DataFrame(columns=['Yedek Parça Kodu'] + [f'Ay_{i+1}' for i in range(12)])
    
    for idx, row in veri.iterrows():
        yedek_parca_kodu = row['Row Labels']
        yedek_parca_verisi = row[1:].dropna().values 
        
        model = WinterHolt(alpha=0.1, beta=0.1, gamma=0.1, period=12)
        model.fit(yedek_parca_verisi)
        tahminler = model.predict(12)
        
        yeni_satir = {'Yedek Parça Kodu': yedek_parca_kodu}
        for i, tahmin in enumerate(tahminler):
            yeni_satir[f'Ay_{i+1}'] = int(tahmin)
        
        tahminler_df = pd.concat([tahminler_df, pd.DataFrame(yeni_satir, index=[0])], ignore_index=True)
        
        tahmin_sutunlari = tahminler_df.columns[1:]
        tahminler_df[tahmin_sutunlari] = tahminler_df[tahmin_sutunlari].applymap(lambda x: max(0, x))
        
        
    return tahminler_df

