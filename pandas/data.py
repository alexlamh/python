import numpy as np
import pandas as pd
import os
import codecs
import csv

def file_size(file_path):
        file_info = os.stat(file_path)
        return file_info.st_size

if __name__  == "__main__":

    file_path = 'test.csv'
    print(file_size(file_path))

    df = pd.read_csv('https://bit.ly/drinksbycountry')

    # try:
    #     df = pd.read_csv(file_path, encoding='utf-8', delimiter=';', decimal=',')
    # except:
    #     df = pd.read_csv(file_path, encoding='latin', delimiter=';', decimal=',')

    # for col in df.columns:  
    #     if df[col].dtype == 'object':
    #         #convert object to datetime
    #         try:
    #             df[col] = pd.to_datetime(df[col])
    #         except:
    #             pass
    #         #convert valores to float
    #         try:
    #             df[col] = df[col].apply(lambda x: float(x.replace(".","").replace(",",".")))
    #         except:
    #             pass
            

    print(df.dtypes)
    
    print(df)