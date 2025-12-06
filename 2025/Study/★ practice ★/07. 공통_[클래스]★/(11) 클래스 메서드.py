<클래스 내부에서만 메서드 속성 공유할 건 공유하고, 아닌건 안하고.> = 공통으로 상요할 메서드 n개, 분기별로 나눌 메서드 n개


# 클래스 메서드는 무엇을 만드나 ? 마법사 생성 공장 - 불독/썬콜 처럼 여러 스타이별 마법사를 쉽게 만들고 싶을 때
# 정적 메서드와 차이? 정적 메서드는 인스턴스 속성, 클래스 속성 접근이 불가한, 클래스 메서드는 클래스 내부에서 접근 가능. 그리고 cls라는 첫 번째 매개변수를 꼭 지정한다.
# 클래스 메서드는 인스턴스를 직접 생성하지 않아도, 클래스 자체를 통해 __init__()에 필요한 인자를 전달해 객체를 만들 수 있다.
# 이때, 클래스 메서드 안에서 필요한 값(power 등)을 직접 지정해서 넣어주면,
# 호출하는 쪽에서는 그 값을 따로 넘길 필요가 없다.  반대로 정적 메서드는, 해당 정적 메서드의 계산된 값의 결과만 줌.
#class 클래스 이름:
    #@classmethod
    #def 메서드(cls, 매개변수1, 매개변수2):
        #코드

class Wizard :
    def __init__(self, name, job, power, level):
        self.name = name
        self.job = job
        self.power = power
        self.level = level

    def wizard_spell(self):
        print(f"{self.name}님의 직업은 {self.job}입니다.".format(self.name, self.job))
        print(f"{self.power}의 힘을 가졌습니다. 레벨은 {self.level}입니다.")

    @classmethod
    def fire_wizard_lv_10(cls, name, job):
        return cls(name,job,"불의 정령","10")

    @classmethod
    def ice_wizard_lv_10(cls,name,job):
        return cls(name,job,"얼음 정령", "10")

maria = Wizard.fire_wizard_lv_10("마리아","전직 예정자")  #인스턴스에 넣지 않고, 바로 클래스의 메서드 호출!
maria.wizard_spell()

dora = Wizard.ice_wizard_lv_10("도라","전직 예정자")
dora.wizard_spell()

