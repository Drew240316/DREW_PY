"""제너레이터?
    - 제너레이터는 데이터를 "미리 안 만들고", "필요할 때 생성하는 함수""""


a = [ i for i in range(10) ]
print("리스트 컴프리헨션으로 리스트 생성",a)


b = list(i for i in range(10))
print("제너레이터 표현식 사용",b)


c = [ i + 5 for i in range(10) ]
print("요소 값을 변경해서 리스트 생성 :",c)


# [표현식 for ? in  ? if 조건문 ]
d = [ i+5 for i in range(10) if i % 2 == 1 ]
print("짝수만 보여줘!: ", d)

