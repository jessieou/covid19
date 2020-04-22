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

covid_2020 = df = pd.read_csv('/Users/JessieOU/Documents/out.csv')

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