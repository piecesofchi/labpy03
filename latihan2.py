# Modal awal
modal_awal = 100_000_000

# Variabel untuk menyimpan total laba
total_laba = 0

# Laba per bulan berdasarkan ketentuan
for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba = 0
    elif bulan == 3 or bulan == 4:
        laba = 0.1 * modal_awal
    elif bulan >= 5 and bulan <= 7:
        laba = 0.5 * modal_awal + 0.8  # Kenaikan laba 5%
    elif bulan == 8:
        laba = 0.2 * modal_awal  # Penurunan laba menjadi 2%

    total_laba += laba
    print(f"Laba bulan ke-{bulan} sebesar: {laba}")

print(f"Total laba adalah: {total_laba}")