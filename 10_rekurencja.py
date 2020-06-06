#potęgowanie


def potegowanie(x, y):
    if y == 1 :
        return x
    else:
        p = potegowanie(x, y-1)
        return x * p


print(potegowanie(3,4))

'''
pow(3, 3) -->
pow(3, 2) -->
pow(3, 1) -->
pow(3, 0) --> 1

pow(3, 0) --> 3 ^ 0 = 1
pow(3, 1) --> 3 * 1 = 3
pow(3, 2) --> 3 * 3 = 9
pow(3, 3) --> 3 * 9 = 27
'''