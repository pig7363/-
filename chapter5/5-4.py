try:
    a=[1,2]
    print(a[3])
    4/0
except IndexError:
    print("인덱싱할수 없습니다")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")