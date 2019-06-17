#Exercise 3
	#Get all values in a given list below 5. Get these values in a single line of code
	#Store these values in another list and print that list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

x =([num for num in a if num<5])

print(x)
