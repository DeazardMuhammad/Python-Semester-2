# Nama: Deazard Muhammad Arrayyan
# NIM: 102022300118

def input_nilai():
    print("\n==Input Nilai==")
    kuis = int(input("Masukkan Nilai Kuis: "))
    tugas = int(input("Masukkan Nilai Tugas: "))
    uts = int(input("Masukkan Nilai UTS: "))
    uas = int(input("Masukkan Nilai UAS: "))
    print("Nilai Berhasil Dimasukkan\n")
    return kuis, tugas, uts, uas

def tampilkan_nilai(kuis, tugas, uts, uas):
    print("\nNilai Kuis:", kuis)
    print("Nilai Tugas:", tugas)
    print("Nilai UTS:", uts)
    print("Nilai UAS:", uas)
    print("")

def tampilkan_nilai_akhir(kuis, tugas, uts, uas):
    nilaiAkhir = (kuis*0.2) + (tugas*0.15) + (uts*0.3) + (uas*0.35)
    print("Nilai Akhir:", nilaiAkhir)
    if nilaiAkhir > 80:
        print("Indeks Huruf: A\n")
    elif nilaiAkhir > 70:
        print("Indeks Huruf: AB\n")
    elif nilaiAkhir > 65:
        print("Indeks Huruf: B\n")
    elif nilaiAkhir > 60:
        print("Indeks Huruf: BC\n")
    elif nilaiAkhir > 50:
        print("Indeks Huruf: C\n")
    elif nilaiAkhir > 40:
        print("Indeks Huruf: D\n")
    else:
        print("Indeks Huruf: E\n")

def tampilkan_status_kelulusan(nilaiAkhir):
    if nilaiAkhir >= 40:
        print("Status Kelulusan: Lulus")
    else:
        print("Status Kelulusan: Tidak Lulus")

def NilaiMhs():
    print("Menu:")
    print("1. Memasukkan Nilai (Kuis, Tugas, UTS, UAS)")
    print("2. Menampilkan Nilai")
    print("3. Menampilkan Nilai Akhir")
    print("4. Menampilkan Status Kelulusan")
    print("5. Keluar")
    while True:
        kategori = int(input("Pilih Menu: "))
        if kategori == 1:
            kuis, tugas, uts, uas = input_nilai()
        elif kategori == 2:
            tampilkan_nilai(kuis, tugas, uts, uas)
        elif kategori == 3:
            tampilkan_nilai_akhir(kuis, tugas, uts, uas)
        elif kategori == 4:
            nilaiAkhir = (kuis*0.2) + (tugas*0.15) + (uts*0.3) + (uas*0.35)
            tampilkan_status_kelulusan(nilaiAkhir)
        elif kategori == 5:
            print("Terima Kasih Telah Menggunakan Program Ini")
            break

NilaiMhs()