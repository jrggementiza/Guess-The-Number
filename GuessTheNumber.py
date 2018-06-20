""" Guess the number! """

import random, generic


def check_answer(player_guess, guess_value):
	"""
	Compares a player's guess and the number to guess
	Returns True if the player guessed correctly
	Returns False by default
	"""

	end_game = False

	if player_guess > guess_value:
		print('guess too high!')
	elif player_guess < guess_value:
		print('guess too low!')
	else:
		print('correct!')
		end_game = True
	return end_game


def check_input(min_guess_range, max_guess_range):
	""" Asks user to enter guess and returns a guess within defined min and max guess range """
	while True:
		try:
			playerGuess = int(input('enter your guess: '))
			assert min_guess_range <= playerGuess <= max_guess_range

		except AssertionError:
			print('guess should be between {0} - {1}!'.format(min_guess_range, max_guess_range))
		except ValueError:
			print('numbers only!')
		else:
			return playerGuess


def guess_number(min_guess_range, max_guess_range):
	""" Returns a guess that is within defined min and max guess range """
	print(f'guess the number between {min_guess_range} and {max_guess_range}!')
	return check_input(min_guess_range, max_guess_range)


def generate_guess_value(min_guess_range=1, max_guess_range=10):
	"""
	Returns a random number to guess between a defined min and max range.
	Min and Max range can be custom. Default values are 1 - 10
	"""
	return random.randrange(min_guess_range, max_guess_range), min_guess_range, max_guess_range


def main():
	run_game = True
	while run_game == True:
		guess_value, min_guess_range, max_guess_range = generate_guess_value(1,4)
		guess_count, guess_limit = 1, 3

		end_game = False
		while end_game == False:
			print(f'You have {guess_limit - guess_count + 1} remaining. ')
			player_guess = guess_number(min_guess_range, max_guess_range)
			player_won = check_answer(player_guess, guess_value)
			guess_count = guess_count + 1
			
			if player_won == True:
				print(f'You win! congrats! ')
				end_game = True
			elif guess_count > guess_limit:
				print(f'You ran out of guesses! you lose!')
				end_game = True

		run_game = generic.run_again()

if __name__ == '__main__':
	main()

# [*] number to guess is generated within min - max range
# [*] guess limit is set
# [*] guess is made -> check guess within range
# [*] guess made compared to number to guess
# [*] loop again until guess limit runs out or until guess made matchess number to guess







