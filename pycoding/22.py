a=list(map(int,input("숫자를 입력하세요: ").split()))

for s in a:
    if s%2==0:
        continue
    else:
        a.remove()

print(a)