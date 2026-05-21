# Nomor 1
my_list = [8, 10, 6, 2, 4]  # list untuk diurutkan
swapped = True              # Inisiasi awal untuk memasuki loop
while swapped:
    swapped = False         # Menganggap tiada penukaran berlaku
    for i in range(len(my_list) - 1):  # Perulangan sepanjang elemen list
        if my_list[i] > my_list[i + 1]:  # Bandingkan elemen semasa dengan yang di depan
            swapped = True               # Menandakan berlaku penukaran
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Proses pertukaran tempat
print(my_list)  # Mencetak list yang telah terurut 

# Nomor 2
swapped = True
my_list = []
num = int(input("Masukkan panjang elemen list yang akan diurutkan: "))
for i in range(num):
    val = float(input("Masukkan elemen list: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print("\nSorted:")
print(my_list)

# Nomor 3
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# Nomor 4
lst = [5, 3, 1, 2, 4]
lst.reverse()
print(lst)

# Nomor 5
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2) 

# Nomor 6
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# Nomor 7
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# Nomor 8
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

# Nomor 9
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

# Nomor 10
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

# Nomor 11
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(my_list)

# Nomor 12
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# Nomor 13
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# Nomor 14
my_list = [10, 8, 6, 4, 2]
my_list.clear()  # Menggunakan .clear() agar variabel tidak hilang total dari memori
print(my_list)

# Nomor 15
my_list = [5, 2, 9, 1, 5, 6]
print(5 in my_list)

# Nomor 16
my_list = [0, 3, 12, 8, 2]
print(10 not in my_list)

# Nomor 17
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > largest:   
        largest = my_list[i]
print(largest)
		
# Nomor 18
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in my_list:
    if i > largest:   
        largest = i  # Diperbaiki agar tidak merusak list asli
print(largest)

# Nomor 19
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemen ditemukan pada index ke-", i)
else:
    print("Tidak ada di dalam list")

# Nomor 21
lotre = [3, 7, 11, 42, 34, 49]
lotreSudahKeluar = [5, 9, 11, 42, 3, 49]
tebakanBenar = 0
for angka in lotre:
    if angka in lotreSudahKeluar:
        tebakanBenar += 1
print(f"Jumlah tebakkan yang benar : {tebakanBenar}")

# Nomor 22
sebuahList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
listSementara = []
for angka in sebuahList:
    if angka not in listSementara:
        listSementara.append(angka)
print("Hasil list unik:", listSementara)