import pandas as pd
import numpy as np
import models_excels.models.take_dataframe as td

class SES:
    def __init__(self, alpha=0.1):
        self.alpha = alpha
        self.level = None
        self.forecast = None

    def fit(self, data):
        demand = np.array(data)
        n = len(demand)

        if n == 0:
            return

        level = demand[0]

        for i in range(1, n):
            level = self.alpha * demand[i] + (1 - self.alpha) * level

        self.level = level
        self.forecast = level

    def predict(self, steps):
        if self.level is None:
            raise ValueError("Model has not been fitted.")

        forecast_values = np.full(steps, self.forecast)
        return forecast_values



def take_ses_pred(df):
    veri = td.take_ronaldo(df)
    
    tahminler_df = pd.DataFrame(columns=['Yedek Parça Kodu'] + [f'Ay_{i+1}' for i in range(12)])
    
    for idx, row in veri.iterrows():
        yedek_parca_kodu = row['Row Labels']
        yedek_parca_verisi = row[1:].dropna().values 
        
        model = SES(alpha=0.1)
        model.fit(yedek_parca_verisi)
        tahminler = model.predict(12)
        
        yeni_satir = {'Yedek Parça Kodu': yedek_parca_kodu}
        for i, tahmin in enumerate(tahminler):
            yeni_satir[f'Ay_{i+1}'] = int(tahmin)
        
        tahminler_df = pd.concat([tahminler_df, pd.DataFrame(yeni_satir, index=[0])], ignore_index=True)
        
    return tahminler_df


