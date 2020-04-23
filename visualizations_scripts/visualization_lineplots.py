#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[151]:


covid = pd.read_csv('/Users/yunyaozhu/Desktop/covid19-master/out.csv')
covid['date'] = pd.DatetimeIndex(covid['publish_time']).day


# In[81]:


sorted_dates = sorted(covid['publish_time'].unique())
sorted_dates = sorted_dates[:-11] # remove dates beyond 4/11/20


# In[82]:


rows = []
for date in sorted_dates:
    
    tmp_df = covid[covid['publish_time']==date]
    
    tmp_areas = tmp_df[tmp_df.columns[8:16]]
    tmp_sum = tmp_areas.sum(axis=0)
    rows.append(np.array(tmp_sum))
date_sum_df = pd.DataFrame(rows)

date_sum_df['date'] = sorted_dates

date_sum_df = date_sum_df.rename(columns={0: "virus_origin", 1: "transmission",
                   2: "risk_factors",
                  3: "medical_care", 
                  4: "diagnostics_surveillance", 
                  5: "therapeutics", 
                  6: "social_ethical", 
                  7: "inventions"})


# In[83]:


area_names = ['virus_origin', 'transmission', 'risk_factors', 'medical_care',
       'diagnostics_surveillance', 'therapeutics', 'social_ethical',
       'inventions']


# In[154]:


fig, ax = plt.subplots(figsize=(20, 8))
for area in area_names:
    plt.plot(date_sum_df['date'], date_sum_df[area], '-')
    plt.legend(area_names)
    plt.title("Trend in number of scholarly articles over time in 2020")
    plt.xticks(['2020-01-01',
               '2020-02-01', 
               '2020-03-01', 
               '2020-04-01'], rotation=0)


# In[157]:


fig, ax = plt.subplots(figsize=(20, 8))
for area in ['virus_origin', 'transmission', 
       'diagnostics_surveillance', 
       'inventions']:
    plt.plot(date_sum_df['date'], date_sum_df[area], '-')
    plt.legend(['virus_origin', 'transmission', 
       'diagnostics_surveillance', 
       'inventions'])
    plt.title("Trend in number of scholarly articles over time in 2020")
    plt.xticks(['2020-01-01',
               '2020-02-01', 
               '2020-03-01', 
               '2020-04-01'], rotation=0)


# In[158]:


fig, ax = plt.subplots(figsize=(20, 8))
for area in ['virus_origin', 'transmission', 
       'diagnostics_surveillance', 
       'inventions']:
    plt.plot(date_sum_df['date'], date_sum_df[area], 'o')
    plt.legend(['virus_origin', 'transmission', 
       'diagnostics_surveillance', 
       'inventions'])
    plt.title("Trend in number of scholarly articles over time in 2020")
    plt.xticks(['2020-01-01',
               '2020-02-01', 
               '2020-03-01', 
               '2020-04-01'], rotation=0)


# In[159]:


import datetime 

d10 = datetime.datetime(2020, 1, 1) 
d11 = datetime.datetime(2020, 1, 11) 
d12 = datetime.datetime(2020, 1, 21) 

d20 = datetime.datetime(2020, 2, 1) 
d21 = datetime.datetime(2020, 2, 11) 
d22 = datetime.datetime(2020, 2, 21) 

d30 = datetime.datetime(2020, 3, 1) 
d31 = datetime.datetime(2020, 3, 11) 
d32 = datetime.datetime(2020, 3, 21) 

d40 = datetime.datetime(2020, 4, 1) 
d41 = datetime.datetime(2020, 4, 11)
d42 = datetime.datetime(2020, 4, 21)


# In[160]:


selected_dates = [d10, d11, d12, d20, d21, d22, d30, d31, d32, d40, d41, d42]
rows = []
for i in range(len(selected_dates)-1):
    
    date1 = selected_dates[i]
    date2 = selected_dates[i+1]
    tmp_df = covid[(pd.DatetimeIndex(covid['publish_time'])>=date1) & (pd.DatetimeIndex(covid['publish_time'])<date2)]
    
    tmp_areas = tmp_df[tmp_df.columns[8:16]]
    tmp_sum = tmp_areas.sum(axis=0)
    rows.append(np.array(tmp_sum))
selected_date_sum_df = pd.DataFrame(rows)

selected_date_sum_df['date'] = ['01.01-01.10', 
                       '01.11-01.20',
                       '01.21-01.31',
                      '02.01-02.10', 
                       '02.11-02.20',
                       '02.21-02.29',
                        '03.01-03.10', 
                       '03.11-03.20',
                       '03.21-03.31',
                       '04.01-04.10',
                       '04.11-04.17']
selected_date_sum_df = selected_date_sum_df.rename(columns={0: "virus_origin", 1: "transmission",
                   2: "risk_factors",
                  3: "medical_care", 
                  4: "diagnostics_surveillance", 
                  5: "therapeutics", 
                  6: "social_ethical", 
                  7: "inventions"})


# In[161]:


fig, ax = plt.subplots(figsize=(20, 8))
for area in area_names:
    plt.plot(selected_date_sum_df['date'], selected_date_sum_df[area], '-')
    plt.legend(area_names)
    plt.title("Trend in number of scholarly articles over time in 2020")


# In[162]:


fig, ax = plt.subplots(figsize=(20, 8))
for area in ['virus_origin', 'transmission', 
       'diagnostics_surveillance', 
       'medical_care']:
    plt.plot(selected_date_sum_df['date'], selected_date_sum_df[area], '-')
    plt.legend(['virus_origin', 'transmission', 'diagnostics_surveillance', 'medical_care'])
    plt.title("Trend in number of scholarly articles over time in 2020")
    
    ax.axvline(x='01.21-01.31', linewidth=0.5, color='lightgray')
    plt.text('01.21-01.31', 55,'01.30.2020\nWHO declared global\nhealth emergency', color='gray', fontsize=13)
    
    ax.axvline(x='02.11-02.20', linewidth=0.5, color='lightgray')
    plt.text('02.11-02.20', 75,'02.14.2020\nFirst coronavirus\ndeath in Europe', color='gray', fontsize=13)
    
    ax.axvline(x='02.21-02.29', linewidth=0.5, color='lightgray')
    plt.text('02.21-02.29', 100,'02.24.2020\nUS: $1.25 billion for\ncoronavirus response', color='gray', fontsize=13)
    
    ax.axvline(x='03.11-03.20', linewidth=0.5, color='lightgray')
    plt.text('03.11-03.20', 150,'03.13.2020\nUS: national\nemergency', color='gray', fontsize=13)

    ax.axvline(x='03.21-03.31', linewidth=0.5, color='lightgray')
    plt.text('03.21-03.31', -5,'03.23.2020\nBritain lockdown\n\n03.24.2020\nIndia lockdown\n\n03.30.2020\nUS: More states\nissue stay-at-home\ndirectives', color='gray', fontsize=13)

    ax.axvline(x='04.01-04.10', linewidth=0.5, color='lightgray')
    plt.text('04.01-04.10', 170,'04.10.2020\nGlobal deaths\nsurpass 101,000', color='gray', fontsize=13)

