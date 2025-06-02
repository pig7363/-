# 1번문제
while True:
    sen = input()
    if sen != 'pu_ang':
        print('다시 입력하세요')

    else:
        print('중앙대학교 마스코트')
        break

# 2번문제
class ElectronicDevice:
    def __init__(self, name, watt):
        self.name = str(name)
        self.watt = int(watt)

class TV(ElectronicDevice):
    def __init__(self, name, watt, hours_per_day):
        super().__init__(name, watt)
        self.hours_per_day = hours_per_day
        self.get_daily_usage()

    def get_daily_usage(self):
        print(f'{self.name} 하루 전력 사용량 {self.watt * self.hours_per_day:.2f}', "Wh")

class Laptop(ElectronicDevice):
    def __init__(self, name, watt, usage_hours):
        super().__init__(name, watt)
        self.usage_hours = usage_hours
        self.get_daily_usage()

    def get_daily_usage(self):
         print(f'{self.name} 하루 전력 사용량 {self.watt * self.usage_hours * 0.8:.2f}', "Wh")

# 3번 문제
menu = {'아메리카노': 2400, '카페라떼': 2900, '아이스티': 2900, '아샷추': 3400, '카야토스트': 3000}

def f_price():
    price = 0
    history = {}

    order = input().split(',')

    for m in order:
        order1 = m.strip()
        if order1 == "아무거나":
            order1 = "아메리카노"
        if order1 not in menu:
            return
        if order1 in history:
            history[order1] = history[order1] + 1
        else:
            history[order1] = 1
        price = price + menu[order1]

    for order1 in history:
        print(order1, ":", str(history[order1]) + "잔")
    
    print("총 금액은", str(price) + "원 입니다.")

f_price()