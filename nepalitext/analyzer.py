import math
def vocabulary(bow_list):
	vocab=set.union(*bow_list)
	return vocab

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
