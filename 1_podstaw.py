print("cdv")
print (2)
print ('test')

#potęga
pow=2**10
print(pow)

text="CDV"
print(text * 2)

#pobieranie danych z klawiatury
name=input()
print(name)
print("Twoje imię:"+name)
surname=input("Podaj swoje nazwisko: ")
print("Imie: " + name + ", nazwisko: " + surname)

lengthSurname=len(surname) #<class 'str'>
print(type(surname)) #<class 'int'>
print(type(lengthSurname))
lengthSurname = str(lengthSurname)  #rzutowanie

print("Długość nazwiska: " + lengthSurname)

'''
Użytkownik podaje z klawiatury
imiona i nazwiska oraz wiek
wyświetl w formacie:
Imię i nazwisko:.........., wiek:.....
'''

print("ZADANIE")

imie=input("Podaj imie: ")
nazwisko=input("Podaj nazwisko: ")
wiek=input("Podaj wiek: ")
print("Imię i nazwisko: " + imie + " " + nazwisko + ", wiek: " + wiek)

print("\nPodaj swój wiek: ", end="")
age=input()

surname="Kowalski"
firstLetter=surname[0]
print(firstLetter)
lastLetter = surname[len(surname) - 1 ]
print(lastLetter)


#konwersja
x="5"
print(type(x)) #str
x=int(x)
print(type(x)) #int

y=5
print(type(y))

#y = y / 2
y /= 2 #y=y / 2
print(type(y)) #float
print(y)

surname="Kowalski"
print(surname[0]) #K
print(surname[0:3]) #Kow
print(surname[-2]) #k
print(surname[-2:]) #ki
print(surname[:]) #Kowalski
print(surname[:-2]) #Kowals
print(surname[:-2:2]) #kwl

