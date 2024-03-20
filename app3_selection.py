# -*- coding: utf-8 -*-
import pandas as pd

errors = []

errors.append(pd.read_excel('error_excels/cr_error.xlsx').rename(columns={'MAE': 'cr'}))
errors.append(pd.read_excel('error_excels/des_error.xlsx').rename(columns={'MAE': 'des'}))
errors.append(pd.read_excel('error_excels/ses_error.xlsx').rename(columns={'MAE': 'ses'}))
errors.append(pd.read_excel('error_excels/sma_error.xlsx').rename(columns={'MAE': 'sma'}))
errors.append(pd.read_excel('error_excels/wh_error.xlsx').rename(columns={'MAE': 'wh'}))
errors.append(pd.read_excel('error_excels/tsb_error.xlsx').rename(columns={'MAE': 'tsb'}))

cr_df = pd.read_excel('pred_excels/cr_pred.xlsx')
des_df = pd.read_excel('pred_excels/des_pred.xlsx')
ses_df = pd.read_excel('pred_excels/ses_pred.xlsx')
sma_df = pd.read_excel('pred_excels/sma_pred.xlsx')
wh_df = pd.read_excel('pred_excels/wh_pred.xlsx')
tsb_df = pd.read_excel('pred_excels/tsb_pred.xlsx')

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



df.to_excel('preds_low_error.xlsx', index=False)


df = df[['Yedek Parça Kodu','min_error_model', 'MAE']]

df.to_excel('result.xlsx', index=False)



df = df[df.iloc[:, 2] != 0]
df.loc[df.iloc[:, 1] == 'cr', 1] = 'Croston'
df.loc[df.iloc[:, 1] == 'ses', 1] = 'Tekli Üstel Düzeltme'
df.loc[df.iloc[:, 1] == 'des', 1] = 'Çiftli Üstel Düzeltme'
df.loc[df.iloc[:, 1] == 'wh', 1] = 'Winterholt'
df.loc[df.iloc[:, 1] == 'tsb', 1] = 'TSB'
df.loc[df.iloc[:, 1] == 'sma', 1] = 'Hareketli Ortalamalar'

df.drop(df.columns[1], axis=1, inplace=True)

columns = list(df.columns)
columns[1], columns[2] = columns[2], columns[1]
df = df[columns]

df.rename(columns={df.columns[1]: 'min_error_model'}, inplace=True)

df.to_excel('result_no_0.xlsx', index=False)




