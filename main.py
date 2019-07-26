from get_lyrics import get_songs, extract_lyrics, manual_lyric_extraction, generate_corpus
from nlp import tokenize_corpus, print_doc_info, print_token_frequency

import nltk

filename = "./data/top100_july2019.txt"

# extract lyrics from HTML
# and build a corpus
artists, titles = get_songs(filename)
extract_lyrics(artists, titles)
manual_lyric_extraction()
corpus_file = generate_corpus()

# build tokenized version of
# documents for NLP processing
tokens_ko = tokenize_corpus(corpus_file)
doc_ko = nltk.Text(tokens_ko)
print_doc_info(doc_ko)
print_token_frequency(doc_ko, n_tokens=40, save_plot=True, plot_filename='img/plot40.png')






