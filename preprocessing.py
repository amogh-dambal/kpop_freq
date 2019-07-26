import enchant, string, re
from konlpy.utils import read_txt


def remove_extraneous(lines):
	lines = [
		line for line in lines
		if
		not '[' in line and
		not ']' in line and
		line is not ''
	]
	return lines


def is_all_english(line):
	d = enchant.Dict("en_US")
	punct = '!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'
	for word in line.translate(str.maketrans('', '', punct)).split():
		if not d.check(word):
			return False
	return True


# -*- coding: utf-8 -*-
def is_english(word):
	d = enchant.Dict("en_US")
	if d.check(word):
		return True

	try:
		word.encode('ascii')
	except UnicodeEncodeError:
		return False
	else:
		return True


def filter_english_words(line):
	return [word for word in line.translate(str.maketrans('', '', string.punctuation)).split() if not is_english(word)]


def remove_english(lines):
	new_lines = [line for line in lines if not is_all_english(line)]
	new_lines = [filter_english_words(line) for line in new_lines]
	return new_lines


def remove_punctuation(tokens):
	new_tokens = []
	for token in tokens:
		new_token = re.sub(r'[^\w\s]', '', token)
		if new_token is not '':
			new_tokens.append(new_token)
	return new_tokens


def remove_stopwords(tokens):
	with open('data/stopwords-ko.txt', 'rb') as f:
		file_lines = read_txt('data/stopwords-ko.txt')

	stopwords = [line.strip() for line in file_lines]
	new_tokens = []
	for token in tokens:
		if token not in stopwords:
			new_tokens.append(token)
	return new_tokens
