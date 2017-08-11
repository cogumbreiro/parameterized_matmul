
import os
import time


tilerange=[2,4,8,16,32,64,128]
#tilerange=[2,4]

for t0 in tilerange:
  for t1 in tilerange:
    for t2 in tilerange:
      os.system("icpc -fopenmp -std=c++11 -O2 -DTILE0={} -DTILE1={} -DTILE2={} matmul.cpp -o matmul".format(t0,t1,t2))
      os.system("./matmul 2048")
      tm0=time.time()
      os.system("./matmul 2048")
      tm1=time.time()
      tm=tm1-tm0
      print("{},{},{},{}".format(t0,t1,t2,tm))
