from max import max_of  #max 모듈에서 정의한 max_of 함수를 사용해보자.

print("배열의 최댓값을 구합니다.")
print("주의: 'end'를 입력하면 종료합니다. ")

number = 0
x = []

while True:
    s = input(f'x[{number}]값을 입력하세요: ')  #인덱스
    if s =='end':
        break

    x.append(int(s))
    number += 1

print(f'{number}개를 입력하세요.')
print(f'최댓값을 {max_of(x)}입니다.')