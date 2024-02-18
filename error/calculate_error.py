import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import math

def error_metrics(tahmin_df, gercek_df, baslangic_ayi, bitis_ayi):

    # Başlangıç ve bitiş ayı indekslerini al
    baslangic_index = baslangic_ayi
    bitis_index = bitis_ayi + 1
    
    # Başlangıç ile bitiş arasındaki ay verilerini al
    tahmin_veri = tahmin_df.iloc[:, baslangic_index:bitis_index]
    gercek_veri = gercek_df.iloc[:, baslangic_index:bitis_index]
    
    # Parça Kodu sütunlarını ayır
    parca_kodu = tahmin_df.iloc[:, 0]
    
    # Hesaplamaları yapmak için boş bir liste oluştur
    error_list = []
    
    # Hesaplamaları yap
    for i in range(len(tahmin_df)):
        kod = parca_kodu[i]
        tahmin_degerleri = tahmin_veri.iloc[i]
        gercek_degerler = gercek_veri.iloc[i]
        
        # Hata metriklerini hesapla
        mae = mean_absolute_error(gercek_degerler, tahmin_degerleri)
        mse = mean_squared_error(gercek_degerler, tahmin_degerleri)
        rmse = math.sqrt(mse)
        
        gercek_degerler = np.where(np.abs(gercek_degerler) < 0.001, 0.001, gercek_degerler)
        mape = np.mean(np.abs((gercek_degerler - tahmin_degerleri) / gercek_degerler)) * 100
        
        # Listeye ekle
        error_list.append({'Row Labels': kod, 'MAE': mae, 'RMSE': rmse, 'MAPE': mape})
    
    # Liste üzerinden DataFrame oluştur
    error_df = pd.DataFrame(error_list)
    
    # Değerleri dönüştür
    for col in ['MAE', 'RMSE', 'MAPE']:
        min_value = error_df[col].min()
        max_value = error_df[col].max()
        error_df[col] = (error_df[col] - min_value) / (max_value - min_value)
        
    error_df['Min_Error'] = error_df[['MAE', 'RMSE', 'MAPE']].min(axis=1)
    
    error_df = error_df.drop(['MAE','RMSE','MAPE'], axis=1)
    
    return error_df
