y = [10,20,30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 각각 입력하시오 (정수 2개): ').split())
    print(y[index],x)

except ZeroDivisionError: #숫자를 0으로 나눠서 에러가 발생했을 때 실행
    print('숫자를 0으로 나눌 수 없다.')

except IndexError: #범위를 벗어나 인덱스에 접근하여 에러 발생
    print('범위를 벗어난 인덱스입니다.')

# try-except-except
# try에서 정상 작동하면 아무 일도 없이 넘어가고,
# try에서 에러가 발생하면 해당 에러의 종류에 맞는 except 블록이 실행된다.