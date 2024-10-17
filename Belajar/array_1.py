import array as Dea
var_Dea = Dea.array('d',[1.3, 2.4 ,3.1 ,4.8 ,5.2,6.2,7.9])
var_Dea.append(8.3)
var_Dea[2] = 3.5
del(var_Dea[0])
print("Isi dari var_Dea")
for i in range(5):
    print(var_Dea[i], end=" ")
print()

print("Element Terakhir: ", var_Dea[1])

print("Slicing 1: ", var_Dea[2:4])
print("Slicing 2: ", var_Dea[:-3])
print("Slicing 3: ", var_Dea[5:])
print("Slicing 4: ", var_Dea[:])
