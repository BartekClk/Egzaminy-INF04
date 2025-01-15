class Class:
    tab = []

    def __init__(self, tab: str):
        self.tab = tab.split(" ")
        for x in range(0, len(self.tab)):
            self.tab[x] = int(self.tab[x])

    def __maximum(self, tab, i):
        max = [tab[i],i]
        for x in range(i, len(tab)):
            if tab[x] > max[0]:
                max[0] = tab[x]
                max[1] = x

        return max[1]
    
    def __minimum(self, tab):
        min = [tab[0],0]
        for x in range(1, len(tab)):
            if tab[x] < min[0]:
                min[0] = tab[x]
                min[1] = x

        return min[1]

    
    def sort(self):
        tab_sort = self.tab.copy()
        min = tab_sort[self.__minimum(tab_sort)]
        i = 0
        while(min!=tab_sort[self.__maximum(tab_sort, i)]):
            max = self.__maximum(tab_sort, i)
            a = tab_sort[i]
            tab_sort[i]=tab_sort[max]
            tab_sort[max]=a
            i+=1

        self.tab = tab_sort.copy()


    def present(self):
        self.sort()
        print("Posortowana tablica: ",self.tab)


print("Podaj 10 liczb całkowitych oddzielając je spacją: ")

a = Class(input())

a.present()