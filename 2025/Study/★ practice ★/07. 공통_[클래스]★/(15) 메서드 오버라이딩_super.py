# 자식 클래스에서 부모 클래스의 메서드를 기반으로 새로 정의하는 메서드 오버라이딩이다.
# Person의 greeting메서드가 있는 상태에서 Student에도 greeting메서드를 만들면, Student의 greeting만 사용된다.
# 이처럼, 오버라이딩(overriding)무시하다.우선하다라는 뜻으로, 말 그대로 부모 클래스의 메서드는 무시하고 새로운 메서드를 만든다는 뜻이다.
# 메서드 오버라이딩은 왜 사용? 프로그램에서 어떤 기능이 메서드 이름을 계속 사용해야할 떼, 메서드 오버라이딩을 사용한다. 이 때 greeiting2처럼 계속 2 3을 붙이면서 수정하기에 쉽지않다.



# 1. 완전 오버라이딩 :  부모의 구현을 완전히 대체(replace)만 한 것
#:출력이 "안녕하세요. 저는 파이썬 코딩 도장 학생입니다.")로 Pesron의 안녕하세요를 무시하고, 출력된다.
class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')


james = Student()
james.greeting()

#2.  부모의 메서드를 호출(super)한 뒤 추가 동작을 하는, 즉 “오버라이딩하면서 확장(extend)”한 것
# 출력이 "안녕하세요. 한줄 띄고, 저는 파이썬 코딩 도장 학생입니다.")만 출력된다.
# 이처럼 중복되는 안녕하세요 기능을 중복제거하고 출력한다.


class Person_2:
    def greeting(self):
        print('안녕하세요.')


class Student_2(Person_2):
    def greeting(self):
        super().greeting()  # 기반 클래스의 메서드 호출하여 중복을 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')


james = Student_2()
james.greeting()