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

#CSV TITLES

#UniqueID	BottleNo	True Bottle ID	NumID	Location No	Distance From Dam
	
#Lake ID (4 dig.)	Sampling Type (B/S)	NH4Results	NOxResults	PO4Results	

#TPResults	NH4 BDL	Nox BDL	PO4 BDL	TP BDL	Microcystin Concentration	

#Chla (Avg 24 and on)	Pheo (Avg 24 and on)	NPOC (AVG) mg/L? [TOC]	

#TN (AVG) mg/L? [TOC]	Secchi Depth (m)	Lat	Long	Month	Day	Year
	
#Exclude	Date	FLIR

print('HAHAHA NEW ONE')

df = pd.read_csv('Substitute_Database_All_Samples2025_D.csv') #open a csv within GH folder for data process.
#print(df)
#https://www.geeksforgeeks.org/pandas/ways-to-filter-pandas-dataframe-by-column-values/
#filter data frames

#2024 = 226 rows of data
df_23 = df[df['Year']<2024]
#print(df_23)

#2025 = 108 rows of data
df_25 = df[df['Year']>2024]
#print(df_25)

#2024 - 288 rows of data
df_24 = df[df['Year']==2024]
#print(df_24)

df_ch = df.dropna(subset='Chla (Avg 24 and on)') #dropna gets rid of nan vlues
df_dfd = df.dropna(subset='Distance From Dam') #dropna gets rid of nan vlues

"""DATA CHECKING"""

'''
plt.figure(figsize=(12,6)) #space out recording
adgb = sns.scatterplot(x='Distance From Dam', y='Chla (Avg 24 and on)', data=df_ch) 
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Average Chl-a Concentration (ug/L)')
adgb.set_title("Average Chl-a Recorded Distance from the Dam (2023-2025)")
#plt.show()
'''
'''
plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance From Dam', y='Chla (Avg 24 and on)', data=df_ch, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Chl-a Concentration (ug/L)')
adgb.set_title("Shafer: Chl-a Recorded Distance from the Dam over Summer 2024")
adgb.set_ylim(0,90)
plt.savefig('ChlaSHAF.png', dpi = 400)
plt.show()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.scatterplot(x='TP BDL', y='Chla (Avg 24 and on)', data=df_ch) 
adgb.set_xlabel('TP BDL (ppm)')
adgb.set_ylabel('Average Chl-a Concentration (ug/L)')
adgb.set_title("TP vs. Chl-a (2023-2025)")
#plt.show()
'''

df_25_M = df_25[df_25['Lake ID (4 dig.)'] == 'MISS']
print(df_25_M)

plt.figure(figsize=(12,6)) #size of graph
sns.boxplot(x='Distance From Dam', y='Chla (Avg 24 and on)', data=df_25_M)
plt.show()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance From Dam', y='Chla (Avg 24 and on)', data=df_25_M, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Chl-a Concentration (ug/L)')
adgb.set_title("MISS Distance from Dam vs. Chla")
#adgb.set_ylim(0,90)
plt.savefig('ChlaM25.png', dpi = 400)
plt.show()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.scatterplot(x='TP BDL', y='Chla (Avg 24 and on)', data=df_25_M) 
adgb.set_xlabel('TP BDL (ppm)')
adgb.set_ylabel('Average Chl-a Concentration (ug/L)')
adgb.set_title("TP vs. Chl-a (2023-2025)")
plt.savefig('TP_chla_M25.png', dpi = 400)
plt.show()

