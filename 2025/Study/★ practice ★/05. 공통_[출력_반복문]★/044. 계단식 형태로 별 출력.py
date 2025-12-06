# 계단식으로 별 출력하기
#     5칸의 계단을 만들고 싶습니다.

for i in range(5):
    for j in range(5):
        if j <= i :
            print('☆', end = ' ')
    print()