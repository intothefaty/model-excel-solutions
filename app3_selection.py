# -*- coding: utf-8 -*-
import pandas as pd

errors = []

errors.append(pd.read_excel('error_excels/cr_error.xlsx').rename(columns={'Min_Error': 'cr'}))
errors.append(pd.read_excel('error_excels/des_error.xlsx').rename(columns={'Min_Error': 'des'}))
errors.append(pd.read_excel('error_excels/ses_error.xlsx').rename(columns={'Min_Error': 'ses'}))
errors.append(pd.read_excel('error_excels/sma_error.xlsx').rename(columns={'Min_Error': 'sma'}))
errors.append(pd.read_excel('error_excels/wh_error.xlsx').rename(columns={'Min_Error': 'wh'}))
errors.append(pd.read_excel('error_excels/tsb_error.xlsx').rename(columns={'Min_Error': 'tsb'}))

cr_df = pd.read_excel('pred_excels/cr_pred.xlsx')
des_df = pd.read_excel('pred_excels/des_pred.xlsx')
ses_df = pd.read_excel('pred_excels/ses_pred.xlsx')
sma_df = pd.read_excel('pred_excels/sma_pred.xlsx')
wh_df = pd.read_excel('pred_excels/wh_pred.xlsx')
tsb_df = pd.read_excel('pred_excels/tsb_pred.xlsx')

# DataFrame'leri birleştirelim
merged_df = pd.merge(errors[0], errors[1], on='Row Labels')

for i in range(2, 6):
    merged_df = pd.merge(merged_df, errors[i], on='Row Labels')

df = merged_df

# En küçük değeri bulalım
min_column_name = df.iloc[:, 1:].idxmin(axis=1)

# Yeni sütunu ekleme
df['min_error_model'] = min_column_name
df = df.drop(['cr','des','ses','sma','wh','tsb'], axis = 1)
df = df.rename(columns={'Row Labels': 'Yedek Parça Kodu'})

values = []
value_count = 12
for i in range(value_count):
    values.append([])

for index, row in df.iterrows():
    if row['min_error_model'] == 'cr':
        for i in range(value_count):
            values[i].append(cr_df.iloc[index, i + 1])
    elif row['min_error_model'] == 'des':
        for i in range(value_count):
            values[i].append(des_df.iloc[index, i + 1])
    elif row['min_error_model'] == 'ses':
        for i in range(value_count):
            values[i].append(ses_df.iloc[index, i + 1])
    elif row['min_error_model'] == 'sma':
        for i in range(value_count):
            values[i].append(sma_df.iloc[index, i + 1])
    elif row['min_error_model'] == 'wh':
        for i in range(value_count):
            values[i].append(wh_df.iloc[index, i + 1])
    elif row['min_error_model'] == 'tsb':
        for i in range(value_count):
            values[i].append(tsb_df.iloc[index, i + 1])
            
    
    
for i in range(value_count):
    df[('Ay_' + str(i + 1))] = values[i]


df = df.drop(['min_error_model'], axis = 1)
df.to_excel('preds_low_error.xlsx', index=False)




