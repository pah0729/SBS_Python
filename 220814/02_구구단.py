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


# 반복문의 필요성
단 = int(input('단을 입력:'))
"""
print("{} X {} = {}".format(단, 1, 단*1))
print("{} X {} = {}".format(단, 2, 단*2))
print("{} X {} = {}".format(단, 3, 단*3))
print("{} X {} = {}".format(단, 4, 단*4))
print("{} X {} = {}".format(단, 5, 단*5))
print("{} X {} = {}".format(단, 6, 단*6))
print("{} X {} = {}".format(단, 7, 단*7))
print("{} X {} = {}".format(단, 8, 단*8))
print("{} X {} = {}".format(단, 9, 단*9))
"""

for c in [1,2,3,4,5,6,7,8,9]:
    print("{} X {} = {}".format(단, c, 단*c))