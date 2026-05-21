# Nomor 1
def penjumlahan(x):
    bilangan = 7 
    return x + 7

print(penjumlahan(4))


# Nomor 2
bilangan = 2
def perkalian_bilangan(x):
    return x * bilangan

print(perkalian_bilangan(7))


# Nomor 3
def perkalian_bilangan(x):
    bilangan = 5  
    return x * bilangan

print(perkalian_bilangan(7))


# Nomor 4
bilangan = 2
print(bilangan) 

def return_bilangan():
    global bilangan
    bilangan = 5
    return bilangan

print(return_bilangan()) 
print(bilangan) 


# Nomor 5 (Tetap Asli - Hanya Dirapikan Barisnya)
def hitung_imt(berat, tinggi):
    imt = berat / (tinggi * tinggi)
    return imt

berat = float(input("Masukkan berat (kg): "))
tinggi = float(input("Masukkan tinggi (m): "))
imt_user = hitung_imt(berat, tinggi)
kategori = ["Normal", "Gemuk", "Obesitas"]

if 18.5 <= imt_user <= 25.0:
    print("Index massa tubuh anda adalah", imt_user, "termasuk kategori", kategori)
elif 25.0 < imt_user <= 27.0:
    print("Index massa tubuh anda adalah", imt_user, "termasuk kategori", kategori[1])
else:
    print("Index massa tubuh anda adalah", imt_user, "termasuk kategori", kategori[2], ". Anda harus diet!")


# Nomor 6
def cek_segitiga(a, b, c):
    if a + b <= c: return False
    if b + c <= a: return False
    if c + a <= b: return False
    return True

print(cek_segitiga(1, 1, 1)) # True
print(cek_segitiga(1, 1, 3)) # False


# Nomor 7
def cek_segitiga(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(cek_segitiga(1, 1, 1)) # True
print(cek_segitiga(1, 1, 3)) # False


# Nomor 8
def cek_segitiga(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(cek_segitiga(1, 1, 1)) # True
print(cek_segitiga(1, 1, 3)) # False


# Nomor 9
def faktorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

n = int(input("Masukkan angka untuk faktorial: "))
print(n, "! =", faktorial(n))


# Nomor 10
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    elem_1 = elem_2 = 1
    hasil_jumlah = 0
    for i in range(3, n + 1):
        hasil_jumlah = elem_1 + elem_2
        elem_1, elem_2 = elem_2, hasil_jumlah
    return hasil_jumlah

for i in range(1, 10):
    print(i, "->", fibonacci(i))


# Nomor 11
def faktorial_rekursif(n):
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * faktorial_rekursif(n - 1)

print(faktorial_rekursif(6))


# Nomor 12
def fibonacci_rekursif(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)

print(fibonacci_rekursif(8))