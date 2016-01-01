import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def get_random_word(word_list):
	#이 함수는 문자열 리스트에서 임의의 문자열을 선택해서 반환한다.
	word_index = random.randint(0, len(word_list) - 1)
	return word_list[word_index]

def display_board(HANGMANPICS, missed_letters, correct_letters, secret_word):
	print (HANGMANPICS[len(missed_letters)])
	print()

	print('Missed letters:', end = ' ')
	for letter in missed_letters:
		print (letter, end = ' ')
	print()

	blanks = '_' * len(secret_word)

	for i in range(len(secret_word)): #맞게 추측한 단어로 빈칸을 채우기
		if secret_word[i] in correct_letters:
			blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

	for letter in blanks: # 문자와 빈칸으로 비밀 단어 보여주기
		print(letter, end=' ')
	print()

def get_guess(already_guessed):
	# 플레이어가 입력한 글자를 입력한다. 여기에서는 플레이어가 글자 하나를 입력했는지 확인한다.
	while True:
		print ('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print ('Please enter a single letter.')
		elif guess in already_guessed:
			print ('You have already guessed that letter. Choose again.')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print ('Please enter a LETTER.')
		else:
			return guess

def play_again():
	#플레이어가 또 게임을 한다고 하면 True를 반환하고 아니면 False를 반환한다.
	print ('Do you want to play again? (Yes or no)')
	return input().lower().startswith('y')


print ('H A N G M A N')
missed_letters = ' '
correct_letters = ' '
secret_word = get_random_word(words)
game_is_done = False

while True:
	display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)

	#플레이어가 문자를 입력하도록 한다.
	guess = get_guess(missed_letters + correct_letters)

	if guess in secret_word:
		correct_letters = correct_letters + guess

		#플레이어가 이겼는지 검사한다.
		found_all_letters = True
		for i in range(len(secret_word)):
			if secret_word[i] not in correct_letters:
				found_all_letters = False
				break
		if found_all_letters:
			print ('Yes! The secret word is "' + secret_word + '"! You have won!')
			game_is_done = True
	else:
		missed_letters = missed_letters + guess

		#플레이어가 제한 횟수를 넘겨서 졌는지 확인한다.
		if len(missed_letters) == len(HANGMANPICS) - 1:
			display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
			print ('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' correct guesses, the word was "' + secret_word + '"')
			game_is_done = True

	#게임 마지막에 플레이를 또 할 것인지 물어본다.
	if game_is_done:
		if play_again():
			missed_letters = ' '
			correct_letters = ' '
			game_is_done = False
			secret_word = get_random_word(words)
		else:
			break