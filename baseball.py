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

def attack():
	print(inning + '회' + topBottom + ' 입니다.')
	print('타자는 ' + thisBatter + ', 투수는 ' + thispitcher + ' 입니다.')
	#타자/투수의 스탯도 출력할 필요가 있음.
	print('투수가 크게 와인드업 합니다.')
	print('배트를 휘두르시겠습니까?')
	print('휘두르시려면 1을, 공을 지켜보시려면 2를 눌러주세요')
	battingWill = ' '
	while battingWill == '1' or battingWill == '2'
		battingWill = input()
		if battingWill == '1'
			print('배팅 타입은 어떻게 하시겠습니까?')
			print('짧고 정확한 스윙은 1을, 길고 강력한 스윙은 2를 눌러주세요.')
			battingType = input()
			while battingType == '1' or battingType == '2':
				if battingType == '1':
				#타자의 스탯 + 전략 VS 투수의 스탯 + 전략으로 결과처리.
				elif battingType == '2':
				#타자의 스탯 + 전략 VS 투수의 스탯 + 전략으로 결과처리.
				else:
					print('잘못된 입력입니다.')


