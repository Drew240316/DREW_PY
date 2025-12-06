fare = 1350
value = int(input("금액을 충전하세요: "))

while value >= 1350:
    value -= fare
    print("사용금액: 1350원", "남은금액: ", value)

if value <= 1349:
    print("충전해주세요.")
