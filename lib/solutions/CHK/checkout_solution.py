# from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = {}
    for c in skus:
        basket[c] = 1 + basket.get(c, 0)
    
    if 'E' in basket and basket['E'] >= 2 and 'B' in basket:
        basket['B'] -= basket['E'] // 2
        basket['B'] = max(0, basket['B'])
    
    if 'F' in basket and basket['F'] >= 3:
        basket['F'] -= basket['F'] // 3
    
    if 'U' in basket and basket['U'] >= 4:
        basket['U'] -= basket['U'] // 4
    
    if 'R' in basket and basket['R'] >= 3 and 'Q' in basket:
        basket['Q'] -= basket['R'] // 3
        basket['Q'] = max(0, basket['Q'])
    
    if 'N' in basket and 'M' in basket and basket['N'] >= 3:
        basket['M'] -= basket['N'] // 3
        basket['M'] = max(0, basket['M'])
    
    

    total = 0
    print(basket)
    for item in basket:
        if item == 'A':
            total += 200 * (basket[item] // 5) + 130 * (basket[item] % 5 // 3) + 50 * (basket[item] % 5 % 3)
        elif item == 'B':
            total += 45 * (basket[item] // 2) + 30 * (basket[item] % 2)
        elif item == 'C':
            total += 20 * basket[item]
        elif item == 'D':
            total += 15 * basket[item]
        elif item == 'E':
            total += 40 * basket[item]
        elif item == 'F':
            total += 10 * basket[item]
        elif item == 'G':
            total += 20 * basket[item]
        elif item == 'H':
            total += 80 * (basket[item] // 10) + 45 * (basket[item] % 10 // 5) + 10 * (basket[item] % 5)
        elif item == 'I':
            total += 35 * basket[item]
        elif item == 'J':
            total += 60 * basket[item]
        elif item == 'K':
            total += 150 * (basket[item] // 2) + 80 * (basket[item] % 2)
        elif item == 'L':
            total += 90 * basket[item]
        elif item == 'M':
            total += 15 * basket[item]
        elif item == 'N':
            total += 40 * basket[item]
        elif item == 'O':
            total += 10 * basket[item]
        elif item == 'P':
            total += 200 * (basket[item] // 5) + 50 * (basket[item] % 5)
        elif item == 'Q':
            total += 80 * (basket[item] // 3) + 30 * (basket[item] % 3)
        elif item == 'R':
            total += 50 * basket[item]
        elif item == 'S':
            total += 30 * basket[item]
        elif item == 'T':
            total += 20 * basket[item]
        elif item == 'U':
            total += 40 * basket[item]
        elif item == 'V':
            if basket[item] >= 3:
                total += 130 * (basket[item] // 3)
                basket[item] = basket[item] % 3
            if basket[item] >= 2:
                total += 90 * (basket[item] // 2)
                basket[item] = basket[item] % 2
            total += 50 * basket[item]
        elif item == 'W':
            total += 20 * basket[item]
        elif item == 'X':
            total += 90 * basket[item]
        elif item == 'Y':
            total += 10
        elif item == 'Z':
            total += 50 * basket[item]
        else:
            return -1
    
    return total

print(checkout("HHHHHHHHHHHHHHHH"))  # 120


