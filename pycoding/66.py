a = int(input('숫자를 입력하세요: '))

# 홀수만 출력 (1, 3, 5, ..., a까지)
for s in range(1, a + 1, 2):
    # 공백 계산: (a - s) // 2
    spaces = ' ' * ((a - s) // 2)
    print(spaces + '*' * s)