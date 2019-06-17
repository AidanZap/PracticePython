# Exercise8
	# Create a rock paper scissors game

import random, os, time
def cpu_game():
	choice = input("Rock / Paper / Scissors?:")
	cpu_choice = random.randint(1, 3)
	if choice.lower() == "rock":
		if cpu_choice == 1:
			print("CPU chooses rock.\nTie game!")
		elif cpu_choice == 2:
			print("CPU chooses paper.\nYou lose!")
		else:
			print("CPU chooses scissors.\nYou win!")
	if choice.lower() == "paper":
		if cpu_choice == 1:
			print("CPU chooses rock.\nYou win!")
		elif cpu_choice == 2:
			print("CPU chooses paper.\nTie game!")
		else:
			print("CPU chooses scissors.\nYou lose!")
	if choice.lower() == "scissors":
		if cpu_choice == 1:
			print("CPU chooses rock.\nYou lose!")
		elif cpu_choice == 2:
			print("CPU chooses paper.\nYou win!")
		else:
			print("CPU chooses scisscors.\nTie game!")
			
def two_player_game():
	Achoice = input("Player 1, Rock / Paper / Scissors?:")
	os.system('cls')
	Bchoice = input("Player 2, Rock / Paper / Scissors?:")
	if Achoice.lower() == "rock":
		if Bchoice.lower() == "rock":
			print("Player 1 chose rock, player 2 chose rock.\nTie game!")
		elif Bchoice.lower() == "paper":
			print("Player 1 chose rock, player 2 chose paper.\nPlayer 2 wins!")
		else:
			print("Player 1 chose rock, player 2 chose scissors.\nPlayer 1 wins!")
	if Achoice.lower() == "paper":
		if Bchoice.lower() == "rock":
			print("Player 1 chose paper, player 2 chose rock.\nPlayer 1 wins!")
		elif Bchoice.lower() == "paper":
			print("Player 1 chose paper, player 2 chose paper.\nTie game!")
		else:
			print("Player 1 chose paper, player 2 chose scissors.\nPlayer 2 wins!")
	if Achoice.lower() == "scissors":
		if Bchoice.lower() == "rock":
			print("Player 1 chose scissors, player 2 chose rock.\nPlayer 2 wins!")
		elif Bchoice.lower() == "paper":
			print("Player 1 chose scissors, player 2 chose paper.\nPlayer 1 wins!")
		else:
			print("Player 1 chose scissors, player 2 chose scissors.\nTie game!")
	
print("Rock Paper Scissors\n--------------------------")
time.sleep(2)
while True:
	os.system('cls')
	game_selection = int(input("1.) vs. CPU\n2.) 2 Player\n3.) Exit\n"))
	if game_selection == 1:
		cpu_game()
		play_again = input("Play again? (yes/no) ")
		if play_again.lower() == "yes":
			pass
		else:
			break
	elif game_selection == 2:
		two_player_game()
		play_again = input("Play again? (yes/no) ")
		if play_again.lower() == "yes":
			pass
		else:
			break
	elif game_selection == 3:
		print("Thank you for playing!")
		break
	else:
		print("Invalid response, enter 1-3\n")
