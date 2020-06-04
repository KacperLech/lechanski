def  show():
    print('Witaj ', end='')
    print('Janusz')

show()

def iloraz(a, b):
    return a/b

# I sposób wyświetlania
print(iloraz(7, 3))
# II sposób wyświetlania
print(iloraz(b=7, a=3))

'''
Użytkownik podaje z klawiatury:
marka, model, pojemnosc, predkoscMax
utwórz funkcję, która pobierze dane od użytkownika i przypisze do słownika

utwórz drugą funkcję wyświetlająca dane w formacie:
Marka:....
Model:....
Pojemnosc:....
Predkosc maksymalna:....
'''
def give(marka, model, pojemnosc, predkoscMax, car):
    marka=input('Podaj markę: ')
    model=input('Podaj model: ')
    pojemnosc=input('Podaj pojemnosc: ')
    predkoscMax=input('Podaj prędkość maksymalną: ')

    car={'marka':marka, 'model':model, 'pojemnosc':pojemnosc, 'predkoscMax':predkoscMax}
    return marka, model, pojemnosc, predkoscMax, car

def view(car):
    key = 'marka'
    for key, value in car.items():
        print(f'{key}:{value}')


#inicjalizacja zmiennych    
marka=0
model=0    
pojemnosc=0    
predkoscMax=0
car=0
#wywołanie funkcji    
marka, model, pojemnosc, predkoscMax, car = give(marka, model, pojemnosc, predkoscMax, car)
car=view(car)

    
