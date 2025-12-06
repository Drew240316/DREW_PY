try :
    x = int(input())
    y = 10/x

except ZeroDivisionError:
    print('0을 입력하셔씁닌다.')

else:
    print(y)

finally :
    print('코드 실행이 끝났다.')