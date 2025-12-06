def print_numbers(a,b,c):
    """ 위치 인수는 함수 호출 시, 위치가 고정된 인수다.
     - 위치 인수는 리스트, 튜플, [문자], range 등 모든 iterable 가능
     - 주의) 함수 정의와 함수 호출의 실제 값의 개수가 같다.
    """
    print(a)
    print(b)
    print(c)

print_numbers(10,20,30)
print(print_numbers.__doc__)


date_r = range(3)
print_numbers(*date_r)

date_l = [1,2,3]
print_numbers(*date_l)

data = "XYZ"
print_numbers(*data)
