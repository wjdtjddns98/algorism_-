def solution(num_str:str) -> int:
    return sum(int(nums) for nums in num_str)

num_str = "123456789"
result = solution(num_str)
print(result)

