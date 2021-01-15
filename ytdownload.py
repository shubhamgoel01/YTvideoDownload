from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=fMdfDnGX9S8")
print(yt.streams.all())

dw = yt.streams.get_by_itag(18)
dw.download("E:/")

