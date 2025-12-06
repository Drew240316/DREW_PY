# 상속 : 무언가 물려받다.
# 클래스 상속 : 물려받은 기능을 유지한채로 다른 기능을 추가할 때 사용. 물려받을 때 연관되는 개념이어야 함.
# 부모 클래스에서 ()를 써준다. 자식 클래스에서 (부모클래스명)을 쓴다.
# class 부모 클래스 이름:
    #코드
# class 자식 클래스 이름(부모클래스이름)
    #코드

class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def study(self):
        print('공부하기')

james = Student()
james.greeting()
james.study()

# 클래스가 상속관계인지 알려면?
# issubclass(자식클래스, 부모클래스)

issubclass(Student, Person)  #맞으면 True나옴