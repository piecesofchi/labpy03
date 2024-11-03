import random

# Meminta input jumlah bilangan acak yang ingin dihasilkan (N)
N = int(input("Masukkan nilai N: "))

# Variabel untuk menghitung data yang valid
count = 0

# Loop untuk menghasilkan bilangan acak yang lebih kecil dari 0.5
while count < N:
    # Menghasilkan bilangan acak
    num = random.random()

    # Memastikan bilangan yang dihasilkan lebih kecil dari 0.5
    if num < 0.5:
        count += 1
        print(f"data ke: {count}{num:.17f}")

print("Selesai")