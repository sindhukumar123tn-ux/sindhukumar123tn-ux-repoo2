from pytubefix import YouTube

url = input("Enter YouTube Video URL: ")

try:
    yt = YouTube(url)
    print("Title:", yt.title)

    video = yt.streams.get_highest_resolution()
    print("Downloading...")
    video.download()

    print("Download Completed!")

except Exception as e:
    print("Error:", e)
