# from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = {}
    for c in skus:
        basket[c] = 1 + basket.get(c, 0)
    
    if 'E' in basket and 'B' in basket:
        if basket['E'] >= 2:
            basket['B'] -= basket['E'] // 2
            basket['B'] = max(0, basket['B'])

    total = 0
    print(basket)
        #     Our price table and offers:
        # +------+-------+------------------------+
        # | Item | Price | Special offers         |
        # +------+-------+------------------------+
        # | A    | 50    | 3A for 130, 5A for 200 |
        # | B    | 30    | 2B for 45              |
        # | C    | 20    |                        |
        # | D    | 15    |                        |
        # | E    | 40    | 2E get one B free      |
        # +------+-------+------------------------+
    for item in basket:
        if item == 'A':
            if basket[item] >= 5:
                total += 200 * (basket[item] // 5) 
                basket[item] = basket[item] % 5
            if basket[item] >= 3:
                total += 130 * (basket[item] // 3)
                basket[item] = basket[item] % 3
            total += 50 * basket[item]
        elif item == 'B':
            total += 45 * (basket[item] // 2) + 30 * (basket[item] % 2)
        elif item == 'C':
            total += 20 * basket[item]
        elif item == 'D':
            total += 15 * basket[item]
        elif item == 'E':
            total += 40 * basket[item]
        else:
            return -1
    
    return total

print(checkout("BBBEE")) 

