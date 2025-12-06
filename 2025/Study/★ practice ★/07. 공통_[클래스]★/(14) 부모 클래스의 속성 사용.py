class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()  # super()로 기반 클래스의 __init__ 메서드 호출 (super가 없으면 부모 클래스의 속성 사용 불가)/
                                # AttributeError: 'Student' object has no attribute 'hello'
                                # 기반 클래스 Person의 __init__ 메서드가 호출되지 않았기 때문입니다.
                                # 실행 결과를 잘 보면 'Student __init__'만 출력되었습니다.
        self.school = '파이썬 코딩 도장'  #self(인스턴스).속성 = 데이터


james = Student()
print(james.school)  #인스턴스.속성 을 불러야 데이터 값 출력.
print(james.hello)



#변형
#class Person:
 #   def __init__(self):
  #      print('Person__init__') # 부모 클래스의
   #     self.hello = '안녕하세요.'  # 인스턴스.속성 = 데이터.
    #    print(self.hello) #속성 할당 즉시 출력

#class Student(Person):
 #   def __init__(self):
  #      super().__init__()
   #     print('Student__init__')
    #    self.school = '파이썬 코딩 도장'
     #   print(self.school)  # 속성 할당 뒤 즉시 출력

# lola = Student()
