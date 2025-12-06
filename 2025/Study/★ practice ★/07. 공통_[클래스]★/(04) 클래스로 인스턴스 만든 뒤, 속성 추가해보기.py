# 지금까지 __init__로 인스턴스 속성을 만들었다.
# 하지만,이와 다르게 클래스를 만들고, 인스턴스.속성 = 값 으로 추가 가능하다.

class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아',20,'부산광역시'])
maria.Survive = "True"
print(maria.Survive)

# 이렇게 추가한 인스턴스의 속성은 다른 클래스에서 해당 속성을 사용할 수 없습니다.