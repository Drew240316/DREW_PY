# 1부터 더해 100을 넘는 최초의 수 찾기 (tip: x를 누적해서 total값이 100이 넘음 됨)
# x = 1 + 1 =2...   2 + 1 = 3...
x = 1
total = 0
while 1:
    total = total + x
    if total > 100:
        print(x)
        print(total)
        break
    x = x + 1
