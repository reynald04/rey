import PySimpleGUI as sg

layout = [[sg.Button('Klik Saya')]]

window = sg.Window("Contoh Program PySimpleGUI", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Klik Saya':
        print("Tombol diklik")

window.close()
