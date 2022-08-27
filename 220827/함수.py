# 응용 예제
# 무지개의 일곱 색깔을 저장하는 rainbow 리스트를 생성하고 다음과 같이 출력
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
for 인덱스, 값 in enumerate(rainbow):
    print('무지개의 {}번째 색은 {}입니다'.format(인덱스+1, 값))


#
#
exam = []
print('점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.')
while True:
    점수 = int(input('점수 입력 >>>'))
    if 점수 < 0:
        break
    else:
        exam.append(점수)
print(exam)

최대 = max(exam)
최소 = min(exam)
avreage = sum(exam) / len(exam)

print('평균 = {}, 최대 = {}, 최소 = {}'.format(avreage, 최대, 최소))

#
#
국번 = input('전화번호를 입력하세요 >>')

print(국번.split('-')[1])

#
#
번호 = input('사업자등록번호를 입력하세요 >>> ')

if len(번호) != 12:
    print('올바른 형식이 아닙니다.')
else:
    if 번호[3] == '-' and 번호[6] == '-':
        if 번호.replace('-', '').isdecimal():
            print('올바른 형식입니다.')
        else:
            print('올바른 형식이 아닙니다.')
    else:
        print('올바른 형식이 아닙니다.')