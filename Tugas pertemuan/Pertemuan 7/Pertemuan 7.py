# Nomor 1
angka = [90, 95, 60, 80, 10]
print("isi dari list awal:", angka)
angka[0] = 111
print("\nisi dari list sebelumnya:", angka)
angka[1] = angka[4]
print("isi dari list sekarang:", angka)

# Nomor 2
angka = [0, 1, 2, 3, 4]
print(angka[0]) 
print(angka[2]) 

# Nomor 3
data = [0, 1, 2, 3, 4]
panjang = len(data) 
print(panjang) 
print("\npanjang list:", len(data))

# Nomor 4
angka = [90, 80, 65, 70, 23]
del angka[1]
print(angka)

# Nomor 5
data = [1, 2, 3, 4, 5]
print(data[-1])
print(data[-2])

# Nomor 6
topi_list = [1, 2, 3, 4, 5] # Langkah 1
topi_list[len(topi_list)//2] = int(input("Masukkan angka: "))  # Langkah 2
del topi_list[-1]  # Langkah 3
print(len(topi_list))
print(topi_list)

# Nomor 7
angka = [1, 2, 3]
print(len(angka))
print(angka)
angka.append(4)
print(len(angka))
print(angka)
angka.insert(1, 5)
print(len(angka))
print(angka)

# Nomor 8
my_list = [] 
for i in range(5):
    my_list.append(i + 1)
print(my_list)

# Nomor 9
my_list = [] 
for i in range(5):
    my_list.insert(0, i + 1)
print(my_list)

# Nomor 10
my_list = [10, 1, 8, 3, 5]
total = 0
for i in range(len(my_list)):
    total += my_list[i]
print(total)

# Nomor 11
my_list = [10, 1, 8, 3, 5]
total = 0
for i in my_list:
    total += i
print(total)

# Nomor 12
my_list = [1, 2, 3, 4, 5]
total = 0
for i in range(len(my_list)):
    total += my_list[i] * 2
print(my_list)

# Nomor 13
exo = []
print("Langkah 1:", exo)

exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("Langkah 2:", exo)

anggota_baru = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for nama in anggota_baru:
    exo.append(nama)
print("Langkah 3:", exo)

for nama in ["Kris", "Luhan", "Tao"]:
    if nama in exo:
        exo.remove(nama)
print("Langkah 4:", exo)

exo.insert(-2, "Xiumin")
print("Langkah 5: ", exo)
print("Jumlah anggota: ", len(exo))