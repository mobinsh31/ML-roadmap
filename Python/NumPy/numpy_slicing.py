"""
NumPy slicing Practice

Author: Mobina Shokouhi
Topic: NumPy Slicing
Date: 2026-06-28
"""

import numpy as np

# Exercise 1

array = np.array([10,20,30,40,50,60,70])
print(array[1:4])

# Exercise 2
arr_1 = np.array([5,10,15,20,25,30,35,40])
print(arr_1[-4:])

# Exercise 3

arr_2 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr_2[1::2])

# Exercise 4

arr_3 = np.array([100,200,300,400,500,600])
print(arr_3[-1:-4:-1])

# Exercise 5

arr_4 = np.array([1,2,3,4,5,6,7,8,9])
print(arr_4[::-2])