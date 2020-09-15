#CalPi.py
from random import random
from time import perf_counter
total = 1000*1000
hits = 0
start = perf_counter()
for i in range(1,total+1):
    x,y = random(),random()
    dist = x**2 + y**2
    if dist < 1 :
        hits += 1
pi = 4 * (hits/total)
print("圆周率：{}".format(pi))
print("time：{:.5f}".format(perf_counter()-start))
