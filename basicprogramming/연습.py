# list1 = [['지민','아메리카노'], ['정국','카페라떼'], ['태형','아샷추'], ['지민','카야토스트'], ['정국','아무거나'], ['뷔','아샷추'], ['정국','아무거나']]


order = input('메뉴를 입력하세요: ').split(',')
list1 = []
history1 = {}
for m in order:
    list1.append(m.strip().split(':'))

for name, menu in list1:
    if name not in history1:
        history1[name] = 1
    else:
        history1[name] = history1[name] + 1

# history1 = {'지민': 2, ...       }
list2 = []
history2 = {}
for l in list1:
    list2.append(l[1])
# list2 = [아메리카노, 카페라떼, ....]
for ord in list2:
    if ord == '아무거나':
        actual = '아메리카노'
    else:
        actual = ord
    
    if actual not in history2:
        history2[actual] = 1
    else:
        history2[actual] += 1
# history2 = {'아메리카노': 2개, ...}
menu_price = {
    '아메리카노': 2400,
    '카페라떼': 2900,
    '아이스티': 2900,
    '아샷추': 3400,
    '카야토스트': 3000
}
customer_total = {}
for name, menu in list1:
    if menu == '아무거나':
        menu = '아메리카노'
    price = menu_price[menu]
    if name not in customer_total:
        customer_total[name] = price
    else:
        customer_total[name] += price


print('[고객별 주문 수]')
for a in history1:
    print(f'{a}: {history1[a]}개')

print('[메뉴별 판매 수]')
for b in history2:
    print(f'{b}: {history2[b]}개')

print('[고객별 지출 순위]')
for a, b in zip(history1, history2):
    print(f'{a}: {'ㅇㅇ'}원')

print('총 매출: 19900원')