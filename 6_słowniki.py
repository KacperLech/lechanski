dict={'key1':'value1','key2':'value2'}
'''
Utwórz słownik o nazwie pracownik zawierający klucze:
imie, nazwisko, miasto, wiek, imionaDzieci (podaj dwa imiona - za pomocą listy), imionaRodzicow(podaj dwa imiona rodzicow - za pomocą listy)
Proszę pojedynczo wyświetlić imiona dzieci:
Dziecko 1: ....
Dziecko 2: ....
'''
worker = {
    'firstName':'Kacper',
    'lastName':'Lechański',
    'city':'Poznań',
    'age':'23',
    'namesChildren':['Marcin', 'Ania'],
    'namesParent':['Edyta', 'Dariusz']
}
print(worker)
print(worker['namesChildren'])
print('Dziecko 1: ' + worker['namesChildren'][0])
print('Dziecko 2: ' + worker['namesChildren'][1])