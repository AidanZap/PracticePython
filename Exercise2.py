#Exercise 2
	#given two numbers, check if the first is divisible by two, four, and another given number

print("Give me two numbers and I will tell you if the first is even, divisible by 4, and divisible by the second number.")
number = int(input("Number:"))
divisor = int(input("Divisor:"))

if number%2 == 0:
	print("{} is even.\n".format(number))
else:
	print("{} is odd.\n".format(number))

if number%4 == 0:
	print("{} is divisible by 4.\n".format(number))
else:
	print("{} is not divisible by 4.\n".format(number))

if number%divisor == 0:
	print("{} is divisible by {}.".format(number,divisor))
else:
	print("{} is not divisible by {}.".format(number,divisor))
