#IMPORTUJEMY BIBLIOTEKĘ 'RANDOM'
import random
#IMPORTUJEMY FUNKCJĘ 'SHUFFLE()'
from random import shuffle

#WPISUJEMY ZAKRES LOSOWANYCH LICZB ORAZ ILOŚĆ LICZB DO LOSOWANIA
a=int(input("Podaj wartość minimalną: "))
b=int(input("Podaj wartość maksymalną: "))
c=int(input("Podaj ilość liczb do wylosowania: "))

#PĘTLA FOR (start, stop, krok):
for i in range (0, c, 1):
    #PRZYPISUJEMY WYLOSOWANĄ LICZBĘ CAŁKOWITĄ Z ZAKRESU DO ZMIENNEJ
    los = random.randrange(a, b, 1)#randrange - losuje liczby całkowite z zakresu 'a->b' ze skokiem co 1
    print("Liczba ",i + 1,": ", los)