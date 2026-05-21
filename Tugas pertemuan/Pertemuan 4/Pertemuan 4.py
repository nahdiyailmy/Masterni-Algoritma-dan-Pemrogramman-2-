# Nomor 1
print("Nahdiya anak baik..")
baik = input()
print("Anak baik", baik, "...beneran?")

# Nomor 2
buku = input("Apakah kamu membaca buku..? ")
print("Hmm..", buku, "...serius?")

# Nomor 3
family = float(input("Enter a number: "))
her_name_is_nazwa = family ** 2.0
print(str(family) + " have 3 sides ", her_name_is_nazwa)

# Nomor 4
family = float(input("Enter a number: "))
her_name_is_nazwa = family ** 2.0
print(str(family) + " have 3 sides ", her_name_is_nazwa)

# Nomor 5
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

# Nomor 6
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

# Nomor 7
fnam = input("May I have your first number, please? ")
lnam = input("May I have your last number, please? ")
print("sure.")
print("\n your number is " + fnam + " " + lnam + ".")

# Nomor 8
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# Nomor 9
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

# Nomor 10
x = input("Enter a number: ")
print(type(x))

# Nomor 11
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
print("Hasil penjumlahan:", a + b)
print("Hasil pengurangan:", a - b)
print("Hasil perkalian:", a * b)
print("Hasil pembagian:", a / b)
print("Selamat kamu sudah pintar matematika")

# Nomor 12
x = float(input("Enter x: "))
y = 1.0
for i in range(100): 
    y = 1.0 / (x + y)
    print(f"Nilai y = {y}")

# Nomor 13
jam = int(input("waktu mulai (jam): "))
menit = int(input("waktu mulai (menit): "))
durasi = int(input("Durasi Acara (menit): "))

total_menit = jam * 60 + menit + durasi

jam_selesai = (total_menit // 60) % 24
menit_selesai = total_menit % 60
print(f"Acara selesai pukul {jam_selesai}:{menit_selesai:02d}")