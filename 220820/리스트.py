                # 0번째, 1번째, 2번째 ....
                # -3번째, -2번째, -1번째...
a_tuple = ('안녕하세요', '저는', '박계현입니다') # () -> Tuple
           # [0]         [1]         [2]
           # [-3]        [-2]        [-1]
a_list = ['안녕하세요', '저는', '박계현입니다'] # [] -> List



print(a_list)

a_list.append('마지막')

print(a_list)
a_list = ['앞에 추가'] + a_list
print(a_list)
a_list.insert(1, '첫번')
print(a_list)
a_list.remove('첫번')
print(a_list)
a_list.pop() # 삭제
print(a_list)
b_list = a_list.copy() # 복사 / b_list = a_list mutable, immutable
print(b_list)


# 1부터 10까지 출력
# 1부터 100까지 더한값을 출력해보세요
"""
a = 1
a = a + 1
"""
sum = 0
for sum in range(1, 101):
    sum = sum + 1
print(sum)
