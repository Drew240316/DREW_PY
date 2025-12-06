try : # 트라이에서 정상작동이 else에서 실행됩니다.
    x = int(input('나눌 숫자를 입력해라: '))
    y = 10/x

except ZeroDivisionError: # 에러발생.
    print('숫자를 0으로 나눌 수 없다.')

else:
    print("올바른 답입니다.",y)


# try-except-else
# try가 에러 없이 정상 실행되면 else가 실행되고,
# try에서 에러가 나면 except가 실행되며, 이 경우 else는 절대 실행되지 않는다.