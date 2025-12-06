# 파이썬은 추상 클래스라는 기능을 제공한다.
# 추상 클래스는 메서드의 목록만 가진 클래스이며, 상속받는 클래래스에서 메서드 구현을 강제하기 위해 사용한다.
# 무엇에 사용 ? 동물의 speak - 강아지 spaek와 고양이의 speak는 다르다.  / 운수 drive - 버스 dirve와 오토바이 dirve
# import로 abc모듈을 가져온다. (앱스트랙트 베이스 클래스)
# 괄호안에 metaclass = ABCMeta 지정.
# 메서드 만들 때 위에, @abstractmethod를 붙인다.
#from abc import *
 #   class 추상클래스 이름 (metaclass=ABCmeta):
  #      @abstractmethod
   #     def 메서드 이름(self):
    #       코드

from abc import *


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):    #만약 go_to_school을 자식클래스에서 안쓰면 에러발생
            #TypeError: Can't instantiate abstract class Student with abstract methods go_to_school
        print('학교가기')


james = Student()
james.study()
james.go_to_school()

# 추상 클래스(abstract class)와 메서드 오버라이딩(override)은 함께 쓰이는 개념
 # 추상 클래스

    # @abstractmethod를 붙인 메서드는 “구현되지 않은 틀”만 제공

    # 하위 클래스가 이 메서드를 반드시 구현(overriding)하도록 강제

    # 부모 클래스만으로는 인스턴스를 만들 수 없습니다.

# 메서드 오버라이딩

    # 부모 클래스에 정의된 메서드(추상 메서드 혹은 일반 메서드)를

    # 자식 클래스에서 같은 이름으로 다시 정의하여 구현을 대체하거나 확장
