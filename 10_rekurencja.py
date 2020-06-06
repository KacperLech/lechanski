#potęgowanie


def potega(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    else:
        return podstawa * potega(podstawa, wykladnik - 1)

print(potega(3, 3))

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