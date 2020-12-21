# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:34:04 2020

@author: ahino

Read in the results of the complicated multi-processing calculations
"""

import numpy as np
import pandas as pd

num_runs =  20
folder = 'results/'

# loop through the files and get the results
results = []
for i in range(num_runs):
    file_name = folder+'run_'+str(i)+'.txt'
    res = np.loadtxt(file_name)
    results.append(res)
    
resultsPD = pd.DataFrame({'results': results})
resultsPD.to_csv('results.csv')