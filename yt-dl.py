from __future__ import unicode_literals
import youtube_dl

# Downloads a YT Video in MP4 Format
def dl_MP4_single(url, playlist):
    ydl_opts = {
        'noplaylist': playlist,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


print("Input YouTube URL to download: ")
url = input()

print("Download entire playlist? ")
playlistChoice = input().lower()
yes = {'yes','y', 'ye', ''}
no = {'no','n'}
if playlistChoice in yes:
    dl_MP4_single(url, False)
elif playlistChoice in no:
    dl_MP4_single(url, True)