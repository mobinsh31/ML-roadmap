"""
NumPy Data Types Practice

Author: Mobina Shokouhi
Topic: Data types
Date: 2026-06-29
"""

import numpy as np

# Exercise 1

array = np.array([10,20,30,40,50])
print(array.dtype)

# Exercise 2
array_1 = np.array([2.5,4.8,7.2,9.1])
new_array_1 = array_1.astype(int)
print(new_array_1)
print(new_array_1.dtype)

# Exercise 3

array_2 = np.array([1,2,3,4,5], dtype='float')
array_2.astype(int)
print(array_2)

# Exercise 4

array_3 = np.array([1.9,2.8,3.7])
array_3.astype(int)
print(array_3)

# Exercise 5

array_4 = np.array([10,20,30,40])
new_array_4 = array_4.astype('float64')
print(new_array_4[0])
print(new_array_4)
print(new_array_4.dtype)
print(array_4.dtype)


