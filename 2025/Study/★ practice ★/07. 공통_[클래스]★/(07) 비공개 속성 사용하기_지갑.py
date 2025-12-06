class Shopping_list:
    def __init__ (self,bag,cosmetic,cloths,wallet_total):
        self.bag = bag
        self.cosmetic = cosmetic
        self.cloths = cloths
        self.__wallet_total = wallet_total #초기화 꼭 해주세요.
        print("고객님이 오늘 구매하신 물품은 가방, 화장품, 옷 입니다.\t 카드 주세요")


    def wallet(self):
        self.__wallet_total = int(input("지갑에 얼마있어요?(속닥..>//<)"))

    def pay(self,amount):
        if amount > self.__wallet_total :
            print("돈이 모자라네.")
            return
        self.__wallet_total -= amount


class Basket:
    def __init__(self):
        self.personal_basket_in = []

    def add_to_basket(self, *items):
        self.personal_basket_in.extend(items)
        print('장바구니에 담은 물건: ')

    def count(self):
        print(f'총 {len(self.personal_basket_in)가 있습니다.}')


class Inventory:

    def several_inventory(self):   # inventory의
        bag_section = {'가방':'나이키 가방', '가방':'프로스펙스 가방', '가방' : '르꼬끄 가방'}
        cosmetic_section = {'입큰':'입큰 립스틱','웨이크 메이크':'웨이크 메이크 새도우', '설화수' : '설화수 팩트'}
        cloths_section = {'잇미샤':'잇미샤 셔츠','나이키':'나이키 트레이닝복','아디다스':'아디다스 트레이닝복'}

    def inventory_pay(self):


    def count(self):





maria = Shopping_list("나이키 가방", "설화수 팩트", "잇미샤 셔츠",50000)
maria.wallet() #pay전에 먼저 호출해야 pay가실행됨
maria.pay(99900)