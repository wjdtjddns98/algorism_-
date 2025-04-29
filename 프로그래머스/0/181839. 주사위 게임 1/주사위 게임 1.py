def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:  # 둘 다 홀수
        return a**2 + b**2
    elif a % 2 == 1 or b % 2 == 1:  # 하나만 홀수
        return 2 * (a + b)
    else:
        return abs(a - b)
    