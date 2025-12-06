# self : 인스턴스 자기 자신을 의미한다.
# 우리는 인스턴스가 생성될 때 self.hello=안녕하세요 처럼 자기 자신에 속성을 추가할 수 있다.
# __init__의 매개면수 self에 들어가는 값은 Person()그 자체라할 수 있고, self가 완성된 뒤, james에 할당된다.
# 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어온다.
# 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어온다.그래서 greeting이 호출가능
class Person:
    def __init__(self):
        self.hello = "안녕하세요."

    def greeting(self):
        print('self.hello')

james = Person()
james.greeting
