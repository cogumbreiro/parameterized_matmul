#!/usr/bin/env python3

from subprocess import check_output, call, STDOUT
import os
import json
import transform

DOMAIN = [(2,128), (2,128), (2,128)]

def codegen(filename, i, j, k):
    with open(filename, "w") as fp:
        row = dict(i=int(i), j=int(j), k=int(k))
        json.dump(row, fp)

def run(filename):
    with open(filename) as fp:
        params = json.load(fp)
    cmd = "clang++ -std=c++11 -O3 -DTILE0={i} -DTILE1={j} -DTILE2={k} matmul.cpp -o matmul"
    os.system(cmd.format(**params))
    p = check_output(["./matmul","1024"])
    elapsed = float(p.decode("utf-8").split("nodes/s")[0])
    print(params, elapsed)
    return elapsed

if __name__ == '__main__':
    transform.main(DOMAIN, codegen, run)

