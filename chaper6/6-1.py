def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 10000부터 1까지 역순으로 소수 체크
for num in range(19870000000014214, 1, -1):
    if is_prime(num):
        print(f"10000 이하의 가장 큰 소수는 {num}입니다.")
        break