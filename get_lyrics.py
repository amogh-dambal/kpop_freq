from bs4 import BeautifulSoup
from glob import iglob
import string, os


from html_manager import fetch

def get_songs(filename):
	artists = []
	titles = []

	with open(filename) as f:
		lines = f.readlines()

		for line in lines:
			titles.append(line.split('-')[0].strip())
			artists.append(line.split('-')[1].strip())

	return artists, titles


def generate_query_string(artist, title):
	artist_q = artist.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '-')
	title_q = title.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '-')

	return artist_q + "-" + title_q + "-lyrics"


def extract_lyrics(artists, titles):
	for artist, title in zip(artists, titles):
		url = "https://genius.com" + generate_query_string(artist, title)

		raw_html = fetch(url)
		if raw_html is not None:
			html = BeautifulSoup(raw_html, 'html.parser')

			lyricdivs = html.findAll('div', {'class': 'lyrics'})
			for div in lyricdivs:
				lyrics = div.find('p')

				with open('./data/lyric_files/{0}.txt'.format(generate_query_string(artist, title))) as f:
					f.write(lyrics.text)
		else:
			print("Lyrics not found for {0} - {1}".format(artist, title))


def manual_lyric_extraction():
	urls = [
		"https://genius.com/Bts-blood-sweat-and-tears-lyrics",
		"https://genius.com/Bts-boy-with-luv-lyrics",
		"https://genius.com/Blackpink-ddu-du-ddu-du-lyrics",
		"https://genius.com/G-i-dle-latata-lyrics",
	]

	for url in urls:
		raw_html = fetch(url)
		if raw_html is None:
			print("unable to fetch lyrics for {0}".format(url))

		html = BeautifulSoup(raw_html, 'html.parser')
		lyricdivs = html.findAll('div', {'class': 'lyrics'})
		for div in lyricdivs:
			lyrics = div.find('p')

			with open("./data/lyric_files/{0}".format(url[19:]), 'w') as f:
				f.write(lyrics.text)


def generate_corpus():
	files = [f for f in iglob('**/*', recursive=True) if os.path.isfile(f)]
	lyric_files = [f for f in files if f.endswith('lyrics.txt')]

	with open('data/korpus.txt', 'wb') as outfile:
		for file in lyric_files:
			with open(file, 'rb') as infile:
				outfile.write(infile.read())
