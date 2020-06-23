from yt import *
import PySimpleGUI as sg



sg.theme('DarkBlue9')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('YouTube Video Downloader')],
            [sg.Text('Enter URL of the video'), sg.InputText()],
            [sg.Checkbox('Download Playlist', default=False)],
            [sg.Checkbox('MP4', default=False)],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('YouTube Video Downloader', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break

    if check_if_url_supported(values[0]) == False:
        sg.popup('Invalid URL entered')
    else:
        if values[2] == True: #MP4 selected
            if values[1] == True:
                dl_MP4(values[0], False)
                sg.popup('Download Successful')
            elif values[1] == False:
                dl_MP4(values[0], True)
                sg.popup('Download Successful')
        elif values[2] == False: #MP3 Selected
            if values[1] == True:
                dl_MP3(values[0], False)
                sg.popup('Download Successful')
            elif values[1] == False:
                dl_MP3(values[0], True)
                sg.popup('Download Successful')

window.close()
