# Nomor 1
def selamat_ulang_tahun(harapan=True):
    print("Pertama aku ingin mempunyai duit")
    print("Dua aku ingin pergi ke jepang")
    print("Tiga aku ingin husbu ku nyata")
    if not harapan:
        return
    print("Selamat Ulang Tahun!")

selamat_ulang_tahun()  # pemanggil tanpa argumen

# Nomor 2
def selamat_ulang_tahun(harapan=True):
    print("Pertama aku ingin mempunyai duit")
    print("Dua aku ingin pergi ke jepang")
    print("Tiga aku ingin husbu ku nyata")
    if not harapan:
        return
    print("Selamat Ulang Tahun!")

selamat_ulang_tahun(False)  # pemanggil dengan argumen False

# Nomor 3
def fungsi_malas():
    return 123

x = fungsi_malas()
print(x)

# Nomor 4
def fungsi_malas():
    print("Mode Malas")
    return 123

fungsi_malas()

# Nomor 5
def fungsi_aneh(n):
    if (n % 2 == 0):
        return True

print(fungsi_aneh(12)) 
print(fungsi_aneh(13)) 

# Nomor 6
def penjumlahan_list(lst):
    s = 0
    for elemen in lst:
        s += elemen
    return s

print(penjumlahan_list([20, 14, 15]))

# Nomor 7
def penjumlahan_list(lst):
    s = 0
    for elemen in lst:
        s += elemen
    return s

print(penjumlahan_list([7]))

# Nomor 8
def fungsi_list_aneh(n):
    list_aneh = []
    for i in range(0, n):
        list_aneh.insert(0, i)
    return list_aneh

print(fungsi_list_aneh(5))

# Nomor 9
def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False

data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]  # Disamakan jumlah elemen dan kebenarannya

for i in range(len(data_uji)):
    th = data_uji[i]
    hasil = tahun_kabisat(th)
    
    print(f"{th} ->", end=" ")
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal") 

# Nomor 10
def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False

def hari_didalam_bulan(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if tahun_kabisat(tahun): 
            return 29          
        else:                   
            return 28          

data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

for i in range(len(data_uji)):
    thn = data_uji[i]
    bln = data_bulan[i]
    hasil = hari_didalam_bulan(thn, bln)
    
    print(f"{thn}, {bln} ->", end=" ")
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")

# Nomor 11
def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False

def hari_dalam_bulan(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        return 29 if tahun_kabisat(tahun) else 28
    return None

def hari_dalam_tahun(tahun, bulan, hari):
    maks_hari = hari_dalam_bulan(tahun, bulan)
    if maks_hari is None or hari < 1 or hari > maks_hari:
        return None

    total = 0
    for b in range(1, bulan):
        total += hari_dalam_bulan(tahun, b)
    
    total += hari
    return total

print(hari_dalam_tahun(2000, 12, 31))

# Nomor 12
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
		
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            return False
    return True

for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()  # Baris baru setelah loop selesai

# Nomor 13
# Kode nomor 13 identik dengan nomor 12, dirapikan kembali strukturnya
for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()

# Nomor 14
def Liter100km_ke_mpg(liter):
    # 100 km dalam mil = 100.000 meter / 1609.344 meter    
    mil = 100 / 1.609344
    # Jumlah galon = liter yang digunakan / 3.785411784 liter    
    galon = liter / 3.785411784
    return mil / galon

def mpg_ke_Liter100km(mpg):
    # 1 galon dalam liter    
    liter = 3.785411784
    # mil dalam satuan 100km = mpg * 1.609344 / 100    
    km100 = (mpg * 1.609344) / 100
    return liter / km100

# Output hasil konversi
print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.0))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))