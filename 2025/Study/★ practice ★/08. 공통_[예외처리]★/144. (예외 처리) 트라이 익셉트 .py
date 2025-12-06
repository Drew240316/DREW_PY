try : # try에서 에러 발생 시 실행되지 않습니다.
    x = int(input('나눌 숫자열 입력: '))
    y = 10 / x
    print(x)

except: #에러 발생 시 실행됩니다.
    print('예외 발생')


