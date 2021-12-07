# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:47:23 2020

@author: Gera-pc
"""

import pandas as pd
import numpy as np
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


datos = pd.read_csv('SPY500_descarga.csv')
df = pd.read_csv('SPY500.csv')

lista2 = df['stocks'].values.tolist()

df = pd.DataFrame()
df2 = pd.DataFrame()
#x=0
#print(datos)
datos = datos.sort_index(ascending=False)
#datos.reset_index()
#print(datos)

for i in lista2:
    try:
        datos[i+'-W']=  datos[i].shift(1)   
        
        datos[i] = np.log(datos[i+'-W']/datos[i])
        datos= datos.drop([i+'-W'], axis=1)
        
    except Exception as e:
        print(e)
        


datos = datos.drop(datos.iloc[:,0].count()-1, axis =0)
datos = datos.reset_index()
datos = datos.drop('index', axis=1)
#print(datos)

datos = datos.set_index('Date')
#print(datos)
#print(datos.head(10))


rendimiento = datos.mean()*256

#print(rendimiento)
std = datos.std()
riesgo = std * np.sqrt(datos.count())
coeficiente_variacion = riesgo/rendimiento



#print(riesgo)
#print(coeficiente_variacion)



from scipy.stats import linregress
datos = datos.sort_index(ascending=False)
dic={}
dic2={}
for i in lista2:
    try:    
        slope, intercept, r_value, p_value, std_err =linregress(datos['SPY'], datos[i])
        dic.update({i: slope})
        dic2.update({i: intercept})
    #print(dic)
    except Exception as e:
        print(e)
  


df_pendiente = pd.DataFrame.from_dict(dic, orient='index')
df_interseccion = pd.DataFrame.from_dict(dic2, orient='index')
#print(df_pendiente)
df_nuevo = pd.DataFrame()
df_nuevo = pd.concat([rendimiento,riesgo,coeficiente_variacion,df_pendiente, df_interseccion], axis =1)
df_nuevo.columns =['rendimiento','riesgo','coeficiente_variacion','beta','alfa']

#tasa libre de riesgo
tasa = 4.0/100

df_nuevo['sharpie'] = (df_nuevo['rendimiento']-tasa) / df_nuevo['riesgo']
df_nuevo['teynor'] = (df_nuevo['rendimiento']-tasa) / df_nuevo['beta']
print(df_nuevo.head())
df_nuevo.to_csv('datos_procesados_SPY500.csv')

