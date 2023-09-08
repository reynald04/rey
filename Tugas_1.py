def hitung_dan_cetak_persegi(sisi):
    luas = sisi ** 2
    keliling = 4 * sisi
    print(f"Luas persegi dengan sisi {sisi} adalah {luas}")
    print(f"Keliling persegi dengan sisi {sisi} adalah {keliling}")


def hitung_dan_cetak_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")
    print(f"Keliling persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {keliling}")


def hitung_dan_cetak_trapesium(panjang_sisi_atas, panjang_sisi_bawah, tinggi, sisi_miring):
    luas = 0.5 * (panjang_sisi_atas + panjang_sisi_bawah) * tinggi
    keliling = panjang_sisi_atas + panjang_sisi_bawah + (2 * sisi_miring)
    print(f"Luas trapesium dengan panjang sisi atas {panjang_sisi_atas}, panjang sisi bawah {panjang_sisi_bawah}, tinggi {tinggi}, dan sisi miring {sisi_miring} adalah {luas}")
    print(f"Keliling trapesium dengan panjang sisi atas {panjang_sisi_atas}, panjang sisi bawah {panjang_sisi_bawah}, tinggi {tinggi}, dan sisi miring {sisi_miring} adalah {keliling}")


print("Pilih bentuk geometri:")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Trapesium")

pilihan = input("Masukkan pilihan (1/2/3): ")

if pilihan == "1":
    sisi = float(input("Masukkan panjang sisi persegi: "))
    hitung_dan_cetak_persegi(sisi)
elif pilihan == "2":
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    hitung_dan_cetak_persegi_panjang(panjang, lebar)
elif pilihan == "3":
    panjang_sisi_atas = float(input("Masukkan panjang sisi atas trapesium: "))
    panjang_sisi_bawah = float(input("Masukkan panjang sisi bawah trapesium: "))
    tinggi = float(input("Masukkan tinggi trapesium: "))
    sisi_miring = float(input("Masukkan panjang sisi miring trapesium: "))
    hitung_dan_cetak_trapesium(panjang_sisi_atas, panjang_sisi_bawah, tinggi, sisi_miring)
else:
    print("Pilihan tidak valid.")