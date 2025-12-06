# <클래스로 인스턴스를 만들 때 값을 받는 방법>

class Person:
    def __init__(self, name,age,address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print("{0} 저는 {1}입니다".format(self.hello, self.name))


maria = Person('마리아',20,'부산광역시')
maria.greeting()


print('이름: ',maria.name)  #인스턴스.속성 이라고 부른다. 출력에서 사용함.
print('나이: ',maria.age)
print('주소: ',maria.address)
