# 클래스 안에서 self로 접근할 수 있고, 인스턴스.속성 형식으로 클래스 밖에서도 접근 가능
# Person은 self를 사용해서 클래스 안, 클래스 밖에서 사용한 것, <> Person_2는 self.__속성 사용해서, 안에서만 접근 가능하게 만듬.
class Person:
    def __init__ (self, name, age, address):
        self.hello = "안녕하세요!"
        self.name = name
        self.age = age
        self.address = address

maria = Person('마리아',50,"뉴욕")
maria.name

class Person_2 :
    def __init__(self, name,age,addrees,wallet):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = addrees
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만든다.

lolen = Person_2('마리아',50, '뉴욕')
lolen.__wallet -= 1000
# TypeError: __init__() missing 1 required positional argument: 'wallet' : 비공개 속성이라 접근 불가! 지갑은 본인만 갖고 있고, 바깥에서 마음대로 돈을 뺄 수 없는걸 볼 수 잇다!