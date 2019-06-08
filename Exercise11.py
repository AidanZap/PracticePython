#Exercise11
    #Given an integer, tell whether it is prime or not

number = int(input('Enter a number:'))

for num in range(2,int(number/2)+1):
    if number%num == 0:
        print(f'{number} is not a prime number.')
        break
    elif num == int(number/2):
        print(f'{number} is a prime number.')