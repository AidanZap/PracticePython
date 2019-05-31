#Exercise 4
	#Given a number, print out all divisors or numbers that divide evenly

num = int(input("Chose a starting number: "))

flag = True
for x in range(2,num):
	if num%x == 0:
		print(x)
		flag = False

if flag:
	print(str(num) + " is a prime number, no divisors")