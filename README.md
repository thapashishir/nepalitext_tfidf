# nepalitext_tfidf
This is the python program which is used to process nepali text and calculate tfidf
# Program Execution
-> python main.py
# TFIDF
TF(w) = (Number of times term w appears in a document) / (Total number of terms in the document)
IDF(w) = log_e(Total number of documents / Number of documents with term w in it)

Consider a document containing 100 words wherein the word 'Cauvery' appears 3 times.
1. The term frequency (tf) for 'Cauvery' is then TF = (3 / 100) = 0.03.
2. Now, assume we have 10 million documents and the word 'Cauvery' appears in 1000 of these. Then, the inverse document frequency (idf) is calculated as IDF = log(10,000,000 / 1,000) = 4.
3. Thus, the Tf-idf weight is the product of these quantities TF-IDF = 0.03 * 4 = 0.12.

