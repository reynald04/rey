nama = str(input("Masukan Nama: "))
Gaji_Pokok = float(input("Masukan Gaji Pokok: "))

tunjangan = 0.02 * Gaji_Pokok
pajak = 0.15 * (Gaji_Pokok + tunjangan)
Gaji_Bersih = Gaji_Pokok + tunjangan - pajak

print(nama)
print(Gaji_Pokok)
print(Gaji_Bersih)