print("=== Perpustakaan ===")
print(" 1. Lihat Daftar Buku ")
print(" 2. Tambah Buku ")
print(" 3. Hapus Buku ")
print(" 4. Edit Buku ")
print(" 5. Cari Buku ")
print(" 6. Keluar ")

buku = []

def listBuku():
    print("\nDaftar Buku:")
    if not buku:
        print("Tidak ada buku dalam perpustakaan.")
    else:
        nomorID = 1
        for judul in buku:
            print(f"{nomorID}. {judul}")
            nomorID += 1

def addData():
    judul = input("\nMasukkan judul buku: ")
    buku.append(judul)
    print(f"Buku '{judul}' berhasil ditambahkan.")

def deleteData():
    listBuku()
    if not buku:
        print("Tidak ada buku dalam perpustakaan.")
        return
    
    nomorID = input("\nPilih nomor buku yang ingin dihapus: ")
    if not nomorID.isdigit():
        print("Masukkan nomor buku yang valid.")
        return

    nomorID = int(nomorID) - 1
    if 0 <= nomorID < len(buku):
        bukuTerhapus = buku.pop(nomorID)
        print(f"Buku '{bukuTerhapus}' berhasil dihapus.")
    else:
        print("Nomor buku tidak valid.")

def editData():
    listBuku()
    if not buku:
        print("Tidak ada buku dalam perpustakaan.")
        return

    nomorID = input("\nPilih nomor buku yang ingin diedit: ")
    if not nomorID.isdigit():
        print("Masukkan nomor buku yang valid.")
        return

    nomorID = int(nomorID) - 1
    if 0 <= nomorID < len(buku):
        judulBaru = input("Masukkan judul baru: ")
        buku[nomorID] = judulBaru
        print("Judul buku berhasil diubah.")
    else:
        print("Nomor buku tidak valid.")

def searchData():
    if not buku:
        print("Tidak ada buku dalam perpustakaan.")
        return

    kataKunci = input("\nMasukkan kata kunci pencarian: ")
    CariBuku = []
    nomorID = 1
    for judul in buku:
        if kataKunci.lower() in judul.lower():
            CariBuku.append((nomorID, judul))
        nomorID += 1

    if CariBuku:
        print("\nHasil pencarian:")
        for nomorID, judul in CariBuku:
            print(f"{nomorID}. {judul}")
    else:
        print("Buku tidak ditemukan berdasarkan kata kunci tersebut.")

def main():
    while True:
        pilihan = input("\nMasukkan pilihan menu: ")

        if pilihan == '1':
            listBuku()
        elif pilihan == '2':
            addData()
        elif pilihan == '3':
            deleteData()
        elif pilihan == '4':
            editData()
        elif pilihan == '5':
            searchData()
        elif pilihan == '6':
            print("Program selesai, terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.")

main()
