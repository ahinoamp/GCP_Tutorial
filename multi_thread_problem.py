# -*- coding: utf-8 -*-
"""
Created Dec 20, 2020

@author: ahinoamp

Send many threads to different CPUs and vary the hyper parameters
according to different distributions.
This is taken from a stack overflow answer that unfortunately I can no longer
find in order to give proper credit :-(
"""

import multiprocessing
import numpy as np
import my_complex_script as complex_func
import pandas as pd

class Predictor(multiprocessing.Process):
    def __init__(self, input_queue, output_queue, cpu_id):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.cpu_id = cpu_id

    def run(self):
        while True:
            input = self.input_queue.get()
            if input is None:
                self.input_queue.task_done()
                self.output_queue.put("Finished with processor %d" % self.cpu_id)
                break
            else:
                try:
                    complex_func.very_long_func(input)
                    self.input_queue.task_done()
                    self.output_queue.put('complete - run #'+str(input['run_n'])+' on cpu#'+str(self.cpu_id))
                except Exception:
                    self.input_queue.task_done()
                    self.output_queue.put('There was an exception- run #'+str(input['run_n'])+'on cpu#'+str(self.cpu_id))
        return

if __name__ == "__main__":
      
    ##############################################
	## Change code below
	##############################################

    # decide on the number of tasks
    num_runs =  20
    num_cpus = 2
    
    # create the variable input data
    x = np.random.rand(num_runs, )
    y = np.random.rand(num_runs, )
    z = np.random.rand(num_runs, )

    # create a list of tasks
    # every task is a dictionary with the input parameters
    tasks = []
    
    for i in range(num_runs):
        params = {}       
        params['run_n'] = i
        params['x'] = x[i]
        params['y'] = y[i]
        params['z'] = z[i]
        params['folder'] = 'results/'
        tasks.append(params)

    # save to file for your records
    input_data = pd.DataFrame({'x': x, 'y':y, 'z': z})
    input_data.to_csv('input_data.csv')

    ##############################################
	## Change code above
	##############################################
    
    # create num_cpus process objects and connect to an input and output que
    # the process will take tasks out of the input que and put results 
    # into the output que
    p_list = []
    input_queue = multiprocessing.JoinableQueue()
    output_queue = multiprocessing.Queue()
    for i in range(num_cpus):
        p = Predictor(input_queue, output_queue, i)
        p_list.append(p)

    # put all the tasks in the input que
    for task in tasks:
        input_queue.put((task))

    # start running all the processes
    for p in p_list:
        p.start()

    # put into the input que a list of "None" in the end, 
    # so that the CPUs can know to stop running when they finish all the 
    # tasks we want them to do    
    for i in range(num_cpus):
        input_queue.put(None)

    
    for i in range(len(tasks)+num_cpus):
        print(output_queue.get())

    # wait until processes are finished 
    input_queue.join()

    # wait until processes are finished 
    for p in p_list:
        p.join()