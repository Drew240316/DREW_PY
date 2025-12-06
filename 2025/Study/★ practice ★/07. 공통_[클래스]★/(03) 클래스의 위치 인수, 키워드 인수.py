# 클래스로 인스턴스를 만들 때는 "위치 인수(01,02)","키워드인수"를 사용한다.
# 위치 인수와 키워드 인수는 가변적일 수 있는데, 가변일 때는 *로 표시한다.  언패킹도 사용가능하다 *args **kwargs
#
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아',20,'부산광역시'])
