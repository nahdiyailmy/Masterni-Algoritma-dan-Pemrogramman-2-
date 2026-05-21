# Nomor 1
pangkat = [x ** 2 for x in range(10)] 
print(pangkat)

dua_pangkat = [2 ** i for i in range(8)] 
print(dua_pangkat)

ganjil = [x for x in pangkat if x % 2 != 0] 
print(ganjil)

# Nomor 2
# Definisi simbol sebagai string
KOSONG = " . "
Benteng = " ♖ "
Kuda = "♘ "

# Membuat papan catur 8x8
papan_catur = []
for i in range(8):
    baris = [KOSONG for j in range(8)]
    papan_catur.append(baris)

# Mengisi Benteng 
papan_catur[0][0] = Benteng
papan_catur[0][7] = Benteng
papan_catur[7][0] = Benteng
papan_catur[7][7] = Benteng

# Mengisi Kuda 
papan_catur[4][2] = Kuda

# Menampilkan papan
for baris in papan_catur:
    print(" ".join(baris))

# Nomor 3
# Membuat data kamar hotel : gedung, 15 lantai, 20 kamar per lantai
kamar = [[[False for k in range(20)] for j in range(15)] for i in range(3)]

# Index: Gedung 2 (index 1), Lantai 10 (index 9), Kamar 14 (index 13)
kamar[1][9][13] = True
kamar[0][4][1] = False

tersedia = 0
for no_kamar in range(20):
    if not kamar[2][14][no_kamar]:
        tersedia += 1

print("\nSetelah ada tamu:")
print("Gedung 2, Lantai 10, Kamar 14:", kamar[1][9][13]) 
print("Gedung 1, Lantai 5, Kamar 2:", kamar[0][4][1])

# Nomor 4
def pesan(angka):
    print("Masukkan sebuah angka:", angka)

pesan(10)

# Nomor 5
hasil = [i * 3 for i in range(1, 11) if i % 2 == 0]
print(hasil)

# Nomor 6
# Membuat array 2 dimensi 3x3 berisi angka 1 sampai 9
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Isi array 2 dimensi 3x3:")
for i in range(len(array_2d)):
    for j in range(len(array_2d[i])):
        print(array_2d[i][j], end=" ")
    print() 
	
# Nomor 7
data = [[2, 4], [6, 8], [10, 12]]
flatten = [x for sublist in data for x in sublist]
print(flatten)

# Nomor 8
# fungsi luas persegi panjang
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

# Memanggil fungsi dan menyimpan hasilnya
p = 8
l = 5
hasil_luas = hitung_luas(p, l)

print(f"Panjang: {p}") 
print(f"Lebar: {l}")
print(f"Luas Persegi Panjang adalah = {p} x {l} = {hasil_luas}")