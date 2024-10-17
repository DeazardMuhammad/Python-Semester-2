print("\nMenu:")
print("1. Tambah Data Mahasiswa")
print("2. Lihat Data Mahasiswa")
print("3. Hitung Nilai Akhir")
print("4. Urutkan Data Mahasiswa")
print("5. Hapus Data Mahasiswa")
print("6. Keluar Program")

def tambah_data_mahasiswa(data_mahasiswa):
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    quiz = float(input("Masukkan Nilai Quiz: "))
    tugas = float(input("Masukkan Nilai Tugas: "))
    ujian = float(input("Masukkan Nilai Ujian: "))
    nilai_akhir = (quiz * 0.25) + (tugas * 0.25) + (ujian * 0.5)
    data_mahasiswa[nim] = {'nama': nama, 'nim': nim, 'nilai_quiz': quiz, 'nilai_tugas': tugas, 'nilai_ujian': ujian, 'nilai_akhir': nilai_akhir}

def tambah_data_mahasiswa(data_mahasiswa):
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    quiz = float(input("Masukkan Nilai Quiz: "))
    tugas = float(input("Masukkan Nilai Tugas: "))
    ujian = float(input("Masukkan Nilai Ujian: "))
    nilai_akhir = (quiz * 0.25) + (tugas * 0.25) + (ujian * 0.5)
    data_mahasiswa[nim] = {'nama': nama, 'nim': nim, 'nilai_quiz': quiz, 'nilai_tugas': tugas, 'nilai_ujian': ujian, 'nilai_akhir': nilai_akhir}
    print(f"Data Mahasiswa {data_mahasiswa[nim]} Berhasil Ditambahkan")

def lihat_data_mahasiswa(data_mahasiswa):
    print("Data Mahasiswa:")
    for index, data in enumerate(data_mahasiswa.values(), start=1):
        print(f"{index}. {data}")

def hitung_nilai_akhir(data_mahasiswa):
    nim = input("Masukkan NIM mahasiswa untuk menhitung nilai akhir: ")
    if nim in data_mahasiswa:
        mahasiswa = data_mahasiswa[nim]
        print(f"Nilai Akhir dari Mahasiswa dengan Nama {mahasiswa['nama']}, NIM {nim} adalah {mahasiswa['nilai_akhir']}")
    else:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan")

def urutkan_data_mahasiswa(data_mahasiswa):
    sorted_mahasiswa = sorted(data_mahasiswa.values(), key=lambda x: x['nilai_akhir'], reverse=True)
    print("Data Mahasiswa (Nilai Akhir Terbesar):")
    for index, mahasiswa in enumerate(sorted_mahasiswa, start=1):
        print(f"{index}. Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}, Nilai Akhir: {mahasiswa['nilai_akhir']}")

def hapus_data_mahasiswa(data_mahasiswa):
    nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus")
    else:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan")

def main():
    data_mahasiswa = {}
    while True:
        pilihan = input("\nMasukkan pilihan menu: ")

        if pilihan == '1':
            tambah_data_mahasiswa(data_mahasiswa)
        elif pilihan == '2':
            lihat_data_mahasiswa(data_mahasiswa)
        elif pilihan == '3':
            hitung_nilai_akhir(data_mahasiswa)
        elif pilihan == '4':
            urutkan_data_mahasiswa(data_mahasiswa)
        elif pilihan == '5':
            hapus_data_mahasiswa(data_mahasiswa)
        elif pilihan == '6':
            print("Program selesai, terimakasih!")
            break
        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.")

main()
