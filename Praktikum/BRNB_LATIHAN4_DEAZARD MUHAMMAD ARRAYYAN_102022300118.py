import pandas as pd

# Membaca data dari file CSV
df = pd.read_csv('Top 50 Football Player.csv')

# Menambahkan kolom rata rata
df['Avarage'] = (df["Speed"] + df["Stamina"] + df["Attack"] + df["Defense"])/4


# Mengurutkan data berdasarkan rata-rata tertinggi
rata_tertinggi = df.sort_values('Avarage', ascending=False)


# Memfilter data berdasarkan umur antara 23 dan 28 tahun
umur = rata_tertinggi[(rata_tertinggi['Umur'] >= 23)].head(11)


# Mengambil 11 data teratas
print(umur)

# Menghitung total harga
total = umur['Harga ($)'].sum()
print(f"Total Harga : ${total}")

# Mencari nilai tertinggi dari setiap kolom ability beserta nama pemain
speed_tertinggi = df["Speed"].max()
stamina_tertinggi = df["Stamina"].max()
attack_tertinggi = df["Attack"].max()
defense_tertinggi = df["Defense"].max()

print("Speed Tertinggi:", speed_tertinggi)
print("Stamina Tertinggi:",stamina_tertinggi)
print("Attack Tertinggi:",attack_tertinggi)
print("Defense Tertinggi:",defense_tertinggi)

# Menampilkan data

