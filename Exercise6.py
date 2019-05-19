#Exercise6
	#Prompt for a string and respond with whether it is a palindrome
	#AKA same backwards as it is forwards
	
word = list(input("Enter a string: "))
if word[::] == word[::-1]:
	print("{} is a palindrome.".format(''.join(word)))
else:
	print("{} is not a palindrome.".format(''.join(word)))
