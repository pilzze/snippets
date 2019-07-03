from random import random
import ctypes
import time

st = time.process_time()
Nsos, sos = 0, 0
for i in range(100000):
	x, y = random(), random()
	if x**2+y**2<=1:
		Nsos += 1
	sos += 1
print(Nsos/sos*4.)
e = time.process_time()
print(e-st)

st = time.process_time()
nsos, sos = ctypes.c_int(0), ctypes.c_int(0)
pyarr = range(100000)
arr = (ctypes.c_int * len(pyarr))(*pyarr)
for i in pyarr:
	x, y = ctypes.c_float(random()), ctypes.c_float(random())
	if x.value*x.value+y.value*y.value<=1:
		nsos.value += 1
	sos.value += 1
print(nsos.value/sos.value*4.)
e = time.process_time()
print(e-st)
