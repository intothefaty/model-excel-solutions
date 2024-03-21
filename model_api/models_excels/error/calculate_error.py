import pandas as pd
from sklearn.metrics import mean_absolute_error

def error_metrics(tahmin_df, gercek_df, baslangic_ayi, bitis_ayi):
    baslangic_index = baslangic_ayi
    bitis_index = bitis_ayi + 1
    
    tahmin_veri = tahmin_df.iloc[:, baslangic_index:bitis_index]
    gercek_veri = gercek_df.iloc[:, baslangic_index:bitis_index]
    
    parca_kodu = tahmin_df.iloc[:, 0]
    
    error_list = []
    
    for i in range(len(tahmin_df)):
        kod = parca_kodu[i]
        tahmin_degerleri = tahmin_veri.iloc[i]
        gercek_degerler = gercek_veri.iloc[i]
        
        mae = mean_absolute_error(gercek_degerler, tahmin_degerleri)
        
        error_list.append({'Row Labels': kod, 'MAE': mae})
    
    error_df = pd.DataFrame(error_list)
    
    return error_df