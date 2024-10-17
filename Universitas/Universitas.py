import numpy as np

data_siswa = {
    'Agus': 70,
    'Budi': 85,
    'Citra': 90,
    'Dian': 75,
    'Eka': 60,
    'Fani': 80,
    'Gina': 95,
    'Hadi': 88,
    'Indra': 77,
    'Joko': 82,
}

def display_students():
    for nama, nilai in data_siswa.items():
        print(f"Nama: {nama} , Nilai: {nilai}")

def Ratarata():
    mean_nilai = np.mean(list(data_siswa.values()))
    mahasiswa_terbanyak = []
    print(f"Rata rata nilai mahasiswa adalah: {np.mean(mean_nilai)}")

def nilaiTertinggi():
    max_nilai = np.max(list(data_siswa.values()))
    mahasiswa_terbanyak = []
    print(f"Nilai Tertinggi mahasiswa adalah: {np.max(max_nilai)}")

def nilaiTerendah():
    min_nilai = np.min(list(data_siswa.values()))
    mahasiswa_terbanyak = []
    print(f"Nilai Terendah mahasiswa adalah: {np.min(min_nilai)}")

def remed():
    for nama, nilai in data_siswa.items():
        if nilai < 70:
            print(f"Mahasiswa yang remedi adalah : {nama}, dengan nilai {nilai}") 

while True:
    print("\n========= UNIVERSITAS DASPRO =========")
    print("1. Data mahasiswa")
    print("2. Rata rata nilai mahasiswa")
    print("3. Nilai tertinggi")
    print("4. Nilai terendah")
    print("5. Mahasiswa remidi")
    print("6. Out")

    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == '1':
        display_students()
        pass

    elif pilihan == '2':
        Ratarata()
        pass

    elif pilihan == '3':
        nilaiTertinggi()
        pass

    elif pilihan == '4':
        nilaiTerendah()
        pass
        
    elif pilihan == '5':
        remed()
        pass

    elif pilihan == '6':
        print("TERIMAKASIH PROGRAM SELESAI")
        break