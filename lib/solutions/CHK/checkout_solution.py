# from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = {}
    for c in skus:
        basket[c] = 1 + basket.get(c, 0)
    
    # {'A': 2, 'B': 2, 'C': 1}

    total = 0
    print(basket)
    for item in basket:
        if item == 'A':
            total += 50 * (basket[item] // 3) + 130 * (basket[item] % 3)
        elif item == 'B':
            total += 30 * (basket[item] // 2) + 45 * (basket[item] % 2)
        elif item == 'C':
            total += 20 * basket[item]
        elif item == 'D':
            total += 15 * basket[item]
        else:
            return -1
    
    return total

print(checkout('AABCD')) # 165
    


