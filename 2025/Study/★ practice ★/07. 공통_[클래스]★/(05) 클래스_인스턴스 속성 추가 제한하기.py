# 인스턴스는 자유롭게 속성을 추가할 수 있지만, 특정 속성만 허용하고 싶을 때 __slots__ = ['속성이름','속성이름']을 사용한다. <-다른 속성 허용하지 않겠다는 말.

class Person:
    __slots__ = ['name','age']

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greeting(self):
        print('{0}님은 {0}입니다.'.format(self.name, self.age))

maria = Person('maria','20')
maria.greeting()
maria.birtyday = '2017/01/01'

# __slots__써서 AttributeError: 'Person' object has no attribute 'birtyday'