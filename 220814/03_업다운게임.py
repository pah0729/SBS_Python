"""
 1에서 100까지 맞추면 됨
 + 반복문을 써야함 While문 참조

 while 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
"""

import os
print('1~100 사이의 숫자 맞추기')
num = 18

while True:
    guess =int(input('값을 입력해주세요. : '))
    if guess == num:
        print('정답입니다!')
        break
    elif guess > num:
        print('다운')
    else:
        print('업')
        break