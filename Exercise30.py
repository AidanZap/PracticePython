import random

with open('sowpods.txt', 'r') as file:
    words = file.readlines()

rand = random.randint(0,len(words))
word = words[rand]

print(word)
