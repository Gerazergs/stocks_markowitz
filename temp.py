# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()
import pandas as pd

datos = pd.read_csv('SPY500.csv')

datos.size

#df2 = pd.DataFrame()
year = '2021'
yearend = '2019'
month = '-11-'
day = '01'
# =============================================================================
# for i in range(0,3):#datos.size):
#     print(datos['stocks'].loc[i])
# 
#     df1 = yf.Ticker(datos['stocks'].loc[i])
#     df = df1.history(start= yearend+month+day, end= year+month+day, interval="1d")
#     
#     #yf.download("AMZN AAPL GOOG", start= yearend+month+day, end= year+month+day, interval="1d", group_by='tickers')
#     
#     #print(type(df1))
#     #df2 = pd.concat(df2,df1[])
#     temp = pd.DataFrame.from_dict(df1, orient="index")
#     print (temp.keys())
# =============================================================================
    
#tickers_list = ["aapl", "goog", "amzn", "BAC", "BA"] # example list
#tickers_data= {} # empty dictionary

df = pd.DataFrame()
#df2 = pd.DataFrame()


# =============================================================================
# for i in datos['stocks'].values.tolist():
#     print(i)
#     try:
#         ticker_object = yf.Ticker(i)
#         
#         #convert info() output from dictionary to dataframe
#         
#         #a =  ticker_object.history(start= yearend+month+day, end= year+month+day, interval="1d")
#         a = ticker_object.history(period="1mo")
#         print(a)
#         #temp = pd.DataFrame.from_dict(a)
#         #print(a.values())
#         #df[i] = temp['Close']
#         break
#     except Exception as e:
#         print(e)
#         break
# =============================================================================
    
# create empty dataframe
stock_final = pd.DataFrame()
# iterate over each symbol
for i in datos['stocks'].values.tolist():  
    # print the symbol which is being downloaded
    
    try:
        # download the stock price 
        stock = []
        stock = yf.download(i,start='2019-11-01', end='2021-11-01', progress=False)
        
        # append the individual stock prices 
        if len(stock) == 0:
            None
        else:
            stock_final = stock_final.append(stock,sort=False)
            stock_final[i] = stock_final['Close']
            print(i)
    except Exception as e:
        None
        print(e)
        
   
print(df.head())
df.to_csv('SPY500_descarga.csv')
   
   