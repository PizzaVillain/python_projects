#-*- coding: utf-8 -*-
import random

guessesTaken = 0

print('자넨 이름이 뭔가?')
userName = input()

print('만나서 반갑구만, ' + userName + '!')

number = random.randint(1, 100)

print('이봐, ' + userName + ', 내가 지금부터 숫자를 하나 생각할 건데, 1에서 100 사이야. 맞춰보라구!! 하하ㅡ하하하!')

while guessesTaken < 6:
    print('맞춰보시지, 얼마인 거 같나?')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if number < guess:
        print('숫자가 너무 크잖아!! 얼간아!! 하ㅡ하하하하!')

    if number > guess:
        print('소심한 멍청이 같으니라고? 그렇게 작은 숫자로 되겠냐!!')

    if number == guess:
        break

if number == guess:
    guessesTaken = str(guessesTaken)
    print(userName + ', 제법 하는군, 운이 좋은건가? 쳇! ' + guessesTaken + '번만에 맞추다니!')

if number != guess:
    number = str(number)
    print('멍청아, 그것도 못 맞추냐! 정답은 ' + number + '였다구! 아ㅡ하하하!')
