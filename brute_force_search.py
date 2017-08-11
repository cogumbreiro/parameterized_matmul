
import os
import time
from subprocess import check_output,call


tilerange=[2,4,8,16,32,64,128]
#tilerange=[2,4]

for t0 in tilerange:
  for t1 in tilerange:
    for t2 in tilerange:
      os.system("clang++ -std=c++11 -O3 -DTILE0={} -DTILE1={} -DTILE2={} matmul.cpp -o matmul".format(t0,t1,t2))
      p=check_output(["./matmul","256"])
      tm=float(p.decode("utf-8").split("nodes/s")[0])
      print("{},{},{},{}".format(t0,t1,t2,tm))
