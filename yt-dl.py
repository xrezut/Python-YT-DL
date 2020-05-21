from __future__ import unicode_literals
import youtube_dl
import PySimpleGUI as sg

# Downloads a YT Video in MP4 Format
def dl_MP4(url, playlist):
    ydl_opts = {
        'noplaylist': playlist,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Downloads a YT Video in MP3 Format
def dl_MP3(url, playlist):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': playlist,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def check_if_url_supported(url):
    extractors = youtube_dl.extractor.gen_extractors()
    for e in extractors:
        if e.suitable(url) and e.IE_NAME != 'generic':
            return True
    return False

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