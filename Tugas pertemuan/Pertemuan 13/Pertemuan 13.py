# Nomor 1
angka = (2, 4, 6, 8)
print(angka)


# Nomor 2
list_nahdiya = (1, 10, 100, 1000)
print(list_nahdiya)
print(list_nahdiya[-1])
print(list_nahdiya[1:])
print(list_nahdiya[:-2])


# Nomor 3
buku_komik_nahdiya = (1, 10, 100)
# buku_komik_nahdiya [10] = 1000  


# Nomor 4
List_Nahdiya1 = (1, 2)
List_Nahdiya2 = (3, 4)
print(len(List_Nahdiya1))
print(List_Nahdiya1 + List_Nahdiya2)
print(List_Nahdiya1 * 2)
print(1 in List_Nahdiya1)
print(5 not in List_Nahdiya1)


# Nomor 5
a = 10
b = 20
c = 30
a, b, c = c, b, a
print (a, b, c)


# Nomor 6
data_pribadi = {"nama": "Nahdiya", "umur": 19}
print(data_pribadi)


# Nomor 7
data = {"nama": "Nahdiya", "umur": 19}
print(data["nama"])
print(data["umur"])


# Nomor 8
menu_kafe = {
    "item": "Caramel Macchiato",
    "harga": 35000,
    "kategori": "Kopi"
}
print(menu_kafe.keys())


# Nomor 9
menu_kafe = {
    "item": "Caramel Macchiato",
    "harga": 35000,
    "kategori": "Kopi"
}
print(menu_kafe.values())


# Nomor 10
menu_kafe = {
    "item": "Caramel Macchiato",
    "harga": 35000,
    "kategori": "Kopi"
}
print(menu_kafe.items())


# Nomor 11
tim_proyek = {
    "ketua": "Nahdiya",
    "anggota1": "Farras"
}
# Menambah anggota baru
tim_proyek.update({"anggota2": "Dias"})
print(tim_proyek)


# Nomor 12
tim_proyek = {
    "ketua": "Nahdiya",
    "anggota1": "Farras"
}

tim_proyek.update({"anggota2": "Dias"})
print(tim_proyek)

tim_proyek.popitem()
print(tim_proyek)


# Nomor 13
buku = {
    "judul": "Laskar Pelangi",
    "status": "Tersedia"
}

buku["status"] = "Dipinjam"
buku["peminjam"] = "Nahdiya"
print(buku)


# Nomor 14
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil pembagian:", hasil)
except ValueError:
    print("Harus berupa angka!")
	

# Nomor 15
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil pembagian:", hasil)
except ValueError:
    print("Harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol!")