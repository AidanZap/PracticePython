#Exercise18
    #Create the cows and bulls game
import random

def playgame(num, difficulty):
    num = [int(x) for x in str(num)]
    guesses = 0
    while guesses < difficulty:
        guess = input('\nEnter a four digit guess: ')
        cows = 0
        bulls = 0
        guess = [int(x) for x in guess]
        for index in range(0,4):
            if num[index] == guess[index]:
                cows = cows +1
            else:
                bulls = bulls +1
        print(f'{cows} cow(s), {bulls} bull(s)')
        if cows == 4:
            print(f"Well done, the number was {num}")
            break
        guesses = guesses +1
while True:
    rand = random.randint(1000,9999)
    response = int(input('Welcome to cows and bulls! Please select a difficulty below:'
          '\n1.)Easy (10 Guesses)\n2.)Medium (7 Guesses)\n3.)Hard (5 Guesses)\n'))

    if response ==1:
        playgame(rand,10)
    elif response ==2:
        playgame(rand,7)
    elif response ==3:
        playgame(rand,5)
    else:
        print('Invalid response...')

    play_again = input('\nWould you like to play again?(y/n)')
    if play_again == 'y':
        pass
    else:
        break