#-*- coding: utf-8 -*-
import random
import time
import csv

def intro():
	print('테스트 야구게임입니다.')
	time.sleep(0.5)
	print('내 마음대로 재구성하는 두산VS삼성')
	time.sleep(0.5)
	print('타자는 9명, 타순은 고정, 대타 없음.')
	time.sleep(0.5)
	print('투수는 5명의 선발투수 중 한 명이 랜덤으로 등판, 완투합니다.')
	time.sleep(0.5)
	print('경기는 9회까지 진행되니 열심히 해 보세요.')
	time.sleep(0.5)
	print('그럼, 우선 팀을 결정하겠습니다.')
	print()

def chooseTeam():
	yourTeam = ' '
	while yourTeam != '두산' and yourTeam != '삼성':
		print('두산을 원하시면 두산을, 삼성을 원하시면 삼성를 입력해주세요.')
		yourTeam = input()
		if yourTeam == '두산':
			print('두산 베어스를 고르셨습니다!')
		
		elif yourTeam == '삼성':
			print('삼성 라이온즈를 고르셨습니다!')

		else:
			print('잘못된 입력입니다.')
		#일단 귀찮아서 1 아니면 다 삼성시키기로 함. 나중에 다시 봅시다.

	return yourTeam

def chooseHome():
	#답을 정해두기
	rightCoin = random.randint(1, 2)
	#내가 동전을 던지기
	yourCoin = ' '
	while yourCoin != '1' and yourCoin != '2':
		print('선/후공을 결정하겠습니다.')
		print('앞면은 1, 뒷면은 2 입니다. 맞추시면 후공입니다.')
		yourCoin = input()
		if rightCoin == int(yourCoin):
			print('맞췄습니다!! 당신이 후공입니다!!')
			#후공처리 필요
		else:
			print('틀렸습니다!! 당신이 선공입니다!!')
			#선공처리 필요

chooseTeam()