#Exercise5
	#Given two lists, print out the numbers that are shared between both lists
	#Randomly generate two new lists
	
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

common_elements = [num for num in a if num in b]
for num in common_elements:
	if num not in c:
		c.append(num)
print(c)

