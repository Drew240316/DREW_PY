def print_numbers(x,y,z):
    """
    *은 리스트,튜플 등 이터러블 객체에 사용하는 언패킹 방법

    1. '이터러블'을 변수에 저장한 후, '호출 시 *'로 '언패킹'하여 위치 인자로 전달
       예: i = [10, 20, 30]
           print_numbers(*i)

    2. 호출 시 직접 '*'로 '언패킹'하여 함수 호출 (아래 주석 참고)
       예: print_numbers(*[10, 20, 30])
    """
    print(x); print(y); print(z)

i = [10,20,30]

print_numbers(*i)
print(print_numbers.__doc__)


# 추가 방법) print_numbers(*[10,20,30])


