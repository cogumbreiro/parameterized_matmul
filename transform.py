#!/usr/bin/env python3

#import transloopy

# For learning
import itertools
import numpy as np
from sklearn.preprocessing import normalize

# For Bayesian optimization
from skopt import gbrt_minimize
minimize = gbrt_minimize

# For code-transformation
from typing import Sequence, Callable, List, Any
import json
from collections import OrderedDict
from random import randint
import pathlib

class CompileAndRun:
    def __init__(self, fname, transf, run):
        self.fname = fname
        self.transf = transf
        self.run = run
    
    def __call__(self, args):
        self.transf(self.fname, *args)
        return self.run(self.fname)

SAMPLE_COUNT = 1000

def main(domain, transf, run): 
    import argparse, csv
    parser = argparse.ArgumentParser(description='Generates a file with profiling parameters and multiple loopy transformation files.')
    parser.add_argument('-t', dest='filename', help='Template for the transformation filename output.', default="params.json")
    parser.add_argument('-s', dest='sample_count', help='The number of samples being generated', default=SAMPLE_COUNT, type=int)
    opts = parser.parse_args()
    
    runner = CompileAndRun(opts.filename, transf, run)
    res = minimize(runner,
        domain,
        #acq_func="EI",
        n_calls=opts.sample_count,
        #noise=0.1**1,
        verbose=True)
    
    params = res.x

    transf(opts.filename, *params)
    print("Wrote: " + opts.filename)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

