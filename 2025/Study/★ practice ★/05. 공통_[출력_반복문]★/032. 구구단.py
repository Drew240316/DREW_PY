a = []

for j in range(2,10):
    for i in range(1,10):
        a.append(i*j)


print("for문 구구단: ",a)


b = [ i*j for j in range(2,10) for i in range(1,10)]
print("리스트 컴프리헨션 구구단 :",a)