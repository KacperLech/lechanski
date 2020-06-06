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

print()

# Użytkownik podaje wartość z klawiatury do momentu wpisania liczby całkowitej
# wykorzystaj pętlę while i wyjątek

while True:
    intTest=input("Wpisz liczbę całkowitą: ")
    try:
        intTest=int(intTest)
        break
    except ValueError:
        pass
    print("Poprawny typ danych")
    finally:
        print('koniec pętli')