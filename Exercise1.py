#Exercise 1: Character Input
	#print out the year you will turn 100
	#ask for a number, then repeat a message that many times

import datetime
today = datetime.datetime.now()

name = input("Hello, what is your name?")
age = int(input("{}, how old are you?".format(name.title())))
message = ("Okay {}, you turn 100 years old in {}!".format(name.title(),today.year + 100 - age))

print(message)
response = int(input("Now, give me a number, and I'll repeat myself that many times!"))
print((message + "\n") * response)
