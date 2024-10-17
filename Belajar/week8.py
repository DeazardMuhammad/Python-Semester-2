# Numpy -> Numerical Python
import numpy as np # np terserah ganti apa

#############
print("Dimensi 1\n")
arr = np.array([8,3,5,1])
arr_sort = np.sort(arr)
f = []
# for el in arr:
#     if el > 2:
#         f.append(True)
#     else:
#         f.append(False)
# filter_f = arr[f]

# Untuk Genap
for el in arr:
    if (el % 2 == 0):
        f.append(True)
    else:
        f.append(False)
filter_f = arr[f]

print(arr)
print("Data arr ->", arr[3])
print(arr_sort)
print("Data arr_sort ->", arr_sort[3])
print(f)
print("Cek Filter:", f)
print("Hasil Filter:", filter_f)

#############
print("\nDimensi 3\n")
arr3 = np.array([
                [[1,2,3], ["a","b","c"]], 
                [[4,5,6], ["x","y","z"]]
                ])

print(arr3.ndim)
print(arr3[1][1][2])
print(arr3[1][0][1])
print(arr3[0][1][2])
# buat data yang paling terakhir
print(arr3[-1]) 
print(arr3[-1][-1])
print(arr3[-1][-1][-1])
print(arr3[-2])
 

