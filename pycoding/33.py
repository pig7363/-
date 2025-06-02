a=int(input('숫자를 입력하세요: '))

for s in range(1,a+1,2):
    print(  ' '*(((a-s)//2)) ,'*'*s)