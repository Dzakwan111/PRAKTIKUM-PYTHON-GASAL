# Definisi tuple
nama_makanan = ("Nasi Goreng", "Ayam Bakar", "Sate", "Kebab", "Pecel")

# Mengakses elemen tuple
print("Makanan pertama:", nama_makanan[0])
print("Makanan kedua:", nama_makanan[1])

# Menggabungkan dua tuple
makanan_favorit = ("Nasi Goreng", "Ayam Bakar")
makanan_tidak_favorit = ("Sate", "Kebab", "Pecel")
makanan_semua = makanan_favorit + makanan_tidak_favorit
print("Makanan semua:", makanan_semua)

# Menghitung jumlah elemen pada tuple
jumlah_makanan = len(nama_makanan)
print("Jumlah makanan:", jumlah_makanan)

# Mencari indeks elemen pada tuple
indeks_ayam_bakar = nama_makanan.index("Ayam Bakar")
print("Indeks Ayam Bakar:", indeks_ayam_bakar)

# Mengganti elemen pada tuple (tidak mungkin karena tuple imutabel)
# nama_makanan[0] = "Nasi Uduk"  # Akan menimbulkan error

tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])