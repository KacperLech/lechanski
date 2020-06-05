#try except

def div(x, y):
    try:
        result = x / y
        #return round(result, 2)
        return "{0:.2f}".format(result)
    except ZeroDivisionError:
        print('Nie wolno dzielić przez 0')

print(div(2, 3))
#div(2,0)