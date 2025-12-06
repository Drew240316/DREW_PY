# 주제 : 원소의 값을 입력 받고, 가장 큰 값을 출력하는 함수를 구현하시오.
# 자료형
    # 시퀀스는 int float str 등의 타입을 요소로 갖는 순서형 자료.
    # (a: Sequence ) -> Any  #시퀀스 형의 어떤 타입(Any)이던 유연하게 받아 반환하겠다.
# 객체 : Any, Sequence / nums / i -> one_of_num / maximum /
# 패키지.모듈 - 클래스 from Typing import Any, Sequence
# 이론 : 큰 값을 만나면 맥시멈으로 움직이는 배열
# 로직 : 1) 큰 값 찾는 함수 2) 원소의 개수를 정하고, 원소의 값을 리스트 자료형으로 저장하는 조건 실행문


from typing import Any, Sequence
#타이핑 모듈의 # Any, Sequence 클래스

def max_of(a:Sequence) -> Any :
    maximum = a[0]

    for i in range(len(a)):
        if a[i] > maximum :
            maximum = a[i]
    return maximum

                                    # 모듈 : 하나의 스크립트 프로그램이라고 하며, 확장자 .py를 사용해서 파일의 이름 자체를 모듈 이름 사용
                                    # if문에서 __name__과 __main__이 같은지 확인한다. __name__은 모듈이라는 뜻이다. 
if __name__ == '__main__':          # 스크립트 프로그램이 직접 실행될 때 사용 <> 스크립트 프로그램 임포트? __name__이 사용.
    nums = int(input(f'원소의 개수는? : '))
    x = [None] * nums

    for i in range(nums):
        x[i] = int(input(f' 원소의 값들을 개수만큼 입력하고싶다. x[{i}]를 입력하세요.'))

    print(f'최댓값은 {max_of(x)}')