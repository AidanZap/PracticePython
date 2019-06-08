#Exercise12
    #Given a list of numbers, return a list with the first and last number

a = [5,10,15,20,25]
b = [num for num in a if num == a[0] or num == a[-1]]
print(b)