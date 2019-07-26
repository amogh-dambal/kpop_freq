from konlpy.utils import read_txt
from konlpy.tag import Okt

from matplotlib import font_manager, rc
from matplotlib import pylab
import matplotlib.pyplot as plt

from preprocessing import remove_english, remove_extraneous, remove_stopwords


def tokenize_corpus(corpus_file):
	raw_document_ko = read_txt(corpus_file)
	lines = raw_document_ko.split('\n')

	processed_doc_ko = remove_stopwords(remove_extraneous(remove_english(remove_extraneous(lines))))
	doc_ko = ' '.join(str(word) for line in processed_doc_ko for word in line)

	t = Okt()
	tokens_ko = t.morphs(doc_ko)

	return tokens_ko


def print_doc_info(doc):
	print("Document length (number of tokens): {0}".format(len(doc.tokens)))
	print("Number of unique tokens: {0}".format(len(set(doc.tokens))))
	print("Frequency distribution: ")
	doc.vocab()


def print_token_frequency(doc, n_tokens, save_plot, plot_filename):
	font_fname = '/Library/Fonts/AppleGothic.ttf'
	font_name = font_manager.FontProperties(fname=font_fname).get_name()
	font = {
		'family': font_name,
		'weight': 'bold',
		'size': 28
	}

	rc('lines', lw=1.4)
	rc('font', **font)

	if save_plot:
		pylab.show = lambda: pylab.savefig(plot_filename)
	plt.figure(figsize=(40, 30))

	doc.plot(n_tokens)






