import nltk
import matplotlib.pyplot as plotter #does not work

#these stopwords will be filtered. Need to normalise capitalisation still.
#'...' and 'les' were not part of the stopwords/punctuation lists => added
from nltk.corpus import stopwords
import string
all_stops = set(stopwords.words('french')) | set(string.punctuation) | set(['...', 'les'])
 
#input file name here
name = 'andorra-bur2'

txt_name = name + '.txt'

txt = open(txt_name).read()
tokens = nltk.word_tokenize(txt)

clean_tokens = tokens[:]

for token in tokens:
    if token in all_stops:
        clean_tokens.remove(token)
 
freq = nltk.FreqDist(clean_tokens)

print(freq.most_common(5))

freq.plot(20,cumulative=False)
plotter.savefig('frequency andorra.png')  #does not work