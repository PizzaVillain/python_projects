# Tic Tac Toe

import random

def drawBoard(board):
	#이 함수는 파라미터로 받은 보드를 출력한다.

	#"board"는 10개의 문자열로 된 리스트이며 보드를 나타낸다.(인덱스 0은 무시한다.)
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')
	
def inputPlayerLetter():
	#플레이어가 어떤 글자 마크로 할 것인지 선택하게 한다.
	#플레이어가 선택한 글자를 첫 번째 아이템으로, 컴퓨터의 문자를 두 번째 아이템으로 하는 문자열을 반환한다.
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Do you want to be X or O?')
		letter = input().upper()

	#튜플의 첫 번째 요소가 플레이어의 글자이고 두 번째 요소는 컴퓨터의 글자이다.
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	#누가 먼저 할 것인지 임의로 정한다.
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'

def playAgain():
	#플레이어가 또 게임을 하겠다고 하면 True를 반환하고, 아니면 False를 반환한다.
	print('Do you want to play again? (Yes or No)')
	return input().lower().startswith('y')

def makeMove(board, letter, move):
	board[move] = letter

def isWinner(bo, le):
	#보드와 플레이어의 글자를 주면, 플레이어가 이겼을 때 True를 반환한다.
	#board 대신 bo, letter 대신 le를 써서 타이핑하는 수고를 줄인다.
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or #윗부분을 가로지르는지
	(bo[4] == le and bo[5] == le and bo[6] == le) or #중간을 가로지르는지
	(bo[1] == le and bo[2] == le and bo[3] == le) or #아랫부분을 가로지르는지
	(bo[7] == le and bo[4] == le and bo[1] == le) or #왼쪽 가장자리에서 세로로 내려오는지
	(bo[8] == le and bo[5] == le and bo[2] == le) or #가운데에서 세로로 내려오는지
	(bo[9] == le and bo[6] == le and bo[3] == le) or #오른쪽 가장자리에서 세로로 내려오는지
	(bo[7] == le and bo[5] == le and bo[3] == le) or #대각선 1
	(bo[9] == le and bo[5] == le and bo[1] == le)) #대각선 2

def getBoardCopy(board):
	#보드 리스트를 복제한 다음 복제한 리스트를 반환한다.
	dupeBoard = []

	for i in board:
		dupeBoard.append(i)

	return dupeBoard

def isSpaceFree(board, move):
	#보드에서 move 위치가 비어 있으면 True를 반환한다.
	return board[move] == ' '

def getPlayerMove(board):
	#플레이어가 움직일 위치를 입력하도록 한다.
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('What is your next move? (1-9)')
		move = input()
	return int(move)

def chooseRandomMoveFromList(board, movesList):
	#moveList와 board를 보고 가능한 위치를 반환한다.
	#가능한 위치가 하나도 없으면 None을 반환한다.
	possibleMoves = []
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)

	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None

def getComputerMove(board, computerLetter):
	#board, computerLetter를 보고, 컴퓨터의 차례에서 어디에 놓을지 결정한 다음 위치를 반환한다.
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	#틱택토 인공지능의 알고리즘
	#우선 다음에 이길 수 있는지 검사한다.
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i

	#상대편이 다음 번에 이길 수 있는지 검사해서 만약 그렇다면 막는다.
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i

	#만약 비어 있으면 코너를 차지한다.
	move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
	if move != None:
		return move

	#만약 비어 있으면 중앙을 차지한다.
	if isSpaceFree(board, 5):
		return 5

	#한쪽 면으로 이동한다.
	return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
	#보드의 모든 공간이 다 찼으면 True를 반환한다. 그렇지 않으면 False를 반환한다.
	for i in range(1, 10):
		if isSpaceFree(board, i):
			return False
	return True

print('Welcome to Tic Tac Toe!')

while True:
	#보드를 재설정한다.
	theBoard = [' '] * 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('The ' + turn + ' will go first.')
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'player':
			#플레이어의 차례
			drawBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)

			if isWinner(theBoard, playerLetter):
				drawBoard(theBoard)
				print('Hooray! You have won the game!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('The game is a tie!')
					break
				else:
					turn = 'computer'

		else:
			#컴퓨터의 차례
			move = getComputerMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)

			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print('The computer has beaten you! You lose.')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('The game is a tie!')
					break
				else:
					turn = 'player'

	if not playAgain():
		break