from numba import jit
import numpy as np
import time

# A simple function to add two arrays
@jit(nopython=True)
def add_arrays(a, b):
    return a + b

# Create two random arrays
a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Measure the time for the addition
start = time.time()
c = add_arrays(a, b)
end = time.time()

print("Time taken:", end - start)
print("First 10 elements of the result:", c[:10])
