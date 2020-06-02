'''
[] lista
() tuple
{} słownik
'''
progr=['Python', 'PHP', 'C#', 'Java']
print(progr)

#typ listy
print(type(progr))

#pierwszy element
first=progr[0]
print(first)

#pierwsze 3 elementy
threeElements=progr[0:3]
print(threeElements)

#ostatni element
lastElements=progr[-1]
print(lastElements)

#dodanie elementu
progr.append('R')
progr.append('Python')
print(progr)

#zliczanie elementów
countElements=progr.count('Python')
print(countElements)

#liczenie wszystkich elementów
countElementsOfList = len(progr)
print(f'Ilość elementów w liście: {countElementsOfList}')
print('Ilość elementów w liście: ' + str(countElementsOfList) )

#połączenie list
anotherList=['C', 'C++']
progr.extend(anotherList)
print(progr)
print(anotherList)

#usuwanie elementów z listy
new=progr
new.clear()
print(f'Lista progr: {progr}')
print(f'Lista new: {new}')
