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
# 100~90 : A
# 89~80 : B
# 79~70 : C
# 69~60 : D
# 59~0 : F

credit = int(input(print('점수를 입력하세요 >>> ')))

if credit >= 90:
    print('A 입니다!')
elif credit >= 80:
    print('B 입니다!')
elif credit >= 70:
    print('C 입니다!')
elif credit >= 60:
    print('D 입니다!')
else:
    print('F 입니다!')

# 응용 예제 2
# 임의의 정수를 입력받은 뒤 3의 배수인지 아닌지 판별

multiple_of_3 = int(input(print('정수를 입력하세요 >>> ')))

if multiple_of_3%3 == 0:
    print(multiple_of_3, '은/는 3의 배수입니다.', sep='')
else:
    print(f'{multiple_of_3}은/는 3의 배수가 아닙니다.')