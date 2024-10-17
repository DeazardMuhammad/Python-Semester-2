import numpy as np

data_siswa = {
    # BUAT LAH DICTIONARY DATA SISWA DISINI!!
    'Agus' : 70,
    'Budi' : 85,
    'Citra' : 90,
    'Dian' : 75,
    'Eka' : 60,
    'Fani' : 80,
    'Gina' : 95,
    'Hadi' : 88,
    'Indra' : 77,
    'Joko' : 82,
}

def daftarmahasiswa():
    print("Daftar Mahasiswa:")
    for nama, nilai in data_siswa.items():
        print(f"Nama: {nama}, Nilai: {nilai}")

def ratarata():
    nilai = [70, 85, 90, 75, 60, 80, 95, 88, 77, 82]
    print(f"Rata-Rata Nilai Mahasiswa: {np.mean(nilai)}")

def nilaitertinggi():
    nilai = [70, 85, 90, 75, 60, 80, 95, 88, 77, 82]
    print(f"Nilai Tertinggi: {np.max(nilai)} ")

def nilaiterendah():
    nilai = [70, 85, 90, 75, 60, 80, 95, 88, 77, 82]
    print(f"Nilai Terendah: {np.min(nilai)}")

def mahasiswaremidi():
    print("Mahasiswa Remidi Yang Memerlukan Remidi: ")
    for nama, nilai in data_siswa.items():
        if nilai < 70:
            print(f"Nama: {nama}, Nilai: {nilai}")

def keluar():
    print("Terima Kasih. Program Selesai")

while True:
    print("\n========= UNIVERSITAS DASPRO =========")
    print("")
    print("Pilih operasi yang ingin dilakukan")
    print("1. Daftar Mahasiswa")
    print("2. Rata-Rata Nilai Mahasiswa")
    print("3. Nilai Tertinggi")
    print("4. Nilai Terendah")
    print("5. Mahasiswa Remedi")
    print("6. Keluar")
    print("")
    print("======================================\n")

    # BUAT LAH TAMPILAN MENU DISINI!!! 

    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == '1':
        daftarmahasiswa()
        pass

    elif pilihan == '2':
        ratarata()
        pass

    elif pilihan == '3':
        nilaitertinggi()
        pass

    elif pilihan == '4':
        nilaiterendah()
        pass
        
    elif pilihan == '5':
        mahasiswaremidi()
        pass

    elif pilihan == '6':
        keluar()
        break

    else:
        print("Masukkan Pilihan Yang Sesuai")
