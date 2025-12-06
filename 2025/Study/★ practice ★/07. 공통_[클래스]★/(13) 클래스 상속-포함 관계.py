# 정확히 클래스 상속은 어디에 사용하나?
# (12)에서 만든 Student 클래스는 Person클래스를 상속받아서 만들었다
# 여기서 student는 person과 같으므로, 이처럼 상속은 동등한 관계이어야 한다. (is a) "있다 라는 개념" (사람-학생) (고양이-동물) (사원-사람) (관리자-사원) (스포츠카-자동차_
# 하지만 포함 관계는 동등한 관계가 아닌 포함의 관계다(has a) ... "가진다" 라는 개념. (교실-학생) (사람-주소) (연예인-초청장) (컴퓨터-cpu,메모리)(고객-장바구니)

class Perosn :
    def greeting(self):
        print("안녕하세요.")

class Sutduent("person"):
    def study(self):
        print('공부하기')

# 포함

class Person:
    def greeting(self):
        print('안녕하세요.')
class Perosnalist:
    def __init__(self):
        self.person_list = []
    def append_person(self,person):
        self.person_list.append(person)
