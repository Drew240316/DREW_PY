#class 기반클래스이름1:
  #  코드


#class 기반클래스이름2:
  #  코드


# class 파생클래스이름(기반클래스이름1, 기반클래스이름2):
  #  코드


class Person:
    def greeting(self):
        print('안녕하세요.')


class University:
    def manage_credit(self):
        print('학점 관리')


class Undergraduate(Person, University):
    def study(self):
        print('공부하기')


james = Undergraduate()

# Undergaduate 클래스에 별도의 __init__ 메서드를 정의하지 않았기 때문에, 파이썬은 자동으로 object의 기본 생성자(__init__(self))를 사용합니다.
# 이 기본 생성자는 아무 인자도 받지 않으므로  () 괄호로만 표시되는 것.

james.greeting()  # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()  # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()  # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드


# 메서드 탐색 순서 mro
# 클래스.mro()
print(Undergraduate.mro())  # 언더그래듀에이트 갔다가 펄슨값다가, 유니벌시티 감.
