import pandas as pd
def muat_data():
        # Hint: Isi dengan fungsi untuk memuat data dari file CSV (fungsi untuk membaca data csv?)
    global data
    data = pd.read_csv('Proporsi Rumah Tangga Yang Memiliki Akses Terhadap Layanan Sanitasi Layak, 2021-2023.csv')
    pass

def tampilkan_data_frame():
    # Hint: Isi dengan fungsi untuk menampilkan seluruh dataframe (print data dari csvnya?)
    print(data)
    pass

def tampilkan_gambaran_umum():
    # Hint: Isi dengan fungsi untuk menampilkan informasi umum tentang data (print ringkasan statistik deskriptif dari data?)
    info_data = data.info()
    info_statistik = data.describe()
    print("Informasi Data:")
    print(info_data)
    print("Informasi Statistik:")
    print(info_statistik)
    pass

def sepuluh_provinsi_teratas():
    # Hint: Isi dengan fungsi untuk menampilkan sepuluh provinsi teratas pada tahun 2023  (pakai sort value)
    provinsi_teratas = data[['Provinsi', '2023']].sort_values(by='2023', ascending=False).head(10)
    print("10 Provinsi dengan performa terbaik tahun 2023:")
    print(provinsi_teratas)
    pass

def provinsi_dengan_peningkatan_terbesar():
    # Hint: Isi dengan fungsi untuk menemukan provinsi dengan peningkatan terbesar dari 2021 ke 2023 (pakai data.loc)
    data['Peningkatan'] = data['2023'] - data['2021']
    tingkat_besar = data.loc[data['Peningkatan'].idxmax()]
    print(f"Provinsi dengan peningkatan terbesar dari tahun 2021 ke 2023: {tingkat_besar} ")
    pass

def analisis_korelasi(data):
    # Hint: Isi dengan fungsi untuk menganalisis korelasi antara tahun (fungsi buat mencari korelasi?)
    pass

def kinerja_provinsi_tertentu(data, nama_provinsi):
    # Hint: Isi dengan fungsi untuk menampilkan kinerja provinsi tertentu (pakai data.loc dan kondisi jika data tidak ada)
    pass

def utama():
    data = muat_data()
    while True:
        print("=====================================")
        print("1. Tampilkan seluruh data frame")
        print("2. Tampilkan gambaran umum data")
        print("3. Tampilkan 10 provinsi terbaik tahun 2023")
        print("4. Tampilkan provinsi dengan peningkatan terbesar 2021-2023")
        print("5. Analisis korelasi antar tahun")
        print("6. Tampilkan provinsi tertentu")
        print("7. Keluar")
        # Hint: Tambahkan pilihan menu sesuai deskripsi soal
        print("=====================================")
        pilihan = int(input("Masukkan pilihan Anda: "))
        if pilihan == 1:
            tampilkan_data_frame()
        elif pilihan == 2:
            tampilkan_gambaran_umum()
        elif pilihan == 3:
            sepuluh_provinsi_teratas()
        elif pilihan == 4:
            provinsi_dengan_peningkatan_terbesar()
        elif pilihan == 5:
            analisis_korelasi()
        elif pilihan == 6:
            kinerja_provinsi_tertentu()
        elif pilihan == 7:
            print("Keluar Dari Program")
            break
        # Hint: Tambahkan if else untuk setiap pilihan menu sesuai deskripsi soal

utama()
