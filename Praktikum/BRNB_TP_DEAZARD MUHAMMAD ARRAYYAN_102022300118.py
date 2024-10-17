


import sqlite3
from prettytable import PrettyTable
import matplotlib.pyplot as plt

def buat_tabel():
    conn = sqlite3.connect('inventaris_buku.db')
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS tabel_buku (
                    id_buku INTEGER PRIMARY KEY AUTOINCREMENT,
                    judul TEXT NOT NULL,
                    penulis TEXT NOT NULL,
                    tahun_terbit INTEGER,
                    genre TEXT,
                    stok INTEGER NOT NULL
                    )
                """)
    conn.commit()
    print("Database Berhasil Dibuat")
    conn.close()

def masukkan_buku(judul, penulis, tahun_terbit, genre, stok):
    conn = sqlite3.connect('inventaris_buku.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO tabel_buku (judul, penulis, tahun_terbit, genre, stok) VALUES (?,?,?,?,?)", (judul, penulis, tahun_terbit, genre, stok,))
    conn.commit()
    print(f"Data Buku '{judul}' Berhasil Ditambahkan")
    conn.close()

def input_masukkan_buku():
    judul = input("Masukkan Judul Buku: ")
    penulis = input("Masukkan Nama Penulis: ")
    tahun_terbit = int(input("Masukkan Tahun Terbit: "))
    genre = input("Masukkan Genre Buku: ")
    stok = int(input("Masukkan Stok Buku: "))

    masukkan_buku(judul, penulis, tahun_terbit, genre, stok)

def hapus_buku(id_buku):
    conn = sqlite3.connect('inventaris_buku.db')
    c = conn.cursor()
    c.execute("DELETE FROM tabel_buku WHERE id_buku = ?", (id_buku,))
    conn.commit()
    conn.close()
    print(f"Data dengan ID Buku = {id_buku} berhasil dihapus.")

def input_hapus_buku():
    id_buku = int(input("Masukkan ID buku yang ingin dihapus: "))
    hapus_buku(id_buku)
    

# def cari_buku(judul: str):
#     conn = sqlite3.connect('inventaris_buku.db')
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM tabel_buku WHERE judul LIKE ?", (judul,))
#     res = cur.fetchall()
#     if len(res) == 0:
#         return "Buku Tidak Ditemukan"
#     else:
#         return res
    
def tampilkan_tabel():
    conn = sqlite3.connect('inventaris_buku.db')
    cur = conn.cursor()
    cur.execute("Select * FROM tabel_buku")
    res = cur.fetchall()
    conn.close()

    table = PrettyTable()
    table.field_names = ["ID Buku", "Judul", "Penulis", "Tahun Terbit", "Genre", "Stok"]
    for row in res:
        table.add_row(row)

    print(table)

def visual_buku():
    conn = sqlite3.connect('inventaris_buku.db')
    cur = conn.cursor()
    cur.execute("SELECT genre, COUNT(*) FROM tabel_buku GROUP BY genre")
    data = cur.fetchall()
    conn.close()
    
    genres = [row[0] for row in data]
    jumlah_buku = [row[1] for row in data]
    
    plt.bar(genres, jumlah_buku)
    plt.xlabel('Genre')
    plt.ylabel('Jumlah Buku')
    plt.title('Jumlah Buku per Genre')
    plt.show()

def menu_utama():
    while True:
        print("\nMenu:")
        print("1. Buat Tabel")
        print("2. Masukkan Buku")
        print("3. Tampilkan Buku")
        print("4. Hapus Buku")
        print("5. Tampilkan Data")
        print("6. Keluar")

        Pilihan = input("\nPilih menu: ")

        if Pilihan == '1':
            buat_tabel()
        elif Pilihan == '2':
            input_masukkan_buku()
        elif Pilihan == '3':
            tampilkan_tabel()
        elif Pilihan == '4':
            input_hapus_buku()
        elif Pilihan == '5':
            visual_buku()
        elif Pilihan == '6':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

menu_utama()


