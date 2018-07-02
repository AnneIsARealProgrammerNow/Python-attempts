#reads txt file, removes stopwords, creates frequency distribution graph

import nltk

#these stopwords will be filtered.
#'...' and 'les' were not part of the stopwords/punctuation lists => added
from nltk.corpus import stopwords
import string
all_stops = set(stopwords.words('english')) | set(string.punctuation) | set(['...', 'les'])
 
#input file name here
name = 'mongolia-bur1'

txt_name = name + '.txt'

txt = open(txt_name, encoding='utf-8').read()
tokens = nltk.word_tokenize(txt.lower()) #tokenizes per word, making all lower case

clean_tokens = tokens[:]

for token in tokens:
    if token in all_stops:
        clean_tokens.remove(token)
 
freq = nltk.FreqDist(clean_tokens)

print(freq.most_common(5))

freq.plot(20,cumulative=False)