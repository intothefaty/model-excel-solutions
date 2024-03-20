# -*- coding: utf-8 -*-
import pandas as pd

def clean_data():
    df = pd.read_excel('data_excels/ronaldo2.xlsx')
    df = df.fillna(0)
    return df

def take_ronaldo():
    df = clean_data()
    train = df.iloc[:, :37]  
    return train

def take_real():
    df = clean_data()
    test = df.iloc[:, 36:]   
    test.insert(0, 'Row Labels', df['Row Labels'])
    return test

