listMakanan = ["Puan", "Deazard", "Riefani"]
print("pilih menu: ")
print("1. tambah data")
print("2. hapus data terakhir")
kategori = int(input("Pilih Kategori: "))

if kategori == 1:
    menu = input("Input Data: ")
    listMakanan.append(menu)

if kategori == 2:
    listMakanan.pop()
    
print(listMakanan)