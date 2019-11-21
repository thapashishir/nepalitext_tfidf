import re
import math
from collections import Counter

def get_stop_words():
	file = open("nepali_stopwords.txt",encoding="utf8")
	line = file.read()
	return line.split()

def get_suffixes():
	suffix_file = open("nepali_suffix.txt",encoding="utf8")
	line = suffix_file.read()
	return line.split()

def tokenize(filepath):
	file = open(filepath,encoding="utf8")
	line = file.read()
	#remove |(),०-९<<?! punctuation marks
	line_without_symbols=re.sub('[।(),०-९<<?!]', '', line)
	return line_without_symbols.split()

def remove_suffix(token):
	suffix_list = get_suffixes()
	for suffix in suffix_list:
		if token.endswith(suffix):
			return token[:-len(suffix)]
	return token

def clean_text(token_list):
	word_list = []
	stop_word_list = get_stop_words()
	for token in token_list:
		if token not in stop_word_list:
			token_without_suffix = remove_suffix(token)
			word_list.append(token_without_suffix)
	return word_list
