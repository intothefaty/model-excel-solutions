# -*- coding: utf-8 -*-
import pandas as pd

def app4(df):
    df.loc[df.iloc[:, 1] == 'cr', 1] = 'Croston'
    df.loc[df.iloc[:, 1] == 'ses', 1] = 'Tekli Üstel Düzeltme'
    df.loc[df.iloc[:, 1] == 'des', 1] = 'Çiftli Üstel Düzeltme'
    df.loc[df.iloc[:, 1] == 'wh', 1] = 'Winterholt'
    df.loc[df.iloc[:, 1] == 'tsb', 1] = 'TSB'
    df.loc[df.iloc[:, 1] == 'sma', 1] = 'Hareketli Ortalamalar'

    df.drop(df.columns[1], axis=1, inplace=True)

    last_column = df.iloc[:, -1]

    first_columns = df.iloc[:, :1]

    df = df.iloc[:, :-1]

    df = pd.concat([first_columns, last_column, df], axis=1)

    df.rename(columns={df.columns[1]: 'min_error_model'}, inplace=True)

    df.to_excel('models_excels/preds_low_error.xlsx', index=False)

    return df
