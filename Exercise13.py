#Exercise13
    #Ask for a number, and print the fibonacci sequence up to that number

amount = int(input('enter how many fibonacci numbers you would like:'))

if amount <=1:
    a = [1]
if amount >=2:
    a = [1,1]
    while amount>2:
        a.append(a[-1]+a[-2])
        amount = amount-1
print(a)