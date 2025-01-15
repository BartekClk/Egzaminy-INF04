import random

tab = []

def fillTab():
    random.seed()
    while(len(tab)<50):
        tab.append(random.randint(1, 100))

def find(toFind):
    tab.append(toFind)
    i=0
    while(True):
        if tab[i] == toFind:
            tab.pop(-1)
            print(tab)
            if(i!=50):
                print("Znaleziono szukaną liczbę na miejscu w tablicy o indexie:", i)
                break
            else:
                print("Nie znaleziono szukanej liczby.")
                break
        i+=1


fillTab()        
toFind = int(input("Podaj szukaną liczbę: "))
find(toFind)