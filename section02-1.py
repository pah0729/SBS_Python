# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python""")
print('''Hello Python''')

print()

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2020', '10', '16', sep='-')
print('admin', 'test.com', sep='@')

print()

# end 옵션 사용
print('Welcome To', end='')
print('the black parada', end=' ')
print('piano notes')

print()

# format 사용
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ('Eunki', 7))
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test2: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123))
print("Test3: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.123))

print()

"""
참고 : Escape 코드

 \n : 개행
 \t : 탭
 \\ : 문자
 \' : 문자
 \" : 문자
 \r :캐리지 리턴
 \f : 폼 피드
 \a :벨 소리
 \b :백 스페이스
 \000 : 널 문자
 ...

"""

print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('\t\t\ttest')