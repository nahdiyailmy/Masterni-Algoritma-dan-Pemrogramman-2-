# ============================================
# SISTEM KASIR TIKET BIOSKOP
# Mata Kuliah : Algoritma & Pemrograman II
# Bahasa      : Python
# ============================================

# ---------- GLOBAL VARIABLE ----------
data_transaksi = []  # list of dictionary

# ---------- TUPLE DATA ----------
DAFTAR_FILM       = ("Ghost in The Cell", "Mortal Kombat II", "Tumbal Proyek",
                     "Salmokji: Whispering Water", "Dilan ITB 1997")
NAMA_STUDIO       = ("Reguler", "IMAX", "The Premiere")
HARGA_PER_STUDIO  = (50000, 75000, 100000)
DAFTAR_SNACK      = ("Popcorn Caramel", "Popcorn Asin", "Nachos", "Cola", "Mineral")
HARGA_SNACK       = (23000, 20000, 25000, 10000, 7000)
METODE_PEMBAYARAN = ("Cash", "QRIS", "Debit")
BARIS_KURSI       = ("A", "B", "C", "D", "E", "F")
KOLOM_KURSI       = (1, 2, 3, 4, 5, 6, 7, 8)

# ---------- KONSTANTA TAMPILAN ----------
LEBAR = 65

def garis_atas():
    print("┌" + "─" * (LEBAR - 2) + "┐")

def garis_tengah():
    print("├" + "─" * (LEBAR - 2) + "┤")

def garis_bawah():
    print("└" + "─" * (LEBAR - 2) + "┘")

def baris_isi(teks):
    print(f"│ {teks:<{LEBAR - 3}}│")

def baris_tengah(teks):
    print(f"│{teks.center(LEBAR - 2)}│")

# ---------- FUNGSI VALIDASI INPUT ----------
def input_angka(prompt, batas_min=1, batas_max=None):
    while True:
        try:
            nilai = int(input(prompt))
            if nilai < batas_min:
                print(f"  Input minimal {batas_min}")
            elif batas_max is not None and nilai > batas_max:
                print(f"  Input harus antara {batas_min} - {batas_max}")
            else:
                return nilai
        except ValueError:
            print("  Input harus berupa angka!")

# ---------- FUNGSI TAMPILKAN LAYOUT KURSI ----------
def tampilkan_layout_kursi(kursi_terisi):
    print()
    garis_atas()
    baris_tengah("[ LAYAR BIOSKOP ]")
    garis_tengah()

    for baris in BARIS_KURSI:
        baris_str = f"{baris}  "
        for i, kolom in enumerate(KOLOM_KURSI):
            kode = f"{baris}{kolom}"
            if i == 4:
                baris_str += "  "
            baris_str += "[XXX] " if kode in kursi_terisi else f"[{kode:<3}] "
        baris_isi(baris_str.rstrip())

    garis_tengah()
    baris_isi("Keterangan: [XXX] = Terisi  |  [A1] = Tersedia")
    garis_bawah()
    print()

# ---------- FUNGSI PILIH KURSI ----------
def pilih_kursi(jumlah, kursi_terisi):
    kursi_dipilih = []
    print(f"  Pilih {jumlah} kursi:")

    for i in range(jumlah):
        while True:
            kode = input(f"  Kursi ke-{i+1} (contoh: A1, B5) : ").strip().upper()
            baris     = kode[0] if kode else ""
            kolom_str = kode[1:]

            if len(kode) < 2:
                print("  Format salah! Contoh: A1, B5")
            elif baris not in BARIS_KURSI:
                print(f"  Baris tidak valid! Pilih antara {BARIS_KURSI[0]}-{BARIS_KURSI[-1]}")
            elif not kolom_str.isdigit() or int(kolom_str) not in KOLOM_KURSI:
                print(f"  Kolom tidak valid! Pilih antara {KOLOM_KURSI[0]}-{KOLOM_KURSI[-1]}")
            elif kode in kursi_terisi:
                print("  Kursi sudah terisi, pilih kursi lain!")
            elif kode in kursi_dipilih:
                print("  Kursi sudah kamu pilih sebelumnya!")
            else:
                kursi_dipilih.append(kode)
                print(f"  Kursi {kode} berhasil dipilih.")
                break

    return kursi_dipilih

# ---------- FUNGSI PILIH SNACK ----------
def pilih_snack():
    print()
    garis_atas()
    baris_tengah("SNACK")
    garis_tengah()
    for i, snack in enumerate(DAFTAR_SNACK):
        baris_isi(f"{i+1}. {snack:<18} Rp{HARGA_SNACK[i]:,}")
    baris_isi("0. Tidak mau snack / Selesai")
    garis_bawah()

    snack_dipilih = []
    total_snack   = 0

    while True:
        pilihan = input_angka("  Pilih Snack (0 untuk selesai) : ", 0, len(DAFTAR_SNACK))
        if pilihan == 0:
            break
        nama_snack   = DAFTAR_SNACK[pilihan - 1]
        harga_snack  = HARGA_SNACK[pilihan - 1]
        snack_dipilih.append(nama_snack)
        total_snack += harga_snack
        print(f"  {nama_snack} ditambahkan. (Rp{harga_snack:,})")

    return {"nama": snack_dipilih, "total": total_snack}

# ---------- FUNGSI INPUT TRANSAKSI ----------
def input_transaksi():
    # Kumpulkan kursi yang sudah terisi
    kursi_terisi = []
    for trx in data_transaksi:
        kursi_terisi.extend(trx["kursi"])

    # Pilih film
    print()
    garis_atas()
    baris_tengah("FILM YANG SEDANG TAYANG")
    garis_tengah()
    for i, film in enumerate(DAFTAR_FILM):
        baris_isi(f"{i+1}. {film}")
    garis_bawah()

    pilihan_film = input_angka(f"  Pilih Film (1-{len(DAFTAR_FILM)})    : ", 1, len(DAFTAR_FILM))
    film   = DAFTAR_FILM[pilihan_film - 1]
    jumlah = input_angka("  Jumlah Tiket        : ", 1)

    # Pilih studio
    print()
    garis_atas()
    baris_tengah("PILIHAN STUDIO")
    garis_tengah()
    for i, nama in enumerate(NAMA_STUDIO):
        baris_isi(f"{i+1}. {nama:<12} Rp{HARGA_PER_STUDIO[i]:,}")
    garis_bawah()

    pilihan_studio = input_angka("  Pilih Studio (1-3)  : ", 1, len(NAMA_STUDIO))
    studio = NAMA_STUDIO[pilihan_studio - 1]
    harga  = HARGA_PER_STUDIO[pilihan_studio - 1]

    # Pilih kursi
    tampilkan_layout_kursi(kursi_terisi)
    kursi_dipilih = pilih_kursi(jumlah, kursi_terisi)

    # Pilih snack
    snack = pilih_snack()

    # Hitung total
    total_tiket = harga * jumlah
    total_snack = snack["total"]
    total       = total_tiket + total_snack

    # Pilih metode pembayaran
    print()
    garis_atas()
    baris_tengah("METODE PEMBAYARAN")
    garis_tengah()
    baris_isi(f"Total Tiket          : Rp{total_tiket:,.0f}")
    baris_isi(f"Total Snack          : Rp{total_snack:,.0f}")
    garis_tengah()
    baris_isi(f"Total yang dibayar   : Rp{total:,.0f}")
    garis_tengah()
    for i, metode_item in enumerate(METODE_PEMBAYARAN):
        baris_isi(f"{i+1}. {metode_item}")
    garis_bawah()

    pilihan_bayar = input_angka("  Pilih Pembayaran (1-3) : ", 1, len(METODE_PEMBAYARAN))
    metode = METODE_PEMBAYARAN[pilihan_bayar - 1]

    if metode == "Cash":
        bayar = input_angka("  Uang yang dibayar   : Rp", total)
        print(f"  Kembalian           : Rp{bayar - total:,.0f}")

    # Simpan transaksi
    data_transaksi.append({
        "film"  : film,
        "studio": studio,
        "kursi" : kursi_dipilih,
        "snack" : snack["nama"],
        "metode": metode,
        "total" : total
    })

    # Struk konfirmasi
    print()
    garis_atas()
    baris_tengah("TRANSAKSI BERHASIL")
    garis_tengah()
    baris_isi(f"Film    : {film}")
    baris_isi(f"Studio  : {studio}")
    baris_isi(f"Kursi   : {', '.join(kursi_dipilih)}")
    if snack["nama"]:
        baris_isi(f"Snack   : {', '.join(snack['nama'])}")
    else:
        baris_isi("Snack   : -")
    baris_isi(f"Metode  : {metode}")
    garis_tengah()
    baris_isi(f"Total   : Rp{total:,.0f}")
    garis_bawah()
    print()

# ---------- FUNGSI TAMPILKAN TRANSAKSI ----------
def tampilkan_data():
    print()
    garis_atas()
    baris_tengah("DATA TRANSAKSI TIKET")
    garis_tengah()

    if not data_transaksi:
        baris_isi("Belum ada data transaksi.")
    else:
        baris_isi(f"{'Film':<22} {'Studio':<11} {'Kursi':<8} {'Metode':<6} {'Total':>9}")
        garis_tengah()
        for trx in data_transaksi:
            kursi_str = ", ".join(trx["kursi"])
            baris_isi(f"{trx['film']:<22} {trx['studio']:<11} {kursi_str:<8} {trx['metode']:<6} Rp{trx['total']:>6,.0f}")

    garis_bawah()
    print()

# ---------- FUNGSI TOTAL PENDAPATAN ----------
def total_pendapatan():
    print()
    garis_atas()
    baris_tengah("TOTAL PENDAPATAN CINEMA")
    garis_tengah()

    if not data_transaksi:
        baris_isi("Belum ada transaksi.")
    else:
        total_semua = sum(trx["total"] for trx in data_transaksi)
        baris_isi(f"Total Pendapatan : Rp{total_semua:,.0f}")

    garis_bawah()
    print()

# ---------- MENU UTAMA ----------
def menu():
    while True:
        print()
        garis_atas()
        baris_tengah("CINEMA STAR")
        garis_tengah()
        baris_isi("1. Beli Tiket")
        baris_isi("2. Tampilkan Transaksi")
        baris_isi("3. Total Pendapatan")
        baris_isi("4. Keluar")
        garis_bawah()

        pilihan = input("  Pilih menu (1-4): ")

        if pilihan == "1":
            input_transaksi()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            total_pendapatan()
        elif pilihan == "4":
            print()
            garis_atas()
            baris_tengah("Terima kasih!!")
            garis_bawah()
            print()
            break
        else:
            print("  Pilihan tidak valid!\n")

# ---------- PROGRAM UTAMA ----------
menu()