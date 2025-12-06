a = [ [10,20],[30,40],[50,60] ]
i = 0


while i < len(a):
    j = 0
    while j < len(a[i]):  #
        print(a[i][j], end = ' ')
        j += 1
    print()
    i += 1

# 생각 할 것
# 1. i는 큰 리스트 한 개(가로), j 는 리스트 안의 각 요소(세로)
# 2. LEN은 총 길이 갯수
# 3. 조건문은 True인지 False인지
# 4. print()는 줄바꿈
# 5. 10을 찾으면 20을 찾아야 함.
