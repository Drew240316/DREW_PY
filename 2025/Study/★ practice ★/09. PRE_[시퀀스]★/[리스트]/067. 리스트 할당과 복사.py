# a와 b를 같은 리스트로 만들어라.

a = [11,12,13,14,15 ]
b = a

print(" 리스트 요소 확인 :",a)

c = a is b
print("true인가?", c)





# a와 b를 다른 변수에 넣고 싶으면?

a = [0,0,0,0,0,0,0,0,0,0,0,0]
b = a.copy()
print("b의 요소들",b)
print("a의 요소들",a)


c = a is b
print("true인가?", c)
