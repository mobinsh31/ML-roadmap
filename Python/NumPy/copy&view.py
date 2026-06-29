"""
NumPy Copy vs View Practice

Author: Mobina Shokouhi
Topic: Copy vs View
Date: 2026-06-29
"""

import numpy as np

# Exercise 1 - copy()

original_array = np.array([1, 2, 3])
copied_array = original_array.copy()
copied_array[1] = 100

print( original_array)
print(copied_array)


# Exercise 2 - view()

original_array = np.array([1, 2, 3])
view_array = original_array.view()
view_array[1] = 100

print( original_array)
print( view_array)




"""
What I learned

1.any changes made to the original array will not affect the copy.it is a Independent Memory
2.view() shares memory with the original array.
3.
# copy()

#arr  ─────► [1][2][3]

#copy_arr ─► [1][2][3]



#view()

#arr ───────────────► [1][2][3]
 #                      ▲
  #                     │
#view_arr ──────────────┘

"""