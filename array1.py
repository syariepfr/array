#deklarasi array untuk menyimpan nilai
nilai_siswa = []

#meminta input nilai dari pengguna
for i in range(5):
    nilai = float(input(f"Masukan nilai siswa ke-{i+1}: "))
    nilai_siswa.append(nilai)

#Menghitung total nilai
total_nilai = sum(nilai_siswa)

#Menghitung rata-rata
rata_rata = total_nilai / len(nilai_siswa)

#Menampilkan hasil Rata-rata
print(f"Rata-rata nilai siswa adalah: (rata_rata)")