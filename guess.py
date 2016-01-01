# 숫자 알아맞히기 게임
import random

guesses_taken = 0
print('Hello! What is your name?')
my_name = input()

number = random.randint(1, 100)
print('well, ' + my_name + ', I am thinking of a number between 1 and 100')

while guesses_taken < 6:
    print('take a guess.')
    guess = input()
    guess = int(guess)

    guesses_taken = guesses_taken + 1

    if guess < number:
    	print ('Your guess is too low.')

    elif guess > number :
    	print ('Your guess is too high')

    else:
    	break

if guess == number:
	guesses_taken = str(guesses_taken)
	print ('Good job, ' + my_name + '! You guessed my number in ' + guesses_taken + ' guesses!')

if guess != number:
	number = str(number)
	print ('Nope, The number I was thinking of was ' + number)

