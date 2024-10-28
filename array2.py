#Deklarasi Matriks
matriks = []

#Meminta input penggua untuk mengisi matriks 3x3
print("masukan elemen untuk matriks 3x3:")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"Masukan Elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks.append(baris)

#Transpose Matriks
transpose = []
for i in range(3):
    baris = []
    for j in range(3):
        baris.append(matriks[j][i])
    transpose.append(baris)

#Menampilkan hasil Transpose
print("\nHasil transpose matriks:")
for baris in transpose:
    print(baris)
