"""
 if 조건식 :
    조건식의 결과가 True일 때 실행문

if 조건식:
    조건식의 결과가 True일 때 실행문
else:
    조건식의 결과가 False일 때 실행문
"""

a = -2

if a > 0:
    print('양수')
else:
    print('음수')

#기본 예제
age = int(input('몇 살입니까? >>> '))
if age >= 20:
    print('성인')
else:
    print('미성년자')