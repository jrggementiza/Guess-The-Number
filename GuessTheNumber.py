""" User is promoted to guess a number between a minimum range and a maximum range 

To Add:
Limited number of guesses
"""
import random

def play_again():
	""" Basic Error Handling """
	while True:
		try:
			answer = input('would you like to play a again? [y/n] : ')
			answer = answer.lower()
			if answer == 'yes': answer = 'y'
			if answer == 'no': answer = 'n'

			assert answer == 'y' or answer =='n'

		except AssertionError:
			print('[y/n] only please!')

		else:
			return False if answer == 'n' else True


def check_answer(playerGuess, numberToGuess):
	""" Working Answer """
	returnValue = True
	prompt = ''

	if playerGuess > numberToGuess:
		prompt = 'guess too high!'
	elif playerGuess < numberToGuess:
		prompt = 'guess too low!'
	else:
		prompt = 'correct!'
		returnValue = False
	return prompt, returnValue

	""" Trying to one line it; SyntaxError
	returnValue = True
	prompt = ''
	prompt = 'guess too high!' if playerGuess > numberToGuess
	prompt = 'guess too low!' if playerGuess < numberToGuess
	prompt = 'guess correct!' and returnValue = False if playerGuess == numberToGuess
	return propmt, returnValue
	"""

	""" Trying to use dictionary; KeyError
	results = {
	playerGuess > numberToGuess : ['guess too high!', True],
	playerGuess < numberToGuess : ['guess too low!', True],
	playerGuess == numberToGuess : ['guess correct!', False]
	}

	return results[playerGuess, numberToGuess]
	"""


def check_input(minGuess, maxGuess):
	#add error handling: not int, outside range
	while True:
		try:
			playerGuess = int(input('enter your guess: '))
			assert minGuess <= playerGuess <= maxGuess

		except AssertionError:
			print('guess should be between {0} - {1}!'.format(minGuess, maxGuess))
		except ValueError:
			print('numbers only!')
		else:
			return playerGuess


def guess_number():
	minGuess, maxGuess = 1, 10
	numberToGuess = random.randrange(minGuess,maxGuess)
	print('guess the number between {0} and {1}!'.format(minGuess, maxGuess))

	noWinner = True
	while noWinner == True:
		playerGuess = check_input(minGuess, maxGuess)
		prompt, noWinner = check_answer(playerGuess, numberToGuess)
		print(prompt)


def play():
	runGame = True
	while runGame == True:
		guess_number()
		runGame = play_again()
	print('GOOD BYE!')


def main():
	play()


if __name__ == '__main__':
	main()