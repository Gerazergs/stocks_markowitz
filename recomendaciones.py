# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 23:02:46 2020

@author: Gera-pc
"""

import pandas as pd
import numpy as np
import sys
import warnings
import seaborn as sn
import matplotlib.pyplot as plt

if not sys.warnoptions:
    warnings.simplefilter("ignore")


#datos = pd.read_csv('SPY500_descarga.csv')
df = pd.read_csv('datos_procesados_SPY500.csv')
#print(df.columns)
#df = df.set_index('ticker')
top_tier = df.loc[(df['teynor'] > df['teynor'].quantile(0.95)) & 
           (df['sharpie']> df['sharpie'].quantile(.95))].sort_values(
               by=['rendimiento','riesgo'],ascending = False)
               
               

#top_tier = df.sort_values( by=['rendimiento','riesgo'],ascending = False)

#riesgo es la desviacion estandar
top_tier  = top_tier.reset_index()
top_tier = top_tier.drop('index',axis=1)
print(top_tier.head(35))
#top_tier.to_csv('top_tier.csv')
# =============================================================================
# top_tier = top_tier.sort_values(by=['ticker'], ascending=True)
# 
# 
# 
# datos = pd.read_csv('SPY500_descarga.csv')
# 
# 
# #print()
# 
# matriz =datos[top_tier['ticker'].values.tolist()].corr()
# #var = top_tier['riesgo']*top_tier['riesgo']
# #var.set_index(top_tier['ticker'])
# 
# sn.heatmap(matriz, annot=True)
# plt.show()
# top_tier.to_csv('top.csv')
# 
# print(matriz.head())
# #print(var.head())
# 
# top_tier['extra'] = top_tier['ticker']
# 
# df2 = top_tier.pivot(index="ticker", columns="extra", values="rendimiento")                                                                                                                                               
# 
# full_index = df2.index.union(df2.columns)                                                                                                                                                                 
# 
# df2 = df2.reindex(labels=full_index, axis=0).reindex(labels=full_index, axis=1).fillna(df2.max(), downcast='infer')                                                                                                              
# 
# print(df2.head())   
# 
# df_fin = pd.DataFrame()
# diccionario={}
# x=0
# a =[]
# for i in top_tier['extra'].values.tolist():
#     for j in top_tier['extra'].values.tolist():
#         diccionario.update({ i+'-'+j : df2[i].iloc[0]*df2[j].iloc[0]*matriz[i].loc[j]})
#         a.append(x)
#         x=x+1
# 
# var_covar = pd.DataFrame.from_dict(diccionario, orient='index',columns=['var-covar-Matrix'])
# 
# var_covar =var_covar.reset_index()
# print(var_covar.keys())
# 
# # new data frame with split value columns 
# new = var_covar["index"].str.split("-", n = 1, expand = True) 
#   
# # making separate first name column from new data frame 
# var_covar["ticker1"]= new[0] 
#   
# # making separate last name column from new data frame 
# var_covar["ticker2"]= new[1]
#   
# # Dropping old Name columns 
# var_covar.drop(columns =["index"], inplace = True)
# 
# df3 = var_covar.pivot(index="ticker1", columns="ticker2", values="var-covar-Matrix")                                                                                                                                               
# 
# full_index = df3.index.union(df3.columns)                                                                                                                                                                 
# 
# df3 = df3.reindex(labels=full_index, axis=0).reindex(labels=full_index, axis=1)                                                                                                             
# 
# 
# print(df3.head())
# 
# 
# df3.to_csv('var-covar-Matrix.csv') 
# =============================================================================
