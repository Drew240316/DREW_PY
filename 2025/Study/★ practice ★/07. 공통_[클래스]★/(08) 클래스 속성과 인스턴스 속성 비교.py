# 클래스 속성 : 모든 인스턴스가 공유, 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용   출력이 ,[책,열쇠]
# 인스턴스 속성 : 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용 출력이, [책] [열쇠] (1~6까지 전부 인스턴스 속성만 함)


# 인스턴스 속성 : bag을 인스턴스 속성으로 만듬.(인스턴스 각각 공유)
class Person:
    def __init__(self):
        self.bag = []
    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

# 클래스 속성 : bag을 클래스 속성으로 만듬(어떤 인스턴스든 공유)

class Person_2:
    bag = []  # james.put_bag('책) , maira.put_bag('열쇠') 전부 사용

    def put_bag(self,stuff):
        self.bag.append(stuff)

james = Person_2()
james.put_bag('책')

maria = Person_2()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)