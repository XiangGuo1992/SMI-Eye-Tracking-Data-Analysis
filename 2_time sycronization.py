# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 20:07:07 2018

@author: Inki Kim's lab
"""

import os
import pandas as pd


timesycronization = pd.read_csv('C:\\Users\\Inki Kim\'s lab\\Documents\\GitHub\\SMI-Eye-Tracking-Data-Analysis\\time syncronization.csv')

os.chdir('C:\\Users\\Inki Kim\'s lab\\Documents\\GitHub\\SMI-Eye-Tracking-Data-Analysis\\2.Exported trials\\')

outputpath = 'C:\\Users\\Inki Kim\'s lab\\Documents\\GitHub\\SMI-Eye-Tracking-Data-Analysis\\3.Sycronized data\\'

for file in os.listdir():
    df = pd.read_csv(file)
    
    name = file.split('.')[0]
    
    index = list(timesycronization.iloc[:,0]).index(name)
    

    
    df.iloc[:,0] = (df.iloc[:,0] - df.iloc[0,0])/1000
    
    df2 = df[(df.iloc[:,0] >timesycronization['start time'][index]) & (df.iloc[:,0] < timesycronization['end driving time'][index])]
    df2.iloc[:,0] = df2.iloc[:,0] - timesycronization['start time'][index]
    
    df2.to_csv(outputpath +file ,index = False)
    print('file name {} is output'.format(file))
    
    