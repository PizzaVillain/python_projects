#-*- coding: utf-8 -*-
import random
import time

def displayIntro():
	print('당신은 목숨을 건 내기를 하고 있습니다.')
	print('눈 앞의 사람이 동전을 던질 것입니다.')
	print('만일 당신이 맞는 면을 고른다면 엄청난 재산을 얻겠지만,')
	print('잘못된 면을 고른다면 즉시 목숨을 잃어버릴 것입니다.')
	print()

def chooseCoin():
	coin = ' '
	while coin != '앞' and coin != '뒤':
		print('어느 면을 고르시겠습니까? (앞 또는 뒤)')
		coin = input()

	return coin

def checkCoin(chosenCoin):
	print('남자가 동전을 하늘 높이 던져올립니다...')
	time.sleep(2)
	print('동전은 정점을 찍고 바닥으로 떨어지기 시작했습니다...')
	time.sleep(2)
	print('짤그랑 소리와 함께 구르던 동전은....')
	print()
	time.sleep(2)

	rightCoin = random.randint(1, 2)

	if rightCoin == '1':
		rightCoin = '앞'
	else:
		rightCoin = '뒤'


	if chosenCoin == rightCoin:
		print('성공입니다! 당신은 세상의 모든 부를 얻었습니다!')

	else:
		print('시ㅡ망입니다.')

playAgain = '예'
while playAgain == '예':

	displayIntro()

	coinSide = chooseCoin()

	checkCoin(coinSide)

	print('한 번 더, 도전해 보시겠습니까?')
	playAgain = input()
