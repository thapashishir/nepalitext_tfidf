import collections
# from nepalitext.utils import *
from nepalitext.preprocessor import tokenize,clean_text
from nepalitext.analyzer import calc_word_frequency,calc_tf,calc_idf,calc_tfidf,vocabulary

# tokenizing
tk1 = tokenize("corpus/doc1.txt")
tk2 = tokenize("corpus/doc2.txt")
tk3 = tokenize("corpus/doc3.txt")

# find bag of words
bow_doc1 = clean_text(tk1)
bow_doc2 = clean_text(tk2)
bow_doc3 = clean_text(tk3)

# generating vocabulary by union operation between
vocabulary = vocabulary([set(bow_doc1),set(bow_doc2),set(bow_doc3)])

# calculating term frequency
wf_doc1 = calc_word_frequency(vocabulary, bow_doc1)
wf_doc2 = calc_word_frequency(vocabulary, bow_doc2)
wf_doc3 = calc_word_frequency(vocabulary, bow_doc3)

tf1 = calc_tf(wf_doc1, len(bow_doc1))
tf2 = calc_tf(wf_doc2, len(bow_doc2))
tf3 = calc_tf(wf_doc3, len(bow_doc3))

idf = calc_idf([wf_doc1, wf_doc2, wf_doc3])

print("TF-IDF in doc1:\n", (collections.Counter(calc_tfidf(tf1, idf))).most_common(5), "\n")
print("TF-IDF in doc2:\n", (collections.Counter(calc_tfidf(tf2, idf))).most_common(5), "\n")
print("TF-IDF in doc3:\n", (collections.Counter(calc_tfidf(tf3, idf))).most_common(5), "\n")
