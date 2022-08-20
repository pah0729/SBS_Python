"""
- if - else
 if 조건식 :
    조건식의 결과가 True일 때 실행문

if 조건식:
    조건식의 결과가 True일 때 실행문
else:
    조건식의 결과가 False일 때 실행문

- if -elif
if 조건식 1:
    조건식 1의 결과가 True일 때 실행문
elif 조건식2:
    조건식 1의 결과가 False이고, 조건식 2의 결과가 True일 때 실행문
else:
    조건식 1, 2의 결과가 모두 False일 때 실행문
"""

# 응용 예제 1
# 점수를 입력받아서 학점을 출력하는 프로그램을 구현
# 100~90 : A, 89~80 : B, 79~70 : C, 69~60 : D, 59~0 : F
score = int(input('점수를 입력하세요 >>> '))

if score >= 90:
    credit = 'A'
elif score >= 80:
    credit = 'B'
elif score >= 70:
    credit = 'C'
elif score >= 60:
    credit = 'D'
else:
    credit = 'F'

print(f'입력하신 점수는 {score}점이고, {credit}입니다!')

# 응용 예제 2
# 임의의 정수를 입력받은 뒤 3의 배수인지 아닌지 판별
multiple_of_3 = int(input('정수를 입력하세요 >>> '))

if multiple_of_3%3 == 0:
    print(multiple_of_3, '은/는 3의 배수입니다.', sep='')
else:
    print(f'{multiple_of_3}은/는 3의 배수가 아닙니다.')

# 응용 예제 3
# 임의의 정수 세개를 입력 받아 그 중 가장 큰 수를 출력
essence_1st = int(input('첫번째 정수 입력'))
essence_2nd = int(input('두번째 정수 입력'))
essence_3rd = int(input('세번째 정수 입력'))

if essence_1st > essence_2nd and essence_1st > essence_3rd:
    print('가장 큰 수는 %i' %essence_1st)
elif essence_2nd > essence_3rd:
    print('가장 큰 수는 %i' %essence_2nd)
else:
    print('가장 큰 수는 %i' %essence_3rd)

# 응용 예제 4
# 미세먼지 저감 활동의 일환으로 차량 2부제 실시
# 차량번호가 짝수 -> 운행가능, 홀수 -> 운행 불가
"""
숫자만 받을 경우
car_num = list(map(int, input('차량번호를 입력하세요 ex) 1234 >>> ')))
if car_num[-1]%2 == 0:
    print('오늘 운행가능입니다.')
else:
    print('오늘은 운행불가입니다.')
"""
car_num = input('차량번호를 입력하세요 >>> ')
last_car_num = int(car_num[-1])

if last_car_num%2 == 0:
    print('오늘 운행가능입니다.')
else:
    print('오늘은 운행불가입니다.')

# 응용 예제 5
# 1 ~ 100까지의 숫자중 홀수의 합, 짝수의 합
synthesis = 0
even = 0
odd_num = 0

for i in range(1, 101):
    synthesis = synthesis + i
    if i%2 == 0:
        even = even + i
    else:
        odd_num = odd_num + i

print(synthesis)
print(even)
print(odd_num)