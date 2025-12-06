def valid(s):
    cnt = 0
    for ch in s :
        if ch == '(':
           cnt += 1
        else :

            cnt -= 1
        if cnt < 0 :
            return 'No'
    if cnt == 0:
        return 'Yes'
    else:
        return 'No'

t = int(input())

for _ in range(t):
    print(valid(input()))
