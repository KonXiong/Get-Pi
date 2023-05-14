import random
import numpy as np
from time import perf_counter
from multiprocessing.dummy import Pool as ThreadPool

# define the Gaussian Function
def gaussian(x):
    return (np.exp(-x**2))

# random throw dot and analyze
def simulate_dot_throwing(xmin, xmax, ymin, ymax):
    global dot_in_area 
    x,y = random.uniform(xmin,xmax),random.uniform(ymin,ymax)
    if y < gaussian(x):
        dot_in_area = dot_in_area + 1
    return 0
    

# counting program duration
start = perf_counter()

# initialize the dot
dot_num = 100000000
dot_in_area = 0.0

# initialize the boundary
xmin = 0
xmax = 10
ymin = 0
ymax = 1

# Parallel Operation(error)
# pool = ThreadPool(4)
# pool.map(simulate_dot_throwing(xmin, xmax, ymin, ymax), range(1, dot_num))
# pool.close()
# pool.join()

# Serial Operation
for ind in range(1,dot_num):
   simulate_dot_throwing(xmin, xmax, ymin, ymax) 

# calculate the result of Pi
problem_space_square = (xmax - xmin) * (ymax - ymin)
dot_in_area_ratio = dot_in_area / dot_num
dot_in_area_square = dot_in_area_ratio * problem_space_square
PI = (dot_in_area_square * 2) ** 2

duration = perf_counter() - start

print(f'PI 的值为 : {PI}')
print("the duration is {:.5f}s".format(duration))

