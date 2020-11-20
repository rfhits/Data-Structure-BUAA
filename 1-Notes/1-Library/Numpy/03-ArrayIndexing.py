import numpy as np
a = np.array([-3, -2, -1, 0, 1, 2, 3])
negetives = a > 0
print(type(negetives))
print(negetives)
mask_list = list(negetives)
print(a[negetives])
print(a[mask_list])
print(a[a > 0])
# 多次使用，可以定义这个mask，只用一次，直接在[]里写
print("change elements by mask")
a[a < 0] = 0
print(a)
and_array = (a > 0) & (a < 2)
print(and_array)
