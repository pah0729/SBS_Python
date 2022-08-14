"""
100 부터 999까지 숫자에 대해
X 스트라이크 X 아웃으로 맞추는 게임
1부터 0까지 중복 없음
"""

import random # 모듈
num = (1,2,3) # 컴퓨터가 고른 숫자
is_right = 0

while is_right == 0: # 사용자 값
    ans = input('값을 입력해주세요.(구분자:,)')
    ans = ans.split(',')
    ans = [int(a) for a in ans]
    print('입력한 값 :', ans)

    s = 0; o = 0

    if num == ans:
        print('3 스트라이크 0 아웃')
        print('정답:', num)
        is_right = 1
    else:
        for a in ans:
            if a in num:
                if num.index(a) == ans.index(a):
                    s = s + 1
                elif num.index(a) != ans.index(a):
                    o = o + 1
        print(f'{s} 스트라이크, {o} 아웃')