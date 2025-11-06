# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 13:04:31 2025
COntents: create graphics for Project
@author: Isaac Bradford, ibradfo@purdue.edu
Assistance: DK Yang
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

""" https://stackoverflow.com/questions/29779079/adding-a-scatter-of-points-to-a-boxplot-using-matplotlib """
#jitter plot

print('HAHAHA NEW ONE')

df_original = pd.read_csv('2023_2025_YSI_Included.csv') #open a csv within GH folder for data process.
df = df_original[df_original['Sampling Type (B/S)'] == 'Boat'] #boat only
df = df.replace('NaN', np.nan) #from DK replaces NaN with numpy NaN
df['Chla (Avg 24 and on)'] = df['Chla (Avg 24 and on)'].astype(np.float64) #sets type to float from DK
print (df.info())

df_M = df[df['Lake ID (4 dig.)'] == 'MISS']
df_M_mc = df_M.dropna(subset='Microcystin BDL') # making sure there iosn't any empty mc data included
df_M_ch = df_M.dropna(subset='Chla (Avg 24 and on)') # same but for chla

#print(df)
#https://www.geeksforgeeks.org/pandas/ways-to-filter-pandas-dataframe-by-column-values/
#filter data frames


"""DATA CHECKING"""

#2024 = 226 rows of data
df_23 = df[df['Year']<2024]
#print(df_23)
df_23_M = df_23[df_23['Lake ID (4 dig.)'] == 'MISS']
#print(df_24_M)

c_23 = df_23_M.dropna(subset='Chla (Avg 24 and on)')
Mc_23 = df_23_M.dropna(subset='Microcystin BDL')

#2025 = 108 rows of data
df_25 = df[df['Year']>2024]
#print(df_25)
df_25_M = df_25[df_25['Lake ID (4 dig.)'] == 'MISS']
#print(df_25_M)

c_25 = df_25_M.dropna(subset='Chla (Avg 24 and on)')
Mc_25 = df_25_M.dropna(subset='Microcystin BDL')
                
#2024 - 288 rows of data
df_24 = df[df['Year']==2024]
#print(df_24)
df_24_M = df_24[df_24['Lake ID (4 dig.)'] == 'MISS']
#print(df_24_M)

c_24 = df_24_M.dropna(subset='Chla (Avg 24 and on)')
Mc_24 = df_24_M.dropna(subset='Microcystin BDL')


"""Graphics"""

# 2025 Additional

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Date', y='Microcystin BDL', data=df_M_mc, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Date', rotation=45)
adgb.set_xlabel('Date')
adgb.set_ylabel('Microcystin Concentration (ug/L)')
adgb.set_title("2023-2025 Microcystin by Date")
adgb.set_ylim(0, 85)
plt.savefig('BoxMcM23-25.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Date', y='Chla (Avg 24 and on)', data=df_M_ch, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Date', rotation=45)
adgb.set_xlabel('Date')
adgb.set_ylabel('Chla Concentration (ug/L)')
adgb.set_title("2023-2025 Chla by Date")
adgb.set_ylim(0, 160)
plt.savefig('BoxCHLAM23-25.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()

# LOOK 2025
#
#
plt.figure(figsize=(12,6)) #space out recording
adgb = sns.scatterplot(x='Distance From Dam', y='Chla (Avg 24 and on)', data=c_25) 
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Average Chl-a Concentration (ug/L)')
adgb.set_title("Average Chl-a Recorded Distance from the Dam (2025)")
adgb.set_ylim(0,140)
plt.savefig('DfDChla_25.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()
plt.clf() #from DK clean figure

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.scatterplot(x='TP BDL', y='Chla (Avg 24 and on)', data=c_25) 
adgb.set_xlabel('TP BDL (ppm)')
adgb.set_ylabel('Average Chl-a Concentration (ug/L)')
adgb.set_title("TP v Avg Chla (2025)")
adgb.set_ylim(0,140)
adgb.set_xlim(0,1.1)
plt.savefig('TPvChla_25.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()
plt.clf()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance From Dam', y='Chla (Avg 24 and on)', data=c_25, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Distance from Dam', rotation=45)
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Chl-a Concentration (ug/L)')
adgb.set_title("Mississinewa: Chl-a Recorded Distance from the Dam over Summer 2025")
adgb.set_ylim(0,140)
plt.savefig('BoxChlaMISS25.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance From Dam', y='Microcystin BDL', data=Mc_25, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Distance from Dam', rotation=45)
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Microcystin Concentration (ug/L)')
adgb.set_title("Mississinewa: Microcystin Distance from the Dam over Summer 2025")
adgb.set_ylim(0, 40)
plt.savefig('BoxMcMISS25.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()

# LOOK 2024
#
#

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.scatterplot(x='Distance From Dam', y='Chla (Avg 24 and on)', data=c_24) 
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Average Chl-a Concentration (ug/L)')
adgb.set_title("Average Chl-a Recorded Distance from the Dam (2024)")
adgb.set_ylim(0,140)
plt.savefig('DfDChla_24.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()
plt.clf() #from DK clean figure

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.scatterplot(x='TP BDL', y='Chla (Avg 24 and on)', data=c_24) 
adgb.set_xlabel('TP BDL (ppm)')
adgb.set_ylabel('Average Chl-a Concentration (ug/L)')
adgb.set_title("TP v Avg Chla (2024)")
adgb.set_ylim(0,140)
adgb.set_xlim(0,1.1)
plt.savefig('TPvChla_24.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()
plt.clf()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance From Dam', y='Chla (Avg 24 and on)', data=c_24, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Distance from Dam', rotation=45)
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Chl-a Concentration (ug/L)')
adgb.set_title("Mississinewa: Chl-a Recorded Distance from the Dam over Summer 2024")
adgb.set_ylim(0,140)
plt.savefig('BoxChlaMISS24.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance From Dam', y='Microcystin BDL', data=Mc_24, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Distance from Dam', rotation=45)
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Microcystin Concentration (ug/L)')
adgb.set_title("Mississinewa: Microcystin Distance from the Dam over Summer 2024")
adgb.set_ylim(0, 40)
plt.savefig('BoxMcMISS24.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance From Dam', y='Microcystin BDL', data=Mc_24, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Distance from Dam', rotation=45)
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Microcystin Concentration (ug/L)')
adgb.set_title("Mississinewa: Microcystin Distance from the Dam over Summer 2024")
adgb.set_ylim(0, 5)
plt.savefig('SmallBoxMcMISS24.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()


# LOOK 2023
#
#

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.scatterplot(x='Distance From Dam', y='Chla (Avg 24 and on)', data=c_23) 
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Average Chl-a Concentration (ug/L)')
adgb.set_title("Average Chl-a Recorded Distance from the Dam (2023)")
adgb.set_ylim(0,140)
plt.savefig('DfDChla_23.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()
plt.clf() #from DK clean figure



plt.figure(figsize=(12,6)) #space out recording
adgb = sns.scatterplot(x='TP BDL', y='Chla (Avg 24 and on)', data=c_23) 
adgb.set_xlabel('TP BDL (ppm)')
adgb.set_ylabel('Average Chl-a Concentration (ug/L)')
adgb.set_title("TP v Avg Chla (2023)")
adgb.set_ylim(0,140)
adgb.set_xlim(0,1.1)
plt.savefig('TPvChla_23.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()
plt.clf()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance From Dam', y='Chla (Avg 24 and on)', data=c_23, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Distance from Dam', rotation=45)
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Chl-a Concentration (ug/L)')
adgb.set_title("Mississinewa: Chl-a Recorded Distance from the Dam over Summer 2023")
adgb.set_ylim(0,140)
plt.savefig('BoxChlaMISS23.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance From Dam', y='Microcystin BDL', data=Mc_23, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Distance from Dam', rotation=45)
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Microcystin Concentration (ug/L)')
adgb.set_title("Mississinewa: Microcystin Distance from the Dam over Summer 2023")
adgb.set_ylim(0, 40)
plt.savefig('BoxMcMISS23.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()

plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance From Dam', y='Microcystin BDL', data=Mc_23, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Distance from Dam', rotation=45)
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Microcystin Concentration (ug/L)')
adgb.set_title("Mississinewa: Microcystin Distance from the Dam over Summer 2023")
adgb.set_ylim(0, 5)
plt.savefig('SmallBoxMcMISS23.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()