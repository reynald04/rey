import tkinter as tk # mengimport module tkinter
from tkinter import ttk # import ttk() widget
from tkinter.messagebox import showinfo

# init
window = tk.Tk() # membuat object window berisi Tk()
window.configure(bg="white") # mengubah background window menjadi putih
window.geometry ("300x200") # mengubah size window dalam sebuah pixel
window.resizable(False,False) # window x,y tidak bisa di resize
window.title("Sapa") # mengubah title window

# variabel
NAMA_DEPAN = tk.StringVar() #membuat constant
NAMA_BELAKANG = tk.StringVar() #membuat constant

# fungsi
def tombol_click():
    pesan=f"Hello {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Have a nice day"
    showinfo(title="Hi",message=pesan)

# frame input
input_frame = ttk.Frame(window) # mengggunakan widget ttk untuk memakai frameyang akan berisi window
input_frame.pack(padx=10, pady=10, fill="x", expand=True) # membuat layout dengan pack

# komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan: ") # label text aisha pada frame input
nama_depan_label.pack(padx=10, fill="x", expand=True) # membuat pack layout untuk label
# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN) # entry akan masuk ke constant NAMA_DEPAN
nama_depan_entry.pack(padx=10, fill="x", expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang: ") # label text aisha pada frame input
nama_belakang_label.pack(padx=10, fill="x", expand=True) # membuat pack layout untuk label
# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG) # entry akan masuk ke constant NAMA_BELAKANG
nama_belakang_entry.pack(padx=10, fill="x", expand=True)
# 5. Tombol
tombol = ttk.Button(input_frame, text="Sapa!", command=tombol_click)
tombol.pack(fil='x', expand=True, padx=10, pady=10)

window.mainloop() # metode mainloop menjalankan program hingga apk close