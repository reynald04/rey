from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Aplikasi Kasir')

JERUK = StringVar()
MANGGA = StringVar()
STRAWBERRY = StringVar()
BLUEBERRY = StringVar()
tekstotal = StringVar()
teksaung = StringVar()
total = 0

def totalbeli():
    global JERUK, MANGGA, STRAWBERRY, BLUEBERRY, tekstotal, total
    hJERUK = int(JERUK.get()) * 15000
    hMANGGA = int(MANGGA.get()) * 15000
    hSTRAWBERRY = int(STRAWBERRY.get()) * 20000
    hBLUEBERRY = int(BLUEBERRY.get()) * 20000
    total = hJERUK + hMANGGA + hSTRAWBERRY + hBLUEBERRY
    tekstotal.set(str(total))

def kembalian():
    global total
    uang = int(teksaung.get())

    if uang >= total:
        kembalian = uang - total
        messagebox.showinfo(message='Kembalian kamu sebesar {}'.format(str(kembalian)))
    else:
        messagebox.showerror(message='maaf uang kamu kurang')

def clear():
        JERUK.set('0')
        MANGGA.set('0')
        STRAWBERRY.set('0')
        BLUEBERRY.set('0')
        tekstotal.set('0')
        teksaung.set('0')


app.geometry('750x600')
app.configure(bg='#010101')

Label(app, text='KASIR TOKO REY', bg='#010101', foreground='#fef5ac', font='arial 18 bold').place(x=200,y=30)

Label(app, text='1. JERUK', bg='#010101', foreground='#fef5ac', font='arial 13 bold').place(x=100,y=100)
Label(app, text='2. MANGGA', bg='#010101', foreground='#fef5ac', font='arial 13 bold').place(x=100,y=140)
Label(app, text='3. STRAWBERRY', bg='#010101', foreground='#fef5ac', font='arial 13 bold').place(x=100,y=180)
Label(app, text='4. BLUEBERRY', bg='#010101', foreground='#fef5ac', font='arial 13 bold').place(x=100,y=220)

Label(app, text='Rp. 15.000/KG', bg='#010101', foreground='#fef5ac', font='arial 13 bold').place(x=350,y=100)
Label(app, text='Rp. 15.000/KG', bg='#010101', foreground='#fef5ac', font='arial 13 bold').place(x=350,y=140)
Label(app, text='Rp. 20.000/PACK', bg='#010101', foreground='#fef5ac', font='arial 13 bold').place(x=350,y=180)
Label(app, text='Rp. 20.000/PACK', bg='#010101', foreground='#fef5ac', font='arial 13 bold').place(x=350,y=220)

Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=JERUK, command=totalbeli).place(x=550,y=100)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=MANGGA, command=totalbeli).place(x=550,y=140)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=STRAWBERRY, command=totalbeli).place(x=550,y=180)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=BLUEBERRY, command=totalbeli).place(x=550,y=220)

Label(app, text='Masukan Uang Anda', bg='#010101', foreground='#fef5ac', font='arial 12 ').place(x=100,y=280)

Entry(app, textvariable=teksaung).place(x=100,y=300)

Label(app, text='Rp. ', bg='#010101', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=300)
Label(app, textvariable=tekstotal, bg='#010101', foreground='#fef5ac', font='arial 12 bold').place(x=380,y=300)

Button(app, text='Total', foreground='white', bg='#36ae7c', width=10, command=kembalian).place(x=100,y=400)
Button(app, text='Clear', foreground='white', bg='#ff1e1e', width=10, command=clear).place(x=250,y=400)


app.mainloop()