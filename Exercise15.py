#Exercise15
    #Given a long string of several words, return the words in reverse order

sentence = input('Write out a sentence: ')
sentence = sentence.split()
sentence.reverse()
print(*sentence)