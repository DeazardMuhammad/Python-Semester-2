#import library sqlite 3 dan maplotlib
import sqlite3
import matplotlib.pyplot as plt
from prettytable import PrettyTable

#buatlah database yang dapat diakses secara keseluruhan

#Buatlah fungsi untuk membuat tabel
def buattabel():
    conn = sqlite3.connect('database_obat.db')
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS tabel_obat (
                    id_obat INTEGER PRIMARY KEY,
                    nama TEXT NOT NULL,
                    harga INTEGER NOT NULL,
                    stok INTEGER NOT NULL,
                    jenis_obat TEXT NOT NULL
                    )
                """)
    conn.commit()
    print("Database Berhasil Dibuat")
    conn.close()
    pass

#Buatlah fungsi untuk menambahkan obat
def tambah_obat(id_obat, nama, harga, stok, jenis_obat):
    conn = sqlite3.connect('database_obat.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO tabel_obat (id_obat, nama, harga, stok, jenis_obat) VALUES (?,?,?,?,?)", (id_obat, nama, harga, stok, jenis_obat,))
    conn.commit()
    print(f"Data Obat '{nama}' Berhasil Ditambahkan")
    conn.close()

def input_tambah_obat():
    id_obat = input("Masukkan id Obat: ")
    nama = input("Masukkan Nama Obat: ")
    harga = int(input("Masukkan Harga Obat: "))
    stok = int(input("Masukkan Stok Obat: "))
    jenis_obat = input("Masukkan Jenis Obat: ")

    tambah_obat(id_obat, nama, harga, stok, jenis_obat)
    
#Buatlah fungsi untuk hapus obat berdasarkan id obat
def hapus_obat(id_obat):
    conn = sqlite3.connect('database_obat.db')
    cur = conn.cursor()
    cur.execute("Delete From tabel_obat WHERE id_obat =?", (id_obat,))
    conn.commit()
    conn.close()
    print("Data Obat Telah Dihapus")    
    

def input_hapus_obat():
    id_obat = int(input("Hapus Obat: "))
    hapus_obat(id_obat)
    
#Buatlah fungsi untuk mencari obat berdasarkan id
def cari_obat(id_obat: int):
    conn = sqlite3.connect('database_obat.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tabel_obat WHERE id_obat LIKE ?", (id_obat,))
    result = cur.fetchall()
    cur.close()
    conn.close()
    for row in result:
        print(row)

def input_cari_obat():
    id_obat = int(input("Cari Obat: "))
    cari_obat(id_obat)

#Buatlah fungsi untuk menampilkan seluruh obat yang ada pada tabel
def tampilkan_obat():
    conn = sqlite3.connect('database_obat.db')
    cur = conn.cursor()
    cur.execute("Select * From tabel_obat")
    res = cur.fetchall()
    conn.close()
    table = PrettyTable()
    table.field_names = ["ID Obat", "Nama", "Harga", "Stok", "Jenis"]
    for row in res:
        table.add_row(row)

    print(table)
    
        
#Buatlah fungsi untuk visualisasi data dalam bentuk bar chart
def vis_data():
    conn = sqlite3.connect('database_obat.db')
    cur = conn.cursor()
    cur.execute("SELECT nama, stok FROM tabel_obat GROUP BY nama")
    data = cur.fetchall()
    conn.close()
    
    nama = [row[0] for row in data]
    stok = [row[1] for row in data]
    
    plt.bar(nama, stok)
    plt.title('Stok Keseluruhan Obat')
    plt.xlabel('Stok Obat')
    plt.show()

#buatlah perulangan untuk menampilkan pilihan menu dan menjalankan program
while True:
    #Tampilkan menu
    print("Selamat Datang Di Apotek Daspro!!")
    print("Pilihan Menu")
    print("1. Membuat Tabel")
    print("2. Menambahkan Obat")
    print("3. Menghapus Obat")
    print("4. Mencari Obat")
    print("5. Menampilkan Data")
    print("6. Visualisasi Data")
    print("7. Keluar")
    pilihan = int(input("Masukan pilihan menu: "))
    if pilihan == 1:
        buattabel()
        pass
    elif pilihan == 2:
        input_tambah_obat()
    elif pilihan == 3:
        input_hapus_obat()
    elif pilihan == 4:
        cari_obat()
        pass
    elif pilihan == 5:
        print(tampilkan_obat())
    elif pilihan == 6:
        vis_data()
    elif pilihan == 7:
        print("Terimakasih Sudah Menggunakan Layanan Apotik Daspro!!")
        break
    else :
        print("Masukkan Nomor Menu Yang Benar!")
        pass