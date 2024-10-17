# Kelas: SI-47-01
# Kelompok: 03
# Anggota Kelompok: 
# 1. Andi Muhammad Ihsanul Haq Malvira (102022300085)
# 2. Deazard Muhammad Arrayyan (102022300118)
# 3. Keysha Aulia Putri (102022300196)
# 4. Neilson Tristant(102022300136)
# 5. Puan Azkia Maulida(102022300385)

import os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time

# Data awal
users = {
    'manager': '12345',
    'resepsionis': '123'
}

room_types = {
    1: {'name': 'standar', 'price': 100000, 'available': 10, 'max_people': 2},
    2: {'name': 'suite', 'price': 200000, 'available': 10, 'max_people': 4},
    3: {'name': 'deluxe', 'price': 300000, 'available': 5, 'max_people': 6}
}

reservations = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print("\n" + "="*50)
    print(f"{title:^50}")
    print("="*50)

def login():
    clear_screen()
    print_header("LOGIN")
    attempts = 0
    while attempts < 3:
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            return username
        else:
            print("Username atau password salah.")
            attempts += 1
    print("Kesempatan login habis.")
    return None

def menu_manager():
    while True:
        clear_screen()
        print_header("MENU MANAGER")
        print("1. Presentase penghuni kamar per bulan")
        print("2. Pendapatan per bulan")
        print("3. Jenis kamar yang dipakai per bulan")
        print("4. Logout")
        choice = input("Pilih menu: ")
        if choice == '1':
            presentase_penghuni()
        elif choice == '2':
            pendapatan_per_bulan()
        elif choice == '3':
            jenis_kamar_dipakai()
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid.")

def menu_resepsionis():
    while True:
        clear_screen()
        print_header("MENU RESEPSIONIS")
        print("1. Jenis Kamar")
        print("2. Add")
        print("3. Edit")
        print("4. Delete")
        print("5. Searching")
        print("6. Logout")
        choice = input("Pilih menu: ")
        if choice == '1':
            jenis_kamar()
        elif choice == '2':
            add_reservation()
        elif choice == '3':
            edit_reservation()
        elif choice == '4':
            delete_reservation()
        elif choice == '5':
            search_reservation()
        elif choice == '6':
            break
        else:
            print("Pilihan tidak valid.")

def jenis_kamar():
    clear_screen()
    print_header("JENIS KAMAR")
    for key, value in room_types.items():
        print(f"{key}. {value['name']} - Rp. {value['price']} ({value['available']} tersedia)")
    input("Tekan Enter untuk kembali ke menu...")

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def add_reservation():
    clear_screen()
    print_header("ADD RESERVATION")
    try:
        name = input("Nama Penghuni: ")
        if not name:
            print("Nama tidak boleh kosong.")
            time.sleep(2)
            return
        
        check_in_date = input("Tanggal Check-in (YYYY-MM-DD): ")
        if not validate_date(check_in_date):
            print("Tanggal tidak valid.")
            time.sleep(2)
            return

        duration = int(input("Durasi Menginap (hari): "))
        if duration <= 0:
            print("Durasi tidak boleh 0 atau kurang.")
            time.sleep(2)
            return
        
        num_people = int(input("Jumlah Penghuni: "))

        print("Pilih Jenis Kamar:")
        jenis_kamar()
        room_type = int(input("Enter room type: "))
        if room_type not in room_types:
            print("Jenis kamar tidak valid.")
            time.sleep(2)
            return
        
        if num_people > room_types[room_type]['max_people']:
            print(f"Jumlah penghuni melebihi kapasitas maksimal untuk kamar {room_types[room_type]['name']}.")
            time.sleep(2)
            return

        if room_types[room_type]['available'] > 0:
            check_out_date = datetime.strptime(check_in_date, '%Y-%m-%d') + timedelta(days=duration)
            reservation_id = len(reservations) + 1
            total_price = room_types[room_type]['price'] * duration
            reservations.append({
                'id': reservation_id,
                'name': name,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date.strftime('%Y-%m-%d'),
                'duration': duration,
                'num_people': num_people,
                'room_type': room_type,
                'total_price': total_price,
                'checked_out': False
            })
            room_types[room_type]['available'] -= 1
            print(f"Reservasi berhasil ditambahkan. Total harga: Rp. {total_price}")
        else:
            print("Kamar tidak tersedia.")
    except ValueError:
        print("Input tidak valid. Pastikan memasukkan data dengan benar.")
        time.sleep(2)
    input("Tekan Enter untuk kembali ke menu...")

def edit_reservation():
    clear_screen()
    print_header("EDIT RESERVATION")
    try:
        reservation_id = int(input("ID Pemesanan yang ingin diubah: "))
        for res in reservations:
            if res['id'] == reservation_id:
                print("1. Check-out")
                print("2. Ganti jadwal")
                choice = input("Pilih menu: ")
                if choice == '1':
                    res['checked_out'] = True
                    room_types[res['room_type']]['available'] += 1
                    print("Check-out berhasil.")
                elif choice == '2':
                    new_check_in_date = input("Tanggal Check-in baru (YYYY-MM-DD): ")
                    if not validate_date(new_check_in_date):
                        print("Tanggal tidak valid.")
                        time.sleep(2)
                        return
                    new_duration = int(input("Durasi Menginap baru (hari): "))
                    if new_duration <= 0:
                        print("Durasi tidak boleh 0 atau kurang.")
                        time.sleep(2)
                        return
                    new_check_out_date = datetime.strptime(new_check_in_date, '%Y-%m-%d') + timedelta(days=new_duration)
                    res['check_in_date'] = new_check_in_date
                    res['check_out_date'] = new_check_out_date.strftime('%Y-%m-%d')
                    res['duration'] = new_duration
                    res['total_price'] = room_types[res['room_type']]['price'] * new_duration
                    print("Jadwal berhasil diubah.")
                return
        print("ID Pemesanan tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Pastikan memasukkan data dengan benar.")
        time.sleep(2)
    input("Tekan Enter untuk kembali ke menu...")

def delete_reservation():
    clear_screen()
    print_header("DELETE RESERVATION")
    try:
        reservation_id = int(input("ID Pemesanan yang ingin dihapus: "))
        for res in reservations:
            if res['id'] == reservation_id:
                if res['checked_out']:
                    print("Reservasi yang sudah check-out tidak bisa dihapus.")
                    time.sleep(2)
                    return
                room_types[res['room_type']]['available'] += 1
                reservations.remove(res)
                print("Reservasi berhasil dihapus.")
                return
        print("ID Pemesanan tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Pastikan memasukkan data dengan benar.")
        time.sleep(2)
    input("Tekan Enter untuk kembali ke menu...")

def search_reservation():
    clear_screen()
    print_header("SEARCH RESERVATION")
    try:
        print("Pilih Jenis Kamar untuk mencari:")
        jenis_kamar()
        room_type = int(input("Enter room type: "))
        if room_type in room_types:
            print(f"Reservasi untuk kamar {room_types[room_type]['name']}:")
            for res in reservations:
                if res['room_type'] == room_type:
                    status = "Sudah Check-out" if res['checked_out'] else "Belum Check-out"
                    print(f"ID Pemesanan   : {res['id']}")
                    print(f"Nama Penghuni  : {res['name']}")
                    print(f"Check-in Date  : {res['check_in_date']}")
                    print(f"Check-out Date : {res['check_out_date']}")
                    print(f"Durasi         : {res['duration']} hari")
                    print(f"Jumlah Penghuni: {res['num_people']}")
                    print(f"Total Harga    : Rp. {res['total_price']}")
                    print(f"Status         : {status}")
                    print("-" * 50)
        else:
            print("Jenis kamar tidak valid.")
    except ValueError:
        print("Input tidak valid. Pastikan memasukkan data dengan benar.")
        time.sleep(2)
    input("Tekan Enter untuk kembali ke menu...")

def presentase_penghuni():
    clear_screen()
    try:
        penghuni_per_bulan = {}
        for res in reservations:
            check_in_date = datetime.strptime(res['check_in_date'], '%Y-%m-%d')
            month_year = check_in_date.strftime('%Y-%m')
            if month_year not in penghuni_per_bulan:
                penghuni_per_bulan[month_year] = 0
            penghuni_per_bulan[month_year] += res['duration']

        months = sorted(penghuni_per_bulan.keys())
        values = [penghuni_per_bulan[month] for month in months]

        plt.bar(months, values)
        plt.title('Presentase Penghuni Kamar per Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Jumlah Hari Penghuni')
        plt.xticks(rotation=45)
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        time.sleep(2)
    input("Tekan Enter untuk kembali ke menu...")

def pendapatan_per_bulan():
    clear_screen()
    try:
        pendapatan_per_bulan = {}
        for res in reservations:
            check_in_date = datetime.strptime(res['check_in_date'], '%Y-%m-%d')
            month_year = check_in_date.strftime('%Y-%m')
            if month_year not in pendapatan_per_bulan:
                pendapatan_per_bulan[month_year] = 0
            pendapatan_per_bulan[month_year] += room_types[res['room_type']]['price'] * res['duration']

        months = sorted(pendapatan_per_bulan.keys())
        values = [pendapatan_per_bulan[month] for month in months]

        plt.bar(months, values)
        plt.title('Pendapatan per Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Pendapatan (Rp)')
        plt.xticks(rotation=45)
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        time.sleep(2)
    input("Tekan Enter untuk kembali ke menu...")

def jenis_kamar_dipakai():
    clear_screen()
    try:
        kamar_per_bulan = {}
        for res in reservations:
            check_in_date = datetime.strptime(res['check_in_date'], '%Y-%m-%d')
            month_year = check_in_date.strftime('%Y-%m')
            if month_year not in kamar_per_bulan:
                kamar_per_bulan[month_year] = {rt['name']: 0 for rt in room_types.values()}
            kamar_per_bulan[month_year][room_types[res['room_type']]['name']] += 1

        months = sorted(kamar_per_bulan.keys())
        data = {room_types[rt]['name']: [kamar_per_bulan[month].get(room_types[rt]['name'], 0) for month in months] for rt in room_types}

        for room_name, values in data.items():
            plt.plot(months, values, label=room_name)

        plt.title('Jenis Kamar yang Dipakai per Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Jumlah Pemakaian')
        plt.xticks(rotation=45)
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        time.sleep(2)
    input("Tekan Enter untuk kembali ke menu...")

def main():
    while True:
        user = login()
        if user:
            if user == 'manager':
                menu_manager()
            elif user == 'resepsionis':
                menu_resepsionis()
        else:
            break

main()
