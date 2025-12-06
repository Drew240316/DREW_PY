# push x : 정수 x를 스택에 넣는다.
# pop 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
# top : 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있지 않으면 -1
# size : 스택에 들어있는 정수의 개수를 출력한다.
# empty : 스택이 비어있으면 1, 아니면 0을 출력한다.

n = int(input())
stack = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    if cmd == 'push':
        num = int(s[1])
        stack.append(num)
    elif cmd == 'pop':
        if stack :
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 'top':
        if stack :
            print(stack[-1])
        else:
            print(-1)
    elif cmd == 'size':
        print(len(cmd))
    elif cmd == 'empty':
            print( 0 if stack else 1 )

