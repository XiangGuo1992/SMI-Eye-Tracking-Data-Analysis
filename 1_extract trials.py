# -*- coding: utf-8 -*-
"""
extract different trials from raw .txt data
"""

import os
import pandas as pd
import numpy as np


os.chdir('YOUR\\PATH\\TO \\SMI-Eye-Tracking-Data-Analysis\\1.Raw txt data\\')

outputpath = 'YOUR\\PATH\\TO \\SMI-Eye-Tracking-Data-Analysis\\2.Exported trials\\'

for file in os.listdir():
    df = pd.read_table(file)
    trials = np.unique(df['Stimulus'])
    for trial in trials:
        df2 = df[df['Stimulus']==trial]    
        df2.to_csv(outputpath + trial.split('.')[0] +'.csv',index = False)
        print('file name {} is output'.format(trial))
        
