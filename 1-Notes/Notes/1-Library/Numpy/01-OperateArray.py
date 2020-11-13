import numpy as np
a = [1, 2, 3, 4]
b = [10, 11, 12, 13]
a_array = np.array([1, 2, 3, 4])
b_array = np.array([10, 11, 12, 13])
print('--- + ---')
print(a+b)
print(a_array+b_array)

print('--- * ---')
print(a_array*b_array)

print('--- / ---')
print(a_array/b_array)

print('--- ** ---')
print(a_array**b_array)

print('--- sin ---')
print(np.sin(a_array))

print('--- log ---')
print(np.log(a_array))
