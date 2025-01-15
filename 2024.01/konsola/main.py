def findSex(pesel): return "K" if pesel[9]%2==0 else "M"

def check(pesel):
    numWei = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    S = 0
    for i in range(0, len(pesel)-1): S += pesel[i]*numWei[i]
    M = S%10
    R = 0 if M == 0 else 10 - M
    return True if R == pesel[10] else False

pesel = []
pesel_text = input("Proszę podać pesel: ")
for x in pesel_text: pesel.append(int(x))

print("Płeć:",("Kobieta" if findSex(pesel) == "K" else "Mężczyzna"))
print("Numer PESEL jest",("poprawny." if check(pesel) == True else "niepoprawny.\nSuma kontrolna numeru PESEL jest błędna."))