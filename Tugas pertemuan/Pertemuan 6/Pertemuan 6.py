# Nomor 1
while True:
    print("nyangkut di perulangan tak hingga")
	
# Nomor 2
angka = 15
while angka > 2:
    print(angka)
    angka -= 2
	
# Nomor 3
i = 1
while i <= 10:
    # cek angka habis dibagi 2 menggunakan module (%)
    if i % 2 == 0:
        print(i, "Angka bilangan genap")
    else:
        print(i, "Angka bilangan ganjil")
    
    i += 1
   
# Nomor 4
secret_number = 108
print("""
+=============================+
| Selamat Datang di Game Pesulap |
| Tebak angka rahasia saya!      |
+=============================+
""")

# Mulai perulangan
while True:
    # Meminta input user
    tebakan = int(input("Masukkan angka tebakanmu: "))

    # Cek apakah tebakan benar
    if tebakan == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break  # keluar dari loop
    else:
        print("hahaha! kamu nyangkut deh di Loop saya")

# Nomor 5
a = 90
b = 80
c = 70
d = 85
e = 95

nilai = [a, b, c, d, e]

nilai_terbesar = nilai[0]
for angka in nilai:
    if angka > nilai_terbesar:
        nilai_terbesar = angka
print("Nilai terbesar:", nilai_terbesar)

# Nomor 6
hasil = 1
for expo in range(11):
    print("2 pangkat", expo, "adalah", hasil)
    hasil *= 2

# Nomor 7
print("Instruksi break")
for i in range(1, 10):
    if i == 5:
        break
    print(i)
print("Perulangan berhenti karena break\n")

print("Contoh continue")
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
print("Angka 5 dilewati karena continue")

# Nomor 8
secret_number = 4
print("=== Game Tebak Angka Rahasia Pesulap ===")
print("Pesulap telah memilih sebuah angka antara 1 sampai 10")
print("Coba tebak angka tersebut!")
while True:
    tebakan = int(input("Masukkan tebakan kamu: "))
    
    if tebakan == secret_number:
        print("Selamat! Tebakan kamu benar!")
        break
    else:
        print("Salah! Coba tebak lagi.")
		
# Nomor 9
kata = input("Masukkan sebuah kata: ")
kata = kata.upper()
for huruf in kata:
    if huruf == "A" or huruf == "I" or huruf == "U" or huruf == "E" or huruf == "O":
        continue
    elif huruf.isalpha():
        print(huruf)
    else:
        print(huruf)
		
# Nomor 10
i = 1
while i < 5:
    print(i)
    i = i + 1
else:
    print("else", i)
	
# Nomor 11
i = 30
for i in range(1, 6):
    print("Angka:", i)
else:
    print("Perulangan selesai")
	
# Nomor 12
a = 12
b = 2
print(a > 2 and b < 12)
print(a < 2 or b < 12)
print(not(a > 2))

# Nomor 13
a = 12
b = 4
print("AND :", a & b)
print("OR :", a | b)
print("NOT :", ~a)  # Diperbaiki karena ~ adalah unary operator
print("XOR :", a ^ b)

# Nomor 14
angka = 8
print("Left shift:", angka << 1)
print("Right shift:", angka >> 1)

# Nomor 15
x = 4
y = 1
a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2
print(a, b, c, d, e, f)