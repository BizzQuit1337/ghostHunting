import PySimpleGUI as sg
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory (Main folder) and append it to sys.path
main_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(main_dir)

# Define the layout for the window
layout = [
    [sg.Text('Standard Mode')],
    [sg.Multiline(size=(40, 1), key='-TEXTBOX-', no_scrollbar=True, disabled=True)],
    [sg.Button('Start'), sg.Button('Stop'), sg.Button('Back')]
]

# Create the window
window = sg.Window('P.E.E.N POD', layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Close':
        break

window.close()
