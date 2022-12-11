import pytube
from pytube import YouTube
from sys import argv

link = input("Enter Link Here:")
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
# need to figure out how find filesize in a video
#print("Size: ", yt.streams.get_highest_resolution.filesize)

yd = yt.streams.get_highest_resolution()

yd.download('/Users/elijahzimmerman/documents/youtube downloads')

print("DONE")