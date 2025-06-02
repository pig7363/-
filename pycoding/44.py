a=input("회문여부를 판별해드립니다: ")

if a[::-1]==a:
    print("회문입니다")
else:
    print("회문이 아닙니다")