def sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print(sum(1, 2, 3))