import youtube_dl


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

