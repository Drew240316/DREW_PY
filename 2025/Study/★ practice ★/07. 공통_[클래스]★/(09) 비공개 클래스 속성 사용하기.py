# 클래스 속성도 비공개 속성을 만들 수 있다. (06번은 인스턴스 비공개 속성, 메서드 비공개 속성)
# 즉, 클래스를 공개하고 싶지 않은 속성이 있다면 비공개 클래스를 사용한다. (게임 캐릭터는 아이템을 최대 10개까지만 보유)

class Knight:
    __item_limit = 10 #비공개 클래스 속성

    def print_item_limit(self):
        print(Knight.__item__limit) #클래스 안에서만 접근 가능

        x = Knight()
        x.print_item_limit() #10

        print(Knight.__item_limit)  #클래스 바깥에서는 접근 불가. 