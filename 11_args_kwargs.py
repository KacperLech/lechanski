def sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print(sum(1, 2, 3))

##########################

def dict(**kwargs):
    for name, value in kwargs.items():
        print(f'{name} = {value}')

dict(Imie1 = 'Jan', Imie2 = 'Anna', Imie3 = 'Paweł')