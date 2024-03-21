# -*- coding: utf-8 -*-
import pandas as pd

def pred_error_df(errors):
    cr_df = pd.read_excel('models_excels/pred_excels/cr_pred.xlsx')
    des_df = pd.read_excel('models_excels/pred_excels/des_pred.xlsx')
    ses_df = pd.read_excel('models_excels/pred_excels/ses_pred.xlsx')
    sma_df = pd.read_excel('models_excels/pred_excels/sma_pred.xlsx')
    wh_df = pd.read_excel('models_excels/pred_excels/wh_pred.xlsx')
    tsb_df = pd.read_excel('models_excels/pred_excels/tsb_pred.xlsx')

    merged_df = pd.merge(errors[0], errors[1], on='Row Labels')

    for i in range(2, 6):
        merged_df = pd.merge(merged_df, errors[i], on='Row Labels')

    df = merged_df
    min_column_name = df.iloc[:, 1:].idxmin(axis=1)
    df['min_error_model'] = min_column_name
    df = df.rename(columns={'Row Labels': 'Yedek Parça Kodu'})

    min_error_array = []
    values = []
    value_count = 12
    for i in range(value_count):
        values.append([])

    for index, row in df.iterrows():
        if row['min_error_model'] == 'cr':
            min_error_array.append(df['cr'][index])
            for i in range(value_count):
                values[i].append(cr_df.iloc[index, i + 1])
        elif row['min_error_model'] == 'des':
            min_error_array.append(df['des'][index])
            for i in range(value_count):
                values[i].append(des_df.iloc[index, i + 1])
        elif row['min_error_model'] == 'ses':
            min_error_array.append(df['ses'][index])
            for i in range(value_count):
                values[i].append(ses_df.iloc[index, i + 1])
        elif row['min_error_model'] == 'sma':
            min_error_array.append(df['sma'][index])
            for i in range(value_count):
                values[i].append(sma_df.iloc[index, i + 1])
        elif row['min_error_model'] == 'wh':
            min_error_array.append(df['wh'][index])
            for i in range(value_count):
                values[i].append(wh_df.iloc[index, i + 1])
        elif row['min_error_model'] == 'tsb':
            min_error_array.append(df['tsb'][index])
            for i in range(value_count):
                values[i].append(tsb_df.iloc[index, i + 1])
                

    df[('MAE')] = min_error_array

    df = df.drop(['cr','des','ses','sma','wh','tsb'], axis = 1)

    for i in range(value_count):
        df[('Ay_' + str(i + 1))] = values[i]
    
    return df







