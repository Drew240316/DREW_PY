a = []

for i in range(10):
    a.append("숫자")
print(a)


b = []

for i in range(10):
    b.extend("숫자")
print(b)

###################################
c = []

for i in range(10):
    c.append(7)
print(c)


#d = []

#for i in range(10):
    #d.extend(7)
#print(d)

# 문자
# append → 전체 문자열을 하나의 항목으로 추가
# extend → 한 글자씩 쪼개서 각각 추가

# 숫자
# append → 숫자 하나를 항목으로 추가
# extend → 숫자는 이터러블이 아니라 에러 발생
#         → 숫자를 [숫자]로 감싸 리스트 형태로 주면 추가 가능


#### 관련 058. 리스트 욧 추가(여러개)