import math

def hitung_dan_cetak_volume_tabung(jari_jari, tinggi):
    volume = math.pi * jari_jari**2 * tinggi
    print(f"Volume Tabung dengan jari - jari {jari_jari} dan tinggi {tinggi} adalah {volume:.2f} kubik satuan.")

def hitung_dan_cetak_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    print(f"Volume Balok dengan panjang {panjang}, lebar {lebar}, tinggi {tinggi} adalah {volume} kubik satuan.")

print("Pilih bentuk geometri")
print("1. Tabung")
print("2. Balok")

pilihan = input("Masukan pilihan (1/2): ")

if pilihan == "1":
    jari_jari = float(input("Masukan jari - jari tabung: "))
    tinggi = float(input("Masukan tinggi tabung: "))
    hitung_dan_cetak_volume_tabung(jari_jari, tinggi)
elif pilihan == "2":
    panjang = float(input("Masukan panjang balok: "))
    lebar = float(input("Masukan lebar balok: "))
    tinggi = float(input("Masukan tinggi balok: "))
    hitung_dan_cetak_volume_balok(panjang, lebar, tinggi)
else:
    print("Pilihan tidak valid")