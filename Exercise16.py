#Exercise16
    #Generate a password using Python
from random import randint
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]#26
numbers = ['0','1','2','3','4','5','6','7','8','9',]#10
symbols = ['!','@','#','$','%','^','&','*','?',]#9

def random_character():
    random1 = randint(1,6)  #1,2,and 3 chooses random letter, 4 and 5 chooses random number, and 6 chooses random symbol
    if random1 <=3:
        random2 = randint(0,25)
        random3 = randint(1,2)  #1 is lowercase, 2 is uppercase
        char = letters[random2]
        if random3 == 2:
            char = char.upper()
        return char
    elif random1 <= 5:
        random2 = randint(0,9)
        return numbers[random2]
    else:
        random2 = randint(0,8)
        return symbols[random2]

num = int(input('How many characters for password?:'))
for _ in range(1,num+1):
    print(random_character(),end='')