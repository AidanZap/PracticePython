import random


def play_game():
    guesses = 0
    correct_num = random.randint(0, 101)
    while True:
        try:
            guess = int(input("Guess number: "))
            if guess == correct_num:
                print(f"You got it in {guesses} guesses, the number was {correct_num}!")
                break
            elif guess > correct_num:
                print("Too High!")
            else:
                print("Too Low!")
        except ValueError:
            print("Invalid number entered, adding 1 guess")
        guesses += 1


while True:
    print("Welcome to High Low\n---------------------\n")
    play_game()
    response = input("Play again? (y/n)")
    if response.lower() == 'y':
        pass
    elif response.lower() == 'n':
        break
    else:
        print("Did not understand response, exiting game.")
        break