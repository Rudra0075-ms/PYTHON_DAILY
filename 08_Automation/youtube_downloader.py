import yt_dlp

url = input("Paste YouTube URL: ")

try:
    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Download completed!")
except Exception as e:
    print("Error:", e)