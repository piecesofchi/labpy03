# Saldo awal
saldo = 1000000

while True:
    # Tampilkan saldo dan menu
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    pilihan = input("Pilih menu (1/2): ")

    # Pilihan menu
    if pilihan == "1":
        # Meminta jumlah penarikan
        jumlah_penarikan = int(input("Masukkan jumlah penarikan: "))

        # Mengecek apakah saldo mencukupi
        if jumlah_penarikan <= saldo:
            saldo -= jumlah_penarikan
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak mencukupi untuk penarikan ini.")
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")