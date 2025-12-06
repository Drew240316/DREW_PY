import random
from max import max_of

num = int(input(f'난수 값의 개수는 ? '))
start = int(input(f'난수의 최소 시작값은? '))
end = int(input(f'난수의 최댓값은? '))
result = [None]*num

for i in range(num) :
    result[i] = random.randint(start,end)

print(f'난수값들은 {result}입니다.')
print(f'가장 큰 값은 {max_of(result)}')
