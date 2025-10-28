# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 13:04:31 2025
COntents: create graphics for IWRA2025 Conference from NASA-RSWQ Dataset
@author: Isaac Bradford, ibradfo@purdue.edu
"""

# import required modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import numpy as np
import scipy as sp


df = pd.read_csv('.csv') #open a csv within GH folder for data process.

print(df)

df_ch = df.dropna(subset='Chla (ug/L)') #dropna gets rid of nan vlues

'''CHLA Scatterplot'''
vd = df_ch[['Chla (ug/L)', 'Distance from Dam']].groupby('Distance from Dam').mean()
# ^ special function that subets and creates a new 

