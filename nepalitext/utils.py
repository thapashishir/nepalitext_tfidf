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


def word_frequecy(word_list):
	return Counter(word_list)

def calc_word_frequency(vocabulary,bow_doc):
	wf_doc=dict.fromkeys(vocabulary,0)
	for word in bow_doc:
		wf_doc[word]+=1
	return wf_doc 


def calc_tf(word_dict,total_words):
	tf_dict = {}
	for word,count in word_dict.items():
	 	tf_dict[word] = count/total_words
	return tf_dict

def calc_idf(doc_list):
	idf_dict = {}
	N = len(doc_list)
	idf_dict = dict.fromkeys(doc_list[0].keys(),0)
	for doc in doc_list:
		for word, val in doc.items():
			if val > 0:
				idf_dict[word] += 1

	for word, val in idf_dict.items():
		idf_dict[word] =math.log10(N/float(val))
	return idf_dict

def calc_tfidf(tf_dict,idf_dict):
	tfidf_dict = {}
	for word, val in tf_dict.items():
		tfidf_dict[word] = val * idf_dict[word]
	return tfidf_dict














	
