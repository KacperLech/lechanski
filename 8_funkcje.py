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
def data():
    print('Podaj markę: ', end='')
    marka=input()
    print('Podaj model: ', end='')
    model=input()
    print('Podaj pojemność: ', end='')
    pojemnosc=input()
    print('Podaj prędkość maksymalną: ', end='')
    predkoscMax=input()

    #wpisujemy dane ze zmiennych do słownika
    car={'marka':marka, 'model':model, 'pojemnosc':pojemnosc, 'predkoscMax':predkoscMax}
    #print(car)
    
data()
    
