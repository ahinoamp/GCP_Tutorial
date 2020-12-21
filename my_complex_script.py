# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:26:16 2020

@author: ahino

An example of a simple function that takes input from a dictionary and runs
some very lengthy calculations 
"""

import numpy as np
import time

def very_long_func(input_dictionary):
    
    # get the input
    x = input_dictionary['x']
    y = input_dictionary['y']
    z = input_dictionary['z']
    i = input_dictionary['run_n']
    folder = input_dictionary['folder']
    
    # do the calculation    
    calc = [x*y*z]
    
    # save to a file numbered by the thread
    fname=folder+'run_'+str(i)+'.txt'
    np.savetxt(fname, calc)
    
    # wait a little so we can pretend this is a calculation that takes days
    time.sleep(3)
    
if __name__== "__main__":

    params = {}
    params['x']=5
    params['y']=2    
    params['z'] = 1
    params['folder'] = 'results/'        
    params['run_n'] = 1
    very_long_func(params)    
    
    
    
