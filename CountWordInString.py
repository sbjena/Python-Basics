from collections import Hashable
import nltk
file_content = open("temp.txt").read()
tokens = nltk.word_tokenize(file_content)

for i in tokens:
    print(i)