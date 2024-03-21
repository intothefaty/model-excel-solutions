# -*- coding: utf-8 -*-
import pandas as pd

def clean_data(df):
    df = df.fillna(0)
    first_column = df.pop('Row Labels')

    # Geri kalan sütunları alfabetik olarak sıralayalım
    df_sorted = df.sort_index(axis=1)

    # İlk sütunu geri ekleyelim
    df_sorted.insert(0, 'Row Labels', first_column)
    return df_sorted

def take_ronaldo(df):
    df = clean_data(df)
    train = df.iloc[:, :37]  
    return train

def take_real(df):
    df = clean_data(df)
    test = df.iloc[:, 37:]
    test.insert(0, 'Row Labels', df['Row Labels'])
    return test

