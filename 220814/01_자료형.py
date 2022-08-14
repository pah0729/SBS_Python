"""
 자료형 ?
 - 정수 int : 3 0 -1
 - 실수 float : 0.1 0.555
 - 문자 = 문자열 python에선 동일
    - 문자 : char
    - 문자열 : string

- Boolean 변수(논리) : True(1), False(0) : 플래그 변수
- 리스트 list(배열) : 여러 값을 저장할 때 쓰는 변수
- 튜플 tuple(배열) : 변경이 불가 = 배열을 상수처럼 쓸 때
- 세트 set(배열) : 변경 가능 대신 중복 불가
- 딕셔너리 (dict) : { "key" : "value" }
"""

# 문자열 변환

a = 10.5
print(type(a))
print(int(a))

# 예제
# 1. 사용자한테 숫자를 입력 받고
# 2. 사용자가 입력한 값의 10배를 출력

b = input('값을 입력해주세요 : ')

print(f'입력하신 값은 {b} 입니다')

print(type(b))

c = print('입력하신 값의 10배는 :',int(b) * 10,'입니다.' )

print(type(c))

print("1-1", "1-2", "1-3",end = "\n")
print("1-1", "1-2", "1-3",sep = "")




# 인덱싱, 슬라이싱
name_1 = '박계현, 26세'
print(name_1[:3])

# split
print(name_1.split(','))
print(name_1.split(',')[0])
print(name_1.split(',')[-1].strip()) #strip 공백 제거
input('입력:')

# string 포맷팅
age = 26
print('제 나이는 ', age, '살 입니다.')
print('제 나이는 {}살 입니다.'.format(age)) # py3
print('제 나이는 %s살 입니다.' %(age)) # py2
print(f'제 나이는 {age}살 입니다.') # 최근