def solution(n, k):
    price_skewer = 12000
    price_drink = 2000
    total_skewer_cost = n * price_skewer
    free_drinks = n // 10
    paid_drinks = max(0, k - free_drinks)
    total_drink_cost = paid_drinks * price_drink
    total_cost = total_skewer_cost + total_drink_cost

    return total_cost