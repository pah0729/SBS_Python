"""
for 반복횟수를 정확하게 알 때
for 변수 in 반복가능객체:
    반복실행문

while 반복을 종료하는 조건을 알 때
while 조건식:
    반복실행문
"""

# 응용 예제
# 정수를 입력받아서 그 횟수만큼 'Hello'를 출력한는 프로그램을 구현
num = int(input('정수를 입력하세요 >>> '))
while num >= 1:
    print('Hello')
    num -= 1

# 응용 예제
# 1부터 100 사이의 모든 정수 중 7의 배수만 출력
숫자 = 1
while 숫자 <= 100:
    숫자 += 1
    if 숫자 % 7 == 0:
        print('while문 ', 숫자)

for 숫자 in range(1, 101):
    if 숫자 % 7 == 0:
        print('for문', 숫자)

# 응용 예제
# 커피 1잔을 300원에 판매하는 커피자판기가 있습니다.
# 이 자판기에 돈을 넣으면 자판기에서 뽑을 수 있는 커피가 몇 잔이며, 잔돈을 얼마인지 출력
돈 = int(input('자판기에 얼마를 넣을까요? >>> ')) # 넣은돈
커피한잔 = 300
커피잔 = 0
while True:
    돈 = 돈 - 커피한잔
    커피잔 = 커피잔 + 1
    print('커피잔 {}, 잔돈 {}원'.format(커피잔, 돈))
    if 돈 < 커피한잔:
        break


# 응용 예제
# 0부터 9 사이의 정수를 입력 받아, 입력된 정수가 5개가 될 때까지
num_li = [] # 입력 정수가 5개
while True:
    # 숫자 입력
    num = int(input('0~9 사이 점수를 입력하세요 >>> '))
    # 중복 확인
    if num in num_li:
        # 중복이면 점프
        continue
    else:
        # 숫자리스트에 추가
        num_li.append(num)

    if len(num_li) == 5:
        break
    # 리스트의 길이가 5면 빠져나가기

print('모두 입력되었습니다.')
print('입력된 값은 {}입니다.'.format(num_li))


# 응용 예제
# 1부터 100 사이의 모든 정수를 한 줄에 10개씩 출력


# 응용 예제
# 전체 구구단 출력
# ex) 2X1=2 3X1=1 4X1=4 5X1=5 ... 9X1=9
for 뒤 in range(1, 10):
    for 앞 in range(2, 10):
        print(f'{앞} X {뒤} = {앞 * 뒤}', end="\t")
    print('')

# 응용 예제 p129 1번
# 1에서 5사이 정수를 역순으로 출력
for l in range(1, 6, -1):
    print(l)

# 응용 예제  p129 2번
# 임의의 양의 정수를 하나 입력 받은 뒤 1부터 입력 받은 정수까지 모든 정수의 합 출력
num = int(input('정수를 입력하세요 >>> '))
_sum = 0
for i in range(1, num+1):
    _sum += i
print(_sum)

# 응용 예제 p129 3번
# 임의의 양의 정수를 하나 입력받은 뒤 그 숫자만큼 '과일 이름'을 입력 받아 basket 리스트에 저장
basket = []
while True:
    fruit = input('과일을 입력하세요')
    if fruit in basket:
        # 중복이면 점프
        continue
    else:
        # 숫자리스트에 추가
        basket.append(fruit)

    if len(basket) == 5:
        break
print('입력된 값은 {}입니다.'.format(basket))

# 응용 예제 p130 5번
# 1 부터 99 사이의 모든 정수를 대상으로  369게임의 결과를 출력하는 프로그램 구현
for 십의자리 in range(10):
    for 일의자리 in range(10):
        숫자 = (10*십의자리)+(일의자리+1)
        if 숫자 == 100:
            break

        출력짝개수 = 0
        #1의 자리가 3의 배수
        if (일의자리+1) % 3 == 0:
            # 10의 자리가 3의 배수
            if 십의자리 % 3 == 0 and 십의자리 !=0:
                출력짝개수 = 2
            else:
                출력짝개수 = 1
        else:
            if 십의자리 % 3 == 0 and 십의자리 !=0:
                출력짝개수 = 1
            else:
                출력짝개수 = 0

        if 출력짝개수 == 0:
            print(숫자, end='\t')
        else:
            print('짝'*출력짝개수, end='\t')
    print()

# 응용 예제 8 p143 4번
# 짝수인 단은 출력하지말고 blank line만 추가
# 각 단까지만 출력
# ex) 3단은 3X3까지, 5단은 5X5까지 출력
for 앞 in range(2, 10):
    if 앞 % 2 == 0:
        continue
    for 뒤 in range(1, 10):
        print(f'{앞} X {뒤} = {앞 * 뒤}', end='\n')
        if 앞 == 뒤:
            break
    print('')