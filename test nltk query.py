from bs4 import BeautifulSoup
 
import urllib.request
 
import nltk
 
from nltk.corpus import stopwords
 
response = urllib.request.urlopen('http://php.net/')
 
html = response.read()
 
soup = BeautifulSoup(html,"html5lib")
 
text = soup.get_text(strip=True)
 
tokens = [t for t in text.split()]
 
clean_tokens = tokens[:]
 
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
 
freq = nltk.FreqDist(clean_tokens)
 
freq.plot(26,cumulative=False)

#________________________________________
from nltk.corpus import wordnet

synonyms = []
 
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
 
print(synonyms)
 