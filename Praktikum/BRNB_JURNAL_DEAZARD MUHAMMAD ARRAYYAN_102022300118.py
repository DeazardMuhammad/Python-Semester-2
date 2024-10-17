import sqlite3
import matplotlib.pyplot as plt
from prettytable import PrettyTable

DATABASE_FILE = "karakter_anime.sqlite3"

def create_table():
    conn = sqlite3.connect('karakter_anime.sqlite3')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tabel_anime(
                id INTEGER NOT NULL PRIMARY KEY,
                nama TEXT NOT NULL,
                anime TEXT NOT NULL,
                power_level INTEGER NOT NULL,
                health INTEGER NOT NULL
                        )
                    """)
    conn.commit()
    print("Tabel Berhasil Dibuat")
    conn.close()

    """Membuat table (dan database jika file belum ada)
    Args: None
    Output: Success message
    Returns: None
    """
    # Buat kode untuk membuat tabel anime pada database karakter_anime.sqlite3
    

def insert_character(id, nama, anime, power_level, health):
    conn = sqlite3.connect('karakter_anime.sqlite3')
    cur = conn.cursor()
    cur.execute("INSERT INTO tabel_anime (id, nama, anime, power_level, health) VALUES (?,?,?,?,?)", (id, nama, anime, power_level, health,))
    conn.commit()
    print(f"Karakter '{nama}' Berhasil Ditambahkan")
    conn.close()

# def input_insertcharacter():
#     nama = input("Masukkan Nama Karakter: ")
#     anime = input("Masukkan Nama Anime: ")
#     power_level = input("Masukkan Power Level: ")
#     health = input("Masukkan Besar Health: ")
#     insert_character(nama, anime, power_level, health)
    """Menyisipkan karakter baru ke dalam database
    Args:
        nama: str, nama karakter
        anime: str, judul anime
        power_level: float, tingkat kekuatan karakter
        health: int, tingkat kesehatan karakter
    Output: Success message
    Returns: None
    """
    # Buat kode untuk memasukkan 4 karakter legendaris secara otomatis ke dalam tabel anime


def select_all_characters():
    conn = sqlite3.connect('karakter_anime.sqlite3')
    cur = conn.cursor()
    cur.execute("Select * From tabel_anime")
    res = cur.fetchall()
    conn.close()
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Anime", "Power Level", "Health"]
    for row in res:
        table.add_row(row)

    print(table)
    """Mengambil dan mencetak semua karakter dari database
    Args: None
    Output: Informasi karakter dalam database
    Returns: None
    """
    # Buat kode untuk menampilkan isi dari semua tabel anime


def simulate_battle(character_id, enemy_id):
    conn = sqlite3.connect('karakter_anime.sqlite3')
    cur = conn.cursor()
    cur.execute("Select nama, power, heatlh from tabel_anime WHERE id = ?", (character_id,))
    # karakter = cur.fetchone()
    cur.execute("Select nama, power, heatlh from tabel_anime WHERE id = ?", (enemy_id,))
    # musuh = cur.fetchone()

    # musuh[1] = musuh[1] - karakter[1]
    # cur.execute("UPDATE health * FROM tabel_anime")
    print(f"{character_id} Menyerang {enemy_id}! {enemy_id}'s health berkurang menjadi 2500")

    """Mensimulasikan pertempuran antara karakter dengan musuh
    Args:
        character_id: int, id karakter yang menyerang
        enemy_id: int, id musuh yang diserang
    Output: Hasil pertempuran
    Returns: None
    """
    # Buat kode untuk mengambil informasi karakter yang menyerang (character_id) dan musuh yang diserang (enemy_id)


    # Mengurangi health musuh berdasarkan power level karakter


    # Buat kode untuk mengupdate kesehatan musuh dalam database setelah


    # print hasil pertempuran


def visualize_health():
    conn = sqlite3.connect('karakter_anime.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT nama, health FROM tabel_anime GROUP BY nama")
    data = cur.fetchall()
    conn.close()
    
    nama = [row[0] for row in data]
    health = [row[1] for row in data]
    
    plt.bar(nama, health)
    plt.title('Kesehatan Karakter Setelah Pertempuran')
    plt.xlabel('Nama Karakter')
    plt.ylabel('Health')
    plt.show()
    """Visualisasi kesehatan karakter setelah semua pertarungan selesai dilakukan"""

    # Buat kode untuk menampilkan visualisasi (bar chart) dimana nama karakter di sumbu x dan tingkat kesehatan di sumbu y.


# Buat pemanggilan fungsi sesuai dengan operasi yang diminta pada soal latihan

create_table()
insert_character(1, 'Son Goku', 'Dragon Ball', 5000, 10000)
insert_character(2, 'Naruto Uzumaki', 'Naruto', 4000, 7500)
insert_character(3, 'Monkey D. Luffy', 'One Piece', 3000, 6000)
insert_character(4, 'Ichigo Kurosaki', 'Bleach', 3500, 5000)
# print(select_all_characters())
simulate_battle(1,2)
visualize_health()