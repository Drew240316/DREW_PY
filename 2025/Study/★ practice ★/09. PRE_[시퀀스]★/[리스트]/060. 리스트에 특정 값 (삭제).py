a = [10,20,30,40,50]

a.remove(40)


print(a)


# 변수.remove()는 인자 1개만 받고 삭제
## 리턴 ) none
a = [10,20,30,40]
a.remove(20)



# del 변수[:] 인덱스 구간으로 삭제
## 리턴 ) none
b = [10,20,30,40]
del b [0:2]


# 변수.clear() 리스트 전체 삭제
c = [10,20,30,40]
c.clear()


# 특정 인자 삭제
## for + if
## 리스트 컴프리헨션
## for + if append()해서 새로운 변수 만들기
## filter() 함수
