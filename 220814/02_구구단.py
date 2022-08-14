"""
 for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
"""

# range( 값1 이상, 값2 미만 )
for i in range(2, 10):
    for j in range(1, 10):
        print(i, '*', j, '=', i * j, end="\n")
    print('')

num = int(input('원하는 단을 입력 : '))
for a in range(1, 10):
    print(num, '*', a, '=', num * a)