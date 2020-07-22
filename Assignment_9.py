# Task:

# Count the number of each letter in a sentence.

sentence = input("Please enter a sentence: ")
sentenceset = set(sentence)
sentencedict = {}

for i in sentenceset:
    sentencedict[i] = sentence.count(i)

print(sentencedict)
