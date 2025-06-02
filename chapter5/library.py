# 소수는 1과 자기자신을 제외한 다른 수로는 나눠지지 않는 자연수


a= int(input("숫자를 입력하세요: "))

b=range(2,a)
for s in b:
    if a%s!=0:
        continue
    else:
        print("소수가 아닙니다")
        break