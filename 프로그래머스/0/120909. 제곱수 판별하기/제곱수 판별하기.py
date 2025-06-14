def solution(n):
  sqrt_n = n ** 0.5
    
  if sqrt_n.is_integer():
    return 1
  else:
    return 2