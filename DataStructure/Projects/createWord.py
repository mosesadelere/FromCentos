from nltk.corpus import words
import json

wordList = words.words()
with open('result.json', 'w') as data:
    for i in range(len(wordList)):
        json.dump(wordList[i], data)