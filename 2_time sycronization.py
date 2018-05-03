# -*- coding: utf-8 -*-
"""
Sycronize time for each trial
"""

import os
import pandas as pd


timesycronization = pd.read_csv('YOUR \\PATH\\TO \\SMI-Eye-Tracking-Data-Analysis\\time syncronization.csv')

os.chdir('YOUR \\PATH\\TO\\SMI-Eye-Tracking-Data-Analysis\\2.Exported trials\\')

outputpath = 'YOUR \\PATH\\TO\\SMI-Eye-Tracking-Data-Analysis\\3.Sycronized data\\'

for file in os.listdir():
    df = pd.read_csv(file)
    
    name = file.split('.')[0]
    
    index = list(timesycronization.iloc[:,0]).index(name)
    

    
    df.iloc[:,0] = (df.iloc[:,0] - df.iloc[0,0])/1000
    
    df2 = df[(df.iloc[:,0] >timesycronization['start time'][index]) & (df.iloc[:,0] < timesycronization['end driving time'][index])]
    df2.iloc[:,0] = df2.iloc[:,0] - timesycronization['start time'][index]
    
    df2.to_csv(outputpath +file ,index = False)
    print('file name {} is output'.format(file))
    
    
