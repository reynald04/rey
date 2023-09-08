# Fungsi Untuk Menghitung rata-rata dari sejumlah angka

def hitung_rata_rata(angka):
    total = sum(angka)
    rata_rata = total / len(angka)
    return rata_rata

# Fungsi untuk mendapatkan input angka dari pengguna
def input_angka():
    angka = []
    while True:
        try:
            bilangan = float(input("Masukan angka (0 untuk mengakhiri): "))
            if bilangan == 0:
                break
            angka.append(bilangan)
        except ValueError:
            print("Masukan angka yang valid.")

    return angka

# Program Utama
if __name__ == "__main__":
    print("Program menghitung Rata-rata")
    daftar_angka = input_angka()

    if daftar_angka:
        rata_rata = hitung_rata_rata(daftar_angka)
        print(f"Rata-rata dari angka-angka yang dimasukkan adalah: {rata_rata:.2f}")
    else:
        print("Tidak ada angka yang dimasukkan.")