#reads txt file, tokenizes by sentence, finds all sentences with specified keyword, writes this to txt file

import nltk

#input file name here without extension
name = 'mongolia-bur1_using acrobat'

#input keyword without capitals
keyword = "capacity building"

txt_name = name + '.txt'
keyout_name = name + '_KeySentences' + '.txt'

#read the txt with the file name
txt = open(txt_name).read()
text_join = "".join(txt.splitlines())
sentences = nltk.sent_tokenize(text_join.lower())

key_list = ""
instances = 0

for n in range(len(sentences)):
    if keyword in sentences[n]:
        key_list = key_list + sentences[n] + "\n"
        instances = instances + 1

#write to txt file (overwrites)
Txt_join = open(keyout_name, 'w', encoding='utf-8')
Txt_join.write(key_list)

print("Keyword  = {0} \n{1} instances found".format(keyword, instances))