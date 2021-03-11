from pytube import YouTube
from pytube import Playlist
import os

'''Python 3 Script'''
file = 'DownloadList.txt'

def youtubedownload():
	f = open(file, 'r')
	url = f.readline()
	while url:
		if url == '':
			return False
		else:
			print(url)
			url = f.readline()
			ytd = YouTube(url).streams.first().download()
			print(ytd)

youtubedownload()

while True:
	youtubedownload()
else:
	os.remove(file)
	quit()
