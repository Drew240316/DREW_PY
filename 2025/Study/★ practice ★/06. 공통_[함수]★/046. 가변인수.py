def print_numbers(*args):
    """ *은 이터러블 객체 사용
        - *args(가변 인수)는 여러 개 값이 들어갈 수 있다.
        - 가변 위치 인자가 아닌 이상* 여러 개 값을 직접 받으면 안 된다."""
    for i in args:
        print(i)


print_numbers(10,20,30,40,50,60)



x = range(3)
print_numbers(*x)
