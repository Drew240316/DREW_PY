# 배열 원소의 최댓값을 구해서 출력하기(원소값을 난수로 생성)

import random
from max import max_of

print('난수의 최댓값을 구합니다.')

num = int(input(f'난수의 개수는 몇 개? :'))
start = int(input(f'난수의 최솟값을 얼마로? '))
end = int(input(f'난수의 최댓값은 얼마로? '))

x = [None] * num

for i in range(num):
    x[i] = random.randint(start, end)

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')
