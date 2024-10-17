# Deazard Muhammad Arrayyan
# 102022300118
# SI-47-01

import pandas as pd

data_lengkap = pd.read_csv("DataPendahuluan.csv")

def tampilkan_pendidikan_tertinggi():
    pendidikan_tertinggi = data_lengkap[['Provinsi', 'Tingkat_Penyelesaian_Pendidikan']].sort_values(by='Tingkat_Penyelesaian_Pendidikan', ascending=False).head(5)
    print("\n5 Kota dengan Tingkat Penyelesaian Pendidikan Tertinggi:")
    print(pendidikan_tertinggi)

def tampilkan_pengangguran_tertinggi():
    pengangguran_tertinggi = data_lengkap[['Provinsi', 'Tingkat_Setengah_Pengangguran']].sort_values(by='Tingkat_Setengah_Pengangguran', ascending=False).head(5)
    print("\n5 Kota dengan Tingkat Pengangguran Tertinggi:")
    print(pengangguran_tertinggi)

def tampilkan_pendidikan_terendah():
    pendidikan_terendah = data_lengkap[['Provinsi', 'Tingkat_Penyelesaian_Pendidikan']].sort_values(by='Tingkat_Penyelesaian_Pendidikan').head(5)
    print("\n5 Kota dengan Tingkat Penyelesaian Pendidikan Terendah:")
    print(pendidikan_terendah)

def tampilkan_pengangguran_terendah():
    pengangguran_terendah = data_lengkap[['Provinsi', 'Tingkat_Setengah_Pengangguran']].sort_values(by='Tingkat_Setengah_Pengangguran').head(5)
    print("\n5 Kota dengan Tingkat Pengangguran Terendah:")
    print(pengangguran_terendah)

def tampilkan_seluruh_data():
    print("\nTampilkan Seluruh Data:")
    print(data_lengkap)

while True:
    print("\nMenu:")
    print("1. 5 Kota dengan Tingkat Penyelesaian Pendidikan Tertinggi")
    print("2. 5 Kota dengan Tingkat Pengangguran Tertinggi")
    print("3. 5 Kota dengan Tingkat Penyelesaian Pendidikan Terendah")
    print("4. 5 Kota dengan Tingkat Pengangguran Terendah")
    print("5. Tampilkan Seluruh Data")
    print("6. Keluar")

    Pilihan = input("\nPilih menu: ")

    if Pilihan == '1':
        tampilkan_pendidikan_tertinggi()
    elif Pilihan == '2':
        tampilkan_pengangguran_tertinggi()
    elif Pilihan == '3':
        tampilkan_pendidikan_terendah()
    elif Pilihan == '4':
        tampilkan_pengangguran_terendah()
    elif Pilihan == '5':
        tampilkan_seluruh_data()
    elif Pilihan == '6':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")
