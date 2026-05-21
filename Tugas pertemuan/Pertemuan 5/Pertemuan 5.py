# Nomor 1
x = 0
y = 2
z = 0
print(x == y)
print(x == y)
print(x != y)
print(x < y)
print(y < x)
print(x > y)
print(x <= y)
print(x <= z)
print(y <= z)
print(x >= y)
print(x >= z)

# Nomor 2
n = int(input("Masukkan nilai n: "))
print(n > 100)
print(n < 100)

# Nomor 3
x = 12
if x == 12:
    print("x sama dengan 12")
    
# Nomor 4
x = 12
if x > 2:
    print("x lebih besar dari 2 ")
if x < 12:
    print("x lebih kecil dari 12 ")
if x == 12:
    print("x sama dengan 12 ")

# Nomor 5
x = 12
if x > 14:
    print("x lebih besar dari 14")
else:
    print("x lebih kecil atau sama dengan 14")

# Nomor 6
x = 12
if x == 12:
    print("x == 12")
elif x > 14:
    print("x > 14")
elif x > 2:
    print("x > 2")
else:
    print("x lebih kecil dari 2")
   
# Nomor 7
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
if angka1 > angka2:
    angka_besar = angka1
else:
    angka_besar = angka2
print("angka yang besar adalah ", angka_besar)

# Nomor 8
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))

# Logika diperbaiki agar selalu akurat mencari yang terbesar
angka_besar = angka1
if angka2 > angka_besar:
    angka_besar = angka2
if angka3 > angka_besar:
    angka_besar = angka3

print("angka yang besar adalah ", angka_besar)

# Nomor 9
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))

angka_besar = max(angka1, angka2, angka3)
print("angka paling besar adalah ", angka_besar)

# Nomor 10
pendapatan_bulanan = float(input("Masukkan pendapatan bulanan Anda: "))
pajak = 0

pendapatan_tahunan = pendapatan_bulanan * 12

# Logika penentuan tarif berdasarkan tabel
if pendapatan_tahunan <= 60000000:
    tarif = 0.05
elif pendapatan_tahunan <= 250000000:
    tarif = 0.15
elif pendapatan_tahunan <= 500000000:
    tarif = 0.25
else:
    tarif = 0.30

pajak = pendapatan_tahunan * tarif

# Cetak hasil
print("Tarif pajak Anda adalah:", tarif * 100, "%")
print("Pajak penghasilan yang harus anda bayar adalah", pajak, "rupiah")