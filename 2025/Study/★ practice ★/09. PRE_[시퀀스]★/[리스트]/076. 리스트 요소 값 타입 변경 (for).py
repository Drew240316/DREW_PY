"""리스트 요소 값을 변경하는 방법은 2가지다
    - for + index : 워언본 리스트에서 변경
    - map으로 변경 """


a = [ 1.2, 2.5, 3.7, 4.6 ]

for i in range(len(a)):
    a[i] = int(a[i])


print(type(a[i]))
