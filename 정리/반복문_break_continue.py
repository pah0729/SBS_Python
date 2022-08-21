"""
break
loop를 중단할 때
보통 조건문 안에서 수행, 조건을 만족하는 경우 루프 탈출을 위해 사용
loop를 중단 하는 경우, while 이후의 코드 수행

continue
break 처럼 반복을 중단 하여 빠져나오지 않고, 다시 while 조건으로 점프
특정한 경우에는 코드를 수행하지 ㅇ낳고 다음으로 건너 뛰기 위해 사용
"""

a = [1, 10, 9, 24, 25, 26]
i = 0
while i < len(a):
    if a[i] > 20:
        break
    print(a[i])
    i += 1

print('hahaha')

"""
while True: # 데이터를 크롤링 할 때
    data = crawl()
    if data == None:
        break # 데이터가 없으면 중단
    print(data)
"""

a = 7
while a > 0:
    a -= 1
    if a == 5:
        continue # 5는 점프
    print(a)

# ----------------------------------------------------------------------

# 1 ~ 100까지 더하기
num = 1
_sum = 0
while num <= 100:
    _sum += num
    num += 1
print(_sum)