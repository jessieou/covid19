#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:34:31 2020

@author: JessieOU
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import re 


df = pd.read_csv('/Users/JessieOU/Documents/datafest_covid19_processed.csv', encoding = "ISO-8859-1")

df_pd = pd.DataFrame(df, columns = df.columns)
print(df_pd.shape)



# extract month and year from publish_time 
# add month and year columuns to end of dataframe 
months = []
years = [] 
# convert all values in publish_time to string 
df_pd['publish_time'] = df_pd['publish_time'].astype(str)
for date in df_pd['publish_time']:
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        validate = True 
    except ValueError:
       # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        validate = False 
    if validate: 
        # convert from string to datetimeo objects 
        date_object = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        months.append(date_object.month)
        years.append(date_object.year)
    else:
        months.append('na')
        years.append('na')
        
df_pd['month'] = months
df_pd['year'] = years
print(df_pd.year.unique())

## Reduce literature set to include those mentioning Covid 19 or its synonyms. 
## Does paper discuss Covid-19, SARS, MERS, etc.? Looking for papers that specifically refer to the recent outbreak, 
## known variously as Covid-19, SARS-CoV-2, 2019-nCoV, Wuhan Pneumonia etc.
## list provided by Kaggle Kernel Covid-19 Project - Medical Tasks 
covid19_synonyms = ['covid','coronavirus disease 19','sars cov 2','2019 ncov','2019ncov',r'2019 n cov\b', r'2019n cov\b',
                    'ncov 2019',r'\bn cov 2019','coronavirus 2019','wuhan pneumonia','wuhan virus','wuhan coronavirus',
                    r'coronavirus 2\b']

relevant_list = []
# convert all values in abstract to string 
df_pd['abstract'] = df_pd['abstract'].astype(str)
for abstract in df_pd['abstract']:
    match = 0
    for keyword in covid19_synonyms:
        if re.search(keyword, abstract):
            match +=1
            

    relevant_list.append(match)
df_pd['relevant'] = relevant_list

# filter to only covid19 relevant 
is_covid = df_pd['relevant'] > 0
df_covid = df_pd[is_covid]
print(df_covid.shape) # (2918, 18)

# further filter to 2019 
# covid_2019 = df_covid[df_covid.year.eq(2019)]
# print(covid_2019.shape) #(0, 18)?


# further filter to year == 2020  
covid_2020 = df_covid[df_covid.year.eq(2020)]
print(covid_2020.shape) #(2592, 18)

# from now on, use covid_2020 dataframe 
# write out this dataset to a csv file 
covid_2020.to_csv('out.csv')



   



