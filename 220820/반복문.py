"""
while 조건식:
    반복실행문
"""

# 응용 예제 1
# 정수를 입력받아서 그 횟수만큼 'Hello'를 출력한는 프로그램을 구현
num = int(input('정수를 입력하세요 >>> '))
while num >= 1:
    print(num)
    num -= 1

# 응용 예제 2
# 1부터 100 사이의 모든 정수 중 7의 배수만 출력
i = 1
while i <= 100:
    i += 1
    if i%7 == 0:
        print(i)