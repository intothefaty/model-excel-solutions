import models_excels.error.calculate_error as err
import models_excels.models.take_dataframe as td
import pandas as pd


def app2(df):
    gercek_df = td.take_real(df)
    baslangic_ayi = 1
    bitis_ayi = 8

    errors = []
    file_path = 'models_excels/pred_excels/'
    last_path_pred = '_pred.xlsx'
    names = ['cr', 'des', 'ses', 'sma', 'wh', 'tsb']

    forecasts = []
    for name in names:
        forecasts.append(pd.read_excel(file_path + name + last_path_pred))

    for forecast in forecasts:
        hata_metrikleri = err.error_metrics(forecast, gercek_df, baslangic_ayi, bitis_ayi)
        errors.append(hata_metrikleri)

    errors[0].to_excel('models_excels/error_excels/cr_error.xlsx', index=False)
    errors[1].to_excel('models_excels/error_excels/des_error.xlsx', index=False)
    errors[2].to_excel('models_excels/error_excels/ses_error.xlsx', index=False)
    errors[3].to_excel('models_excels/error_excels/sma_error.xlsx', index=False)
    errors[4].to_excel('models_excels/error_excels/wh_error.xlsx', index=False)
    errors[5].to_excel('models_excels/error_excels/tsb_error.xlsx', index=False)

    errors[0] = errors[0].rename(columns={'MAE': 'cr'})
    errors[1] = errors[1].rename(columns={'MAE': 'des'})
    errors[2] = errors[2].rename(columns={'MAE': 'ses'})
    errors[3] = errors[3].rename(columns={'MAE': 'sma'})
    errors[4] = errors[4].rename(columns={'MAE': 'wh'})
    errors[5] = errors[5].rename(columns={'MAE': 'tsb'})

    return errors
