import numpy as np 

# 1 Dimensi
# arr = np.array([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) 

# 2 Dimensi
# arr = np.array([
#                 [3, 2, 1], 
#                 [6, 5, 4]
#                 ])

# 3 Dimensi
# arr = np.array([
#     [[3, 2, 1], [6, 5, 4]],
#     [["a","b","c"], ["x","y","z"]]
#     ])

# newarr = arr.reshape(2, 3, 2)
# print(newarr)

# Random
arr = np.random.randint(1, 12, 100)

# 1 Dimensi
print(arr)
print(arr[5])
# for cetak in arr:
#     print(cetak)
# for cetak in range(7):
#     print(arr[cetak])


# 2 Dimensi
# for loop_1 in arr:
#     for loop_2 in loop_1:
#         print(loop_2)

# # 3 Dimensi
# for loop_1 in arr:
#     for loop_2 in loop_1:
#         for loop_3 in loop_2:
#             print(loop_3)

# print("Array Dimensi:", arr.shape)