"""
NumPy Indexing Practice

Author: Mobina Shokouhi
Topic: NumPy Indexing
Date: 2026-06-28
"""

import numpy as np

# Exercise 1

arr = np.array([12, 25, 37, 49, 58, 63, 71])
print(arr[3])

# Exercise 2

print(arr[-1])

# Exercise 3

arr_1 = np.array([5, 10, 15, 20, 25])
arr_1[2] = 100
print(arr_1)

# Exercise 4

arr_2 = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr_2[2,1])

# Exercise 5

arr_3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_3[2,-1])
