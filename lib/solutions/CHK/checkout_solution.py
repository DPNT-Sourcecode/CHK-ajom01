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
    for item, qty in basket.items():
        match item:
            case 'A':
                total += 200 * (qty // 5) + 130 * (qty % 5 // 3) + 50 * (qty % 5 % 3)
            case 'B':
                total += 45 * (qty // 2) + 30 * (qty % 2)
            case 'C':
                total += 20 * qty
            case 'D':
                total += 15 * qty
            case 'E' | 'U' | 'N':
                total += 40 * qty
            case 'F':
                total += 10 * qty
            case 'G':
                total += 20 * qty
            case 'H':
                total += 80 * (qty // 10) + 45 * (qty % 10 // 5) + 10 * (qty % 5)
            case 'I':
                total += 35 * qty
            case 'J':
                total += 60 * qty
            case 'K':
                total += 150 * (qty // 2) + 80 * (qty % 2)
            case 'L':
                total += 90 * qty
            case 'M':
                total += 15 * qty
            case 'O':
                total += 10 * qty
            case 'P':
                total += 200 * (qty // 5) + 50 * (qty % 5)
            case 'Q':
                total += 80 * (qty // 3) + 30 * (qty % 3)
            case 'R':
                total += 50 * qty
            case 'S':
                total += 30 * qty
            case 'T':
                total += 20 * qty
            case 'V':
                total += 130 * (qty // 3) + 90 * (qty % 3 // 2) + 50 * (qty % 3 % 2)
            case 'W':
                total += 20 * qty
            case 'X':
                total += 90 * qty
            case 'Y':
                total += 10 * qty
            case 'Z':
                total += 50 * qty
            case _:
                return -1
    
    return total

print(checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'))
print(checkout('LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH'))



