#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:30:58 2020

@author: JessieOU
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import re 

covid_2020 = df = pd.read_csv('/Users/JessieOU/covid19/out.csv')

# sum paper_count by month and aggregate for each research_category 
summarize = covid_2020.groupby(['month']).agg({
    'virus_origin': 'sum', 
    'transmission': 'sum',
    'risk_factors': 'sum',
    'medical_care': 'sum',
    'diagnostics_surveillance': 'sum',
    'therapeutics': 'sum',
    'social_ethical': 'sum',
    'inventions': 'sum'})

print(summarize.head(4))
print(type(summarize))

# slice to month 1-4 
summarize_head = summarize.head(4)

## Plotting
plot = summarize_head.plot(kind = 'bar', title='Research Paper Count by Category Per Month')
plot.set_xlabel("month in 2020")
plot.set_ylabel("Number of Published Research Papers")
plot.figure.savefig('barplot.png')



stacked = summarize_head.plot(kind='bar', stacked=True, sort_columns = True, title='Research Paper Proportion by Category Per Month', figsize=[20,10])
stacked.set_ylabel("month in 2020")
stacked.set_xlabel("Percentage of Published Research Papers")
stacked.figure.savefig('stackedplot.png')

# Change: groupby state_office and divide by sum
# summarize_pcts = summarize_head.groupby(level=0).apply(lambda x:
                                             #    100 * x.astype(float) / float(x.sum()))
# fractions = summarize_head / summarize_head.groupby(level=0).sum()
# print(fractions)
column_list = list(summarize_head)
summarize_head["sum"] = summarize_head[column_list].sum(axis=1)
print(summarize_head)

origin_list = list(summarize_head['virus_origin'])
transmission_list = list(summarize_head['transmission'])
diag_list = list(summarize_head['diagnostics_surveillance'])
medical_list = list(summarize_head['medical_care'])
intervention_list = list(summarize_head['inventions'])


origin_prop = [] 
for i in range(0, 4): 
    prop = origin_list[i]/ summarize_head['sum'].iloc[i]
    origin_prop.append(prop)
summarize_head['origin_prop'] = origin_prop


transmission_prop = [] 
for i in range(0, 4): 
    prop = transmission_list[i]/ summarize_head['sum'].iloc[i]
    transmission_prop.append(prop)
summarize_head['transmission_prop'] = transmission_prop

diag_prop = [] 
for i in range(0, 4): 
    prop = diag_list[i]/ summarize_head['sum'].iloc[i]
    diag_prop.append(prop)
summarize_head['diag_prop'] = diag_prop


medical_prop = [] 
for i in range(0, 4): 
    prop = medical_list[i]/ summarize_head['sum'].iloc[i]
    medical_prop.append(prop)
summarize_head['medical_prop'] = medical_prop

intervention_prop = [] 
for i in range(0, 4): 
    prop = intervention_list[i]/ summarize_head['sum'].iloc[i]
    intervention_prop.append(prop)
summarize_head['intervention_prop'] = intervention_prop

print(summarize_head.shape)


propdf = summarize_head.iloc[0:4, 9:15]


prop_plot = propdf.plot(kind='bar', stacked=True, sort_columns = True, title='Research Paper Category Composition by Month', figsize=[20,10], legend = False)
prop_plot.set_xlabel("month in 2020")
prop_plot.set_ylabel("Proportion of Published Research Papers")
patches, labels = prop_plot.get_legend_handles_labels()
prop_plot.legend(patches, labels, loc='best')
prop_plot.figure.savefig('prop_plot.png')


