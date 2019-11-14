word = 'EVAPORATE'
correct_letters = []
for _ in range(0,len(word)):
    correct_letters.append('_')


def guess_letter(correct_letters, word):
    for letter in correct_letters:
        print(letter + " ", end="")
    letter = input('\n\nGuess a letter:').upper()
    if letter in correct_letters:
        print("You already guessed that!\n")
    else:
        index = 0
        notFound = True
        for word_letter in list(word):
            if letter == word_letter:
                correct_letters[index] = letter
                notFound = False
            index += 1
        if notFound:
            print(f"There are no {letter}s in this word\n")
        else:
            print(f"Found some {letter}s!\n")
    return correct_letters

while True:
    correct_letters = guess_letter(correct_letters, word)
    if '_' not in correct_letters:
        print(f"You got it, the word was {word.title()}!")
        break



