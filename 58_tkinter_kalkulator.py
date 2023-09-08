import tkinter as tk
from tkinter import ttk

# fungsi untuk menghitung hasil
def hitung():
    angka1 = float(angka1_entry.get())
    angka2 = float(angka2_entry.get())
    operator = operator_combobox.get()

    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        hasil = angka1 / angka2
    else:
        hasil = "Operator tidak valid"

    hasil_label.config(text=str(hasil))

# membuat jendela
window = tk.Tk()
window.title("Kalkulator")

# frmae input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10)

# entry angka 1
angka1_label = ttk.Label(input_frame, text="Angka 1: ")
angka1_label.grid(row=0, column=0, sticky="W")
angka1_entry = ttk.Entry(input_frame)
angka1_entry.grid(row=0, column=1)

# entry angka 2
angka2_label = ttk.Label(input_frame, text="Angka 2: ")
angka2_label.grid(row=1, column=0, sticky="W")
angka2_entry = ttk.Entry(input_frame)
angka2_entry.grid(row=1, column=1)

# combobox operator
operator_label = ttk.Label(input_frame, text="Operator: ")
operator_label.grid(row=2, column=0, sticky="W")
operator_combobox = ttk.Combobox(input_frame, values=("+", "-", "*", "/"))
operator_combobox.grid(row=2, column=1)

# tombol hitung 
hitung_button = ttk.Button(window, text="Hitung", command=hitung)
hitung_button.pack(padx=10)

# label hasil
hasil_label = ttk.Label(window, text="")
hasil_label.pack()

window.mainloop()