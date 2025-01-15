import math

#pusta tablica na dane
tab = []

#zakres
n = 100

#wypełniamy tablice True
for x in range(0, n+1):
    tab.append(True)
#ustawiamy liczby 0 i 1 na false, dzięki czemu pierwsza na true będzie 2 co pozwoli na poprawne wykonywanie się kodu
tab[0], tab[1] = False, False

# przechodzimy przez cały zakres od 2 do pierwiastka z n
for i in range(2, int(math.sqrt(n))):
    #pierwsza napotkana liczba która jest ustawiona na true w tym przypadku 2 spowoduje usunięcie wszystkich wielokrotności tej liczby i tak odpowiednio dla każdej następnej (3, 4, 5, ...)
    if tab[i] == True:
        #pętla która przechodzi przez liczby od dwa do n+1 dając nam liczbę wielokrotności
        for j in  range(2, n+1):
            #i czyli liczba bazowa zostaje pomnożona przez mnożnik i daję nam liczbę która na pewno nie będzie liczbą pierwszą a dzięki specyficznej budowie tablicy true/false ta pomnożona wartość jest zarazem naszym indexem
            index = i*j
            #zabezpieczenie przed wyjściem naszej wymnożonej liczby poza index naszej tablicy
            if index > n:
                break
            #przypisanie wartości które wykonuje się jedynie wtedy gdy liczba faktycznie liczbą pierwszą nie jest
            tab[index] = False

#wypisanie tablicy
result = []
i = 0
for x in tab:
    if x == True:
        result.append(i)
    i+=1

print(result)