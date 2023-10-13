import PySimpleGUI as sg
import spiriteBox as sb
import sharedFunctions as sf
import time, os, subprocess

wordLists = os.listdir('wordsdatabase/')

# Define the layouts for the pages
home_layout = [
    [sg.Text('Welcome to the spirite zone.\nThis is the P.E.E.N Pod (Paranormal, Eccentric, Evaluation, Nanoreceptor).\nThis works by layering randomness within the code, since the ghosts can effect small\n electrical fields, they can manipulate the randomness once it is layered properly, like within this\n software. Below are some setting to help get the best results\n\nWordlist options')],
    [sg.Combo(wordLists, default_value=wordLists[0], key='-COMBO-'), sg.Button('Select', key='SELECT')],
    [sg.Button('Close', key='END')]
]

standard_layout = [
    [sg.Text('Standard Mode')],
    [sg.Multiline(size=(40, 1), key='-sTEXTBOX-', no_scrollbar=True, disabled=True)],
    [sg.Button('Play', key='sStart')]
]

reverse_layout = [
    [sg.Text('Reverse Mode')],
    [sg.Multiline(size=(40, 1), key='-rTEXTBOX-', no_scrollbar=True, disabled=True)],
    [sg.Button('Play', key='rStart')]
]

binary_layout = [
    [sg.Text('Binary Mode')],
    [sg.Multiline(size=(40, 1), key='-byTEXTBOX-', no_scrollbar=True, disabled=True, default_text='Yes', background_color='white'), sg.Multiline(size=(40, 1), key='-bnTEXTBOX-', no_scrollbar=True, disabled=True, default_text='No', background_color='white')],
    [sg.Button('Play', key='bStart')]
]

tarot_layout = [
    [sg.Text('Tarot Mode')],
    [sg.Button('Play', key='tStart')]
]

# Create a Tab element to hold the pages
tab_layout = [
    [sg.Tab('Home', home_layout, key='-HOME-')],
    [sg.Tab('Standard Mode', standard_layout, key='-STANDARD-')],
    [sg.Tab('Reverse Mode', reverse_layout, key='-REVERSE-')],
    [sg.Tab('Binary Mode', binary_layout, key='-BINARY-')],
    [sg.Tab('Tarot Mode', tarot_layout, key='-TAROT-')],
]

# Create the main layout containing the Tab element
layout = [
    [sg.TabGroup(tab_layout)]
]

def run_pygame_script():
    subprocess.run(["python", "tarot.py"])

# Create the window
window = sg.Window('P.E.E.N POD', layout, finalize=True)

sFlag = False
lines = sf.read(wordLists[0])

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'END':
        break
    elif event == '-STANDARD-':
        print('Switched to Standard Mode')
    elif event == '-REVERSE-':
        print('Switched to Reverse Mode')
    elif event == '-BINARY-':
        print('Switched to Binary Mode')
    elif event == 'sStart':
        line = sb.standardMode(lines)
        window['-sTEXTBOX-'].update(value=line)
        window.finalize()
        sf.speak(line)
    elif event == 'rStart':
        line = sb.reverseMode(lines)
        window['-rTEXTBOX-'].update(value=line)
        window.finalize()
        sf.speak(line)
    elif event == 'bStart':
        line = sb.binary()
        if line == 'Yes':
            window['-byTEXTBOX-'].update(background_color='green')
        else:
            window['-bnTEXTBOX-'].update(background_color='Red')
        window.finalize()
        sf.speak(line)
        time.sleep(1)
        window['-byTEXTBOX-'].update(background_color='white')
        window['-bnTEXTBOX-'].update(background_color='white')
        window.finalize()
    elif event == 'SELECT':
        lines = sf.read(values['-COMBO-'])
        sg.popup(f"Wordlist has been changed to: {values['-COMBO-']}")
    elif event == 'tStart':
        run_pygame_script()
        

window.close()