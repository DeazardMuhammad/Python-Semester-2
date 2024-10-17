pin = int(input("masukkan pin anda :"))
saldo = 50000
logtrx = []
def cekSaldo():
    global saldo
    print("Rp " + str(saldo))
def tarikUang():
    global saldo
    tarik = int(input("masukkan Jumlah Uang yang di tarik : Rp."))    
    if tarik > 0:
        saldo -= tarik
        print("Saldo Asli anda: Rp.", saldo)
        logtrx.append(("tarik uang Rp.", tarik))

def setorUang():
    global saldo
    setor = int(input("masukkan Jumlah Uang yang di setor :"))
    saldo += setor
    print("Saldo Asli anda: Rp. ", saldo)
    logtrx.append(("setor uang Rp. ",setor))

def CetakTransaksi():
    for transaksi, a in logtrx:
        print(transaksi, a)                
if pin == 6666:
    while True:
            print("\n")
            print("===Menu Utama===")
            print("1.Cek Saldo")
            print("2.Tarik Uang")
            print("3.Setor Uang")
            print("4.Cetak Transaksi")
            print("5. Keluar")           
            menu = int(input("Pilih menu: "))
            print("\n")           
            if menu == 1:
                cekSaldo()
            elif menu == 2:
                tarikUang()
            elif menu == 3:
                setorUang()
            elif menu == 4:
                CetakTransaksi()
            else:
                break
else :
    print("pin anda salah!")