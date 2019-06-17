# Exercise9
    #Generate a number between 1-9, and have the user guess which number it is. Inform of high or low guesses.

import random
def play_game():
    number = random.randint(1, 9)
    print("Guess a number between 1-9 (enter quit anytime to stop)\n")
    i = 0
    while True:
        guess = input("Guess: ")
        if guess.lower() == "quit":
            flag = False
            break
        guess = int(guess)
        if guess == number:
            i+=1
            print("Correct! The correct number was " + str(number))
            print("You got the correct number in {} guesses".format(str(i)))
            break
        elif guess < number:
            print("too low, try again.\n")
            i+=1
        else:
            print("too high, try again.\n")
            i+=1

play_again = "yes"
while play_again.lower() == "yes":
    play_game()
    play_again = input("play again? (yes/no): ")