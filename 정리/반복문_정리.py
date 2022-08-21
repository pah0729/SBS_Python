a = [1, 10, 9, 24, 26, 23, 45, 67, 89]
i = 0 # 인덱스
while i < len(a): # 비교
    print('값: ', a[i], ', index: ', i) # 인덱스 증가에 따른 출력
    i += 1 # 반복을 멈춰줄 장치

print('hahaha')

a = [1, 10, 9, 24, 26, 23, 45, 67, 89]
i = 0 # 인덱스
while i < len(a):
    if a[i] > 20: # 20보다 큰 경우
        print(a[i])
    i += 1

a = [1, 10, 9, 24, 26, 23, 45, 67, 89]
i = 0 # 인덱스
while i < len(a):
    if a[i] % 2: # 홀수인 경우
        print(a[i])
    else:
        print('뭐야', a[i] / 2)
    i += 1
