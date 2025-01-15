# Podręcznik Python - Kompletny Przewodnik (Rozbudowany)

## Spis Treści

1.  [Wprowadzenie](#wprowadzenie)
    *   [1.1. Czym jest Python?](#11-czym-jest-python)
        *   [Definicja, zastosowania i korzyści](#definicja-zastosowania-i-korzysci)
    *   [1.2. Konfiguracja środowiska](#12-konfiguracja-srodowiska)
        *   [1.2.1. Instalacja Pythona](#121-instalacja-pythona)
        *   [1.2.2. Środowiska wirtualne](#122-srodowiska-wirtualne)
    *   [1.3. Pierwszy program](#13-pierwszy-program)
2.  [Podstawy języka](#podstawy-jezyka)
    *   [2.1. Typy danych](#21-typy-danych)
        *   [2.1.1. Liczby (int, float, complex)](#211-liczby-int-float-complex)
        *   [2.1.2. Łańcuchy znaków (string)](#212-lancuchy-znakow-string)
        *   [2.1.3. Listy (list)](#213-listy-list)
        *   [2.1.4. Krotki (tuple)](#214-krotki-tuple)
        *   [2.1.5. Słowniki (dict)](#215-slowniki-dict)
        *   [2.1.6. Zbiory (set)](#216-zbiory-set)
        *   [2.1.7. Wartości logiczne (bool)](#217-wartosci-logiczne-bool)
    *   [2.2. Operatory](#22-operatory)
        *   [2.2.1. Arytmetyczne](#221-arytmetyczne)
        *   [2.2.2. Porównania](#222-porownania)
        *   [2.2.3. Logiczne](#223-logiczne)
        *   [2.2.4. Przypisania](#224-przypisania)
            *   [2.2.4.1. Złożone operatory przypisania](#2241-zlozone-operatory-przypisania)
        *   [2.2.5. Bitowe](#225-bitowe)
        *   [2.2.6. Tożsamościowe](#226-tozsamosciowe)
        *   [2.2.7. Przynależnościowe](#227-przynaleznosciowe)
    *   [2.3. Zmienne](#23-zmienne)
        *   [2.3.1. Adnotacje typów](#231-adnotacje-typow)
    *   [2.4. Komentarze](#24-komentarze)
    *   [2.5. Instrukcje warunkowe](#25-instrukcje-warunkowe)
        *   [2.5.1. if, elif, else](#251-if-elif-else)
    *   [2.6. Pętle](#26-petle)
        *   [2.6.1. for](#261-for)
             * [2.6.1.1. Pętla for ze skokiem](#2611-petla-for-ze-skokiem)
        *   [2.6.2. while](#262-while)
    *   [2.7. Funkcje](#27-funkcje)
        *    [2.7.1. Definiowanie funkcji](#271-definiowanie-funkcji)
        *    [2.7.2. Argumenty funkcji](#272-argumenty-funkcji)
        *    [2.7.3. Wartość zwrotna](#273-wartosc-zwrotna)
             *    [2.7.3.1. Adnotacje typów zwracanych](#2731-adnotacje-typow-zwracanych)
        *    [2.7.4. Funkcje lambda](#274-funkcje-lambda)
    *   [2.8. Moduły](#28-moduly)
      *   [2.8.1. Importowanie modułów](#281-importowanie-modulow)
      *   [2.8.2. Własne moduły](#282-wlasne-moduly)
    *   [2.9. Obsługa błędów i wyjątków](#29-obsluga-bledow-i-wyjatkow)
        *   [2.9.1. try, except, finally](#291-try-except-finally)
3.  [Zaawansowane koncepcje](#zaawansowane-koncepcje)
    *   [3.1. Programowanie obiektowe (OOP)](#31-programowanie-obiektowe-oop)
        *   [3.1.1. Klasy i obiekty](#311-klasy-i-obiekty)
        *   [3.1.2. Dziedziczenie](#312-dziedziczenie)
        *   [3.1.3. Polimorfizm](#313-polimorfizm)
        *   [3.1.4. Hermetyzacja](#314-hermetyzacja)
            * [3.1.4.1. Public, protected, private](#3141-public-protected-private)
        *   [3.1.5. Metody i zmienne statyczne](#315-metody-i-zmienne-statyczne)
    *   [3.2. Iteratory i generatory](#32-iteratory-i-generatory)
    *   [3.3. Dekoratory](#33-dekoratory)
    *   [3.4. Kontekst managery](#34-kontekst-managery)
        *   [3.4.1. with](#341-with)
    *   [3.5. Praca z plikami](#35-praca-z-plikami)
        *  [3.5.1. Odczyt plików](#351-odczyt-plików)
            *   [3.5.1.1. Odczyt całego pliku](#3511-odczyt-całego-pliku)
            *   [3.5.1.2. Iteracja po liniach pliku](#3512-iteracja-po-liniach-pliku)
            *   [3.5.1.3. Wczytywanie danych do klasy](#3513-wczytywanie-danych-do-klasy)
        * [3.5.2. Zapis plików](#352-zapis-plików)
            *   [3.5.2.1. Zapis pojedynczego stringa](#3521-zapis-pojedynczego-stringa)
            *   [3.5.2.2. Zapis wielu linii](#3522-zapis-wielu-linii)
            *   [3.5.2.3. Zapis obiektów klasy](#3523-zapis-obiektów-klasy)
            *   [3.5.2.4. Dopisywanie do pliku](#3524-dopisywanie-do-pliku)
        *  [3.5.3. Dodatkowe Operacje](#353-dodatkowe-operacje)
            *   [3.5.3.1. Sprawdzanie istnienia pliku](#3531-sprawdzanie-istnienia-pliku)
            *   [3.5.3.2. Usuwanie i zmiana nazw plików](#3532-usuwanie-i-zmiana-nazw-plików)
    *   [3.6. Wyrażenia regularne](#36-wyrazenia-regularne)
        *   [3.6.1. Moduł `re`](#361-modul-re)
    *   [3.7. Moduł `json`](#37-modul-json)
    *   [3.8. Obsługa dat i czasu](#38-obsluga-dat-i-czasu)
        *   [3.8.1. Moduł `datetime`](#381-modul-datetime)
    *  [3.9. Moduł `abc`](#39-modul-abc)
         * [3.9.1. Klasy abstrakcyjne](#391-klasy-abstrakcyjne)
4.  [Praca z danymi](#praca-z-danymi)
    *   [4.1. Moduł `csv`](#41-modul-csv)
    *   [4.2. `NumPy` - Obliczenia numeryczne](#42-numpy---obliczenia-numeryczne)
        *   [4.2.1. Tablice `NumPy`](#421-tablice-numpy)
        *   [4.2.2. Operacje na tablicach](#422-operacje-na-tablicach)
    *   [4.3. `Pandas` - Analiza danych](#43-pandas---analiza-danych)
        *   [4.3.1. `DataFrame`](#431-dataframe)
            * [4.3.1.1. Tworzenie DataFrame](#4311-tworzenie-dataframe)
            * [4.3.1.2. Podstawowe informacje o DataFrame](#4312-podstawowe-informacje-o-dataframe)
        *    [4.3.2. Manipulacja danymi](#432-manipulacja-danymi)
         *    [4.3.2.1. Wybieranie kolumn i wierszy](#4321-wybieranie-kolumn-i-wierszy)
         *    [4.3.2.2. Filtrowanie danych](#4322-filtrowanie-danych)
         *    [4.3.2.3. Sortowanie danych](#4323-sortowanie-danych)
         *    [4.3.2.4. Dodawanie i usuwanie kolumn](#4324-dodawanie-i-usuwanie-kolumn)
         *    [4.3.2.5. Grupowanie danych](#4325-grupowanie-danych)
         *    [4.3.2.6. Agregacje danych](#4326-agregacje-danych)
         *    [4.3.2.7. Łączenie DataFrame](#4327-laczenie-dataframe)
         *    [4.3.2.8. Praca z brakującymi danymi](#4328-praca-z-brakujacymi-danymi)
         *    [4.3.2.9. Zapis i odczyt danych](#4329-zapis-i-odczyt-danych)
5.  [Programowanie współbieżne](#programowanie-wspolbiezne)
    *   [5.1. Wątki](#51-watki)
        *   [5.1.1. Moduł `threading`](#511-modul-threading)
    *   [5.2. Procesy](#52-procesy)
        *   [5.2.1. Moduł `multiprocessing`](#521-modul-multiprocessing)
    *   [5.3. Asynchroniczność](#53-asynchronicznosc)
        *   [5.3.1. `asyncio` i `async`/`await`](#531-asyncio-i-asyncawait)
6.  [Wybrane biblioteki i frameworki](#wybrane-biblioteki-i-frameworki)
    *   [6.1. `Requests` - Obsługa HTTP](#61-requests---obsluga-http)
    *   [6.2. `Beautiful Soup` - Web scraping](#62-beautiful-soup---web-scraping)
    *   [6.3. `Flask` - Mikroframework webowy](#63-flask---mikroframework-webowy)
    *   [6.4. `Django` - Framework webowy](#64-django---framework-webowy)
    *   [6.5. `PyTest` - Testy jednostkowe](#65-pytest---testy-jednostkowe)
        *   [6.5.1. Podstawy `PyTest`](#651-podstawy-pytest)
        *   [6.5.2. Pisanie testów](#652-pisanie-testow)
        *   [6.5.3. Uruchamianie testów](#653-uruchamianie-testow)
        *   [6.5.4.  Fixtures](#654--fixtures)
        *   [6.5.5. Markery](#655-markery)
7.  [Dobre praktyki](#dobre-praktyki)
    *   [7.1. Styl kodu PEP 8](#71-styl-kodu-pep-8)
    *   [7.2. Testowanie kodu](#72-testowanie-kodu)
    *   [7.3. Dokumentacja kodu](#73-dokumentacja-kodu)

## Wprowadzenie

### 1.1. Czym jest Python?

Python to wszechstronny, interpretowany język programowania wysokiego poziomu, znany ze swojej czytelnej składni i wszechstronności.

#### Definicja, zastosowania i korzyści
**Zastosowania:**
* Web development (backend, API).
* Data science i analiza danych.
* Sztuczna inteligencja i uczenie maszynowe.
* Automatyzacja zadań i skrypty.
* Aplikacje desktopowe.
* Gry.
* Testowanie oprogramowania.

**Korzyści:**
*   Czytelność: Składnia jest intuicyjna, co ułatwia naukę i czytanie kodu.
*   Wszechstronność: Szeroki zakres zastosowań.
*   Duża biblioteka standardowa: Bogactwo modułów i narzędzi.
*   Aktywna społeczność: Duża społeczność i wsparcie.
*   Wieloplatformowość: Działa na różnych systemach operacyjnych.
*   Szybki rozwój: Idealny do szybkiego prototypowania.

### 1.2. Konfiguracja środowiska

#### 1.2.1. Instalacja Pythona
Python można pobrać ze strony python.org. Upewnij się, że pobierasz wersję odpowiednią dla Twojego systemu operacyjnego. Podczas instalacji zaznacz opcję "Add Python to PATH", aby móc korzystać z Pythona z poziomu terminala.

#### 1.2.2. Środowiska wirtualne
Środowiska wirtualne pomagają izolować zależności projektów, unikając konfliktów. Do ich tworzenia można wykorzystać `venv`:

```bash
python -m venv nazwa_srodowiska
```
Aktywacja środowiska:

**Linux/macOS:**
```bash
source nazwa_srodowiska/bin/activate
```
**Windows:**
```bash
nazwa_srodowiska\Scripts\activate
```
### 1.3. Pierwszy program

Stwórz plik `hello.py` i wpisz w nim:

```python
print("Witaj, Pythonie!")
```
Uruchom program z terminala:

```bash
python hello.py
```
## Podstawy języka

### 2.1. Typy danych

Python oferuje szeroki wachlarz wbudowanych typów danych.

#### 2.1.1. Liczby (int, float, complex)

```python
x: int = 10
y: float = 3.14
z: complex = 2 + 3j
```

#### 2.1.2. Łańcuchy znaków (string)

```python
name: str = "Python"
message: str = 'Witaj!'
long_message: str = """To jest
wieloliniowy
łańcuch."""
```

#### 2.1.3. Listy (list)

```python
numbers: list[int] = [1, 2, 3, 4]
names: list[str] = ["Anna", "Jan", "Piotr"]
mixed: list[any] = [1, "tekst", 3.14]
```

#### 2.1.4. Krotki (tuple)

```python
point: tuple[int, int] = (10, 20)
colors: tuple[str, str, str] = ("red", "green", "blue")
```

#### 2.1.5. Słowniki (dict)

```python
person: dict[str, any] = {"name": "Jan", "age": 30, "city": "Warszawa"}
```

#### 2.1.6. Zbiory (set)

```python
unique_numbers: set[int] = {1, 2, 3, 1, 2}  # {1, 2, 3}
```

#### 2.1.7. Wartości logiczne (bool)

```python
is_true: bool = True
is_false: bool = False
```

### 2.2. Operatory
#### 2.2.1. Arytmetyczne
`+, -, *, /, %, **, //`

#### 2.2.2. Porównania
`==, !=, >, <, >=, <=`

#### 2.2.3. Logiczne
`and, or, not`

#### 2.2.4. Przypisania
`=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=`

##### 2.2.4.1. Złożone operatory przypisania
Są to skróty dla częstych operacji przypisania, na przykład `x += 5` jest równoważne `x = x + 5`.

```python
x: int = 10
x += 5  # x = x + 5  -> x wynosi teraz 15
x -= 3  # x = x - 3 -> x wynosi teraz 12
x *= 2  # x = x * 2  -> x wynosi teraz 24
x /= 4  # x = x / 4 -> x wynosi teraz 6.0
x //= 2 # x = x // 2 -> x wynosi teraz 3.0
x **= 3 # x = x ** 3 -> x wynosi teraz 27.0
x %= 10 # x = x % 10 -> x wynosi teraz 7.0
```

#### 2.2.5. Bitowe
`&, |, ^, ~, <<, >>`

#### 2.2.6. Tożsamościowe
`is, is not`

#### 2.2.7. Przynależnościowe
`in, not in`

### 2.3. Zmienne
Zmienne przechowują dane.

```python
x: int = 10
name: str = "Python"
```

#### 2.3.1. Adnotacje typów
Python pozwala na dodawanie adnotacji typów do zmiennych, co zwiększa czytelność i pomaga w wykrywaniu błędów.

```python
x: int = 10
name: str = "Python"
price: float = 99.99
numbers: list[int] = [1, 2, 3]
```

### 2.4. Komentarze
Komentarze są ignorowane przez interpreter.

```python
# To jest komentarz jednoliniowy

"""
To jest komentarz
wieloliniowy
"""
```

### 2.5. Instrukcje warunkowe
#### 2.5.1. if, elif, else

```python
age: int = 20

if age >= 18:
    print("Jesteś pełnoletni")
elif age >= 13:
    print("Jesteś nastolatkiem")
else:
    print("Jesteś dzieckiem")
```

### 2.6. Pętle
#### 2.6.1. for

```python
for i in range(5):
    print(i)

names: list[str] = ["Anna", "Jan", "Piotr"]
for name in names:
    print(name)
```

##### 2.6.1.1. Pętla for ze skokiem
Pętla for może iterować z krokiem innym niż 1 przy użyciu funkcji `range` z trzecim argumentem.

```python
for i in range(0, 20, 5):
  print(i)  # Wyświetli 0, 5, 10, 15
```

#### 2.6.2. while

```python
count: int = 0
while count < 5:
    print(count)
    count += 1
```

### 2.7. Funkcje
#### 2.7.1. Definiowanie funkcji

```python
def greet(name: str) -> None:
    print(f"Witaj, {name}!")
```
#### 2.7.2. Argumenty funkcji
```python
greet("Jan") #Argument pozycyjny
greet(name="Anna") #Argument nazwany
```

#### 2.7.3. Wartość zwrotna

```python
def add(x: int, y: int) -> int:
    return x + y

result: int = add(5, 3)
print(result)
```

##### 2.7.3.1. Adnotacje typów zwracanych
Python pozwala na definiowanie typu zwracanego przez funkcję.

```python
def add(x: int, y: int) -> int:
    return x + y

def greet(name: str) -> str:
  return f"Witaj, {name}!"
```

#### 2.7.4. Funkcje lambda
Anonimowe funkcje.

```python
double = lambda x: x * 2
print(double(5))
```

### 2.8. Moduły
#### 2.8.1. Importowanie modułów

```python
import math
print(math.sqrt(16))

from datetime import date
print(date.today())
```

#### 2.8.2. Własne moduły
Stwórz plik `my_module.py` z definicją np. funkcji. Następnie zaimportuj ten moduł z innego pliku.

### 2.9. Obsługa błędów i wyjątków
#### 2.9.1. try, except, finally

```python
try:
  x: float = 1 / 0
except ZeroDivisionError:
    print("Dzielenie przez zero!")
finally:
    print("To wykona się zawsze")
```

## Zaawansowane koncepcje

### 3.1. Programowanie obiektowe (OOP)
#### 3.1.1. Klasy i obiekty

```python
class Dog:
    def __init__(self, name: str, breed: str) -> None:
        self.name: str = name
        self.breed: str = breed

    def bark(self) -> None:
        print("Woof!")

my_dog: Dog = Dog("Rex", "Labrador")
my_dog.bark()
```

#### 3.1.2. Dziedziczenie

```python
class Cat(Dog):
  def meow(self) -> None:
        print("Meow!")

my_cat: Cat = Cat("Mruczek", "Pers")
my_cat.meow()
```

#### 3.1.3. Polimorfizm

```python
import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self) -> None:
      pass
class Dog(Animal):
     def make_sound(self) -> None:
        print("Woof")

class Cat(Animal):
    def make_sound(self) -> None:
        print("Meow")

def make_sound(animal: Animal) -> None:
    animal.make_sound()

my_dog = Dog()
my_cat = Cat()

make_sound(my_dog) #wywoła bark
make_sound(my_cat) #wywoła meow
```

#### 3.1.4. Hermetyzacja
Mechanizm ukrywania szczegółów implementacyjnych klasy i udostępniania kontrolowanego dostępu do jej danych.

##### 3.1.4.1. Public, protected, private

*   **Public:** Atrybuty i metody są dostępne z dowolnego miejsca (domyślnie).
*   **Protected:** Atrybuty i metody są przeznaczone do użytku w klasie i jej podklasach (konwencja `_nazwa`).
*   **Private:** Atrybuty i metody są przeznaczone do użytku tylko w obrębie klasy (konwencja `__nazwa`).
```python
class Car:
    def __init__(self, model: str, color: str, speed: int) -> None:
       self.model: str = model #atrybut publiczny
       self._color: str = color  # atrybut protected
       self.__speed: int = speed # atrybut private

    def get_speed(self) -> int: #metoda publiczna do dostępu do atrybutu private
         return self.__speed

    def _increase_speed(self, value: int) -> None: #metoda protected
        self.__speed += value
```
#### 3.1.5. Metody i zmienne statyczne

*   **Metody statyczne:** Nie mają dostępu do instancji klasy (`self`), są związane z klasą, a nie obiektami. Deklarowane za pomocą dekoratora `@staticmethod`.
*   **Zmienne statyczne:** Są współdzielone przez wszystkie instancje klasy, deklarowane poza metodami, ale w obrębie klasy.
```python
class MathUtils:
    PI: float = 3.14159  # Zmienna statyczna

    @staticmethod
    def calculate_area(radius: float) -> float: #Metoda statyczna
      return MathUtils.PI * radius * radius
```

### 3.2. Iteratory i generatory
Umożliwiają sekwencyjne przechodzenie po elementach zbioru.

### 3.3. Dekoratory
Modyfikują zachowanie funkcji.

### 3.4. Kontekst managery
#### 3.4.1. with
Zapewniają odpowiednie zamknięcie zasobów.

```python
with open("file.txt", 'r') as file:
    data: str = file.read()
```


### 3.5. Praca z plikami

#### 3.5.1. Odczyt plików

##### 3.5.1.1. Odczyt całego pliku

```python
with open("file.txt", 'r') as file:
    data: str = file.read()
    print(data)
```
Ten kod otworzy plik "file.txt" wtrybie odczytu ('r'), odczyta całą zawartość do zmiennej `data` i wypisze ją na konsolę. Użycie `with` automatycznie zamknie plik po zakończeniu bloku kodu.

##### 3.5.1.2. Iteracja po liniach pliku

Często potrzebujemy przetwarzać plik linijka po linijce. Możemy to zrobić, iterując po obiekcie pliku:

```python
with open("file.txt", 'r') as file:
    for line in file:
        # Usuwanie znaku nowej linii na końcu każdej linii
        line = line.strip()
        print(f"Linia: {line}")
```
W tym przykładzie, każda linijka z pliku jest przypisywana do zmiennej `line` w pętli `for`. Funkcja `strip()` usuwa białe znaki z początku i końca linii, w tym znak nowej linii `\n`.

##### 3.5.1.3. Wczytywanie danych do klasy

Załóżmy, że mamy klasę `Person` z pięcioma atrybutami:

```python
class Person:
    def __init__(self, name, surname, age, city, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.profession = profession

    def __str__(self):
        return f"Imię: {self.name}, Nazwisko: {self.surname}, Wiek: {self.age}, Miasto: {self.city}, Zawód: {self.profession}"
```

Chcemy teraz wczytać dane o osobach z pliku, gdzie każda osoba zajmuje 5 kolejnych linijek w pliku:

```python
def load_people_from_file(filename):
    people = []
    with open(filename, 'r') as file:
        while True:
            name = file.readline().strip()
            if not name:  # Jeśli napotkamy pustą linię to koniec pliku lub koniec osoby
                break
            surname = file.readline().strip()
            age = file.readline().strip()
            city = file.readline().strip()
            profession = file.readline().strip()

            person = Person(name, surname, int(age), city, profession)
            people.append(person)
    return people

# Przykład użycia:
people_list = load_people_from_file("people.txt")
for person in people_list:
    print(person)
```
Ten kod wczytuje dane z pliku "people.txt", tworzy obiekty `Person` i dodaje je do listy `people`. Plik `people.txt` powinien mieć następującą strukturę:

```
Jan
Kowalski
30
Warszawa
Programista
Anna
Nowak
25
Kraków
Lekarz
...
```

---

#### 3.5.2. Zapis plików

##### 3.5.2.1. Zapis pojedynczego stringa

```python
with open("output.txt", 'w') as file:
    file.write("Hello, world!\n")
```

Ten kod otworzy plik "output.txt" w trybie zapisu ('w'). Jeśli plik nie istnieje, zostanie utworzony. Jeśli istnieje, jego zawartość zostanie nadpisana.  Zapisany string to "Hello, world!" i znak nowej linii.

##### 3.5.2.2. Zapis wielu linii

Możemy zapisywać wiele linii do pliku, używając pętli:

```python
lines = ["Pierwsza linia", "Druga linia", "Trzecia linia"]
with open("output.txt", 'w') as file:
    for line in lines:
        file.write(line + "\n")
```

Ten kod zapisze trzy linie tekstu do pliku "output.txt". Każda linia będzie zakończona znakiem nowej linii `\n`.

##### 3.5.2.3. Zapis obiektów klasy
Możemy zapisać dane z obiektów klasy do pliku. Używając wcześniej zdefiniowanej klasy `Person` :

```python
def save_people_to_file(filename, people):
    with open(filename, 'w') as file:
        for person in people:
           file.write(person.name + "\n")
           file.write(person.surname + "\n")
           file.write(str(person.age) + "\n")
           file.write(person.city + "\n")
           file.write(person.profession + "\n")


people_list = [Person("Jan", "Kowalski", 30, "Warszawa", "Programista"),
               Person("Anna", "Nowak", 25, "Kraków", "Lekarz")]

save_people_to_file("output_people.txt", people_list)
```

Ten kod zapisuje dane z listy obiektów `Person` do pliku "output_people.txt" w formacie, który można później odczytać funkcją `load_people_from_file`.

##### 3.5.2.4. Dopisywanie do pliku

Jeśli chcemy dopisać dane do istniejącego pliku bez nadpisywania jego zawartości, użyjemy trybu 'a' (append):

```python
with open("output.txt", 'a') as file:
    file.write("Dodana linia na końcu.\n")
```
Ten kod dopisze nową linię na końcu pliku "output.txt"

#### 3.5.3. Dodatkowe operacje

##### 3.5.3.1. Sprawdzanie istnienia pliku

Przed wykonaniem operacji na pliku warto sprawdzić czy on istnieje:
```python
import os

if os.path.exists("file.txt"):
    print("Plik istnieje.")
else:
    print("Plik nie istnieje.")
```

##### 3.5.3.2. Usuwanie i zmiana nazw plików

Możemy usuwać i zmieniać nazwy plików używając biblioteki `os`:

```python
import os

# Zmiana nazwy pliku
os.rename("old_file.txt", "new_file.txt")

# Usuwanie pliku
os.remove("file_to_delete.txt")
```


### 3.6. Wyrażenia regularne
#### 3.6.1. Moduł `re`
Do zaawansowanego wyszukiwania i manipulacji tekstem.

### 3.7. Moduł `json`
Służy do kodowania i dekodowania JSON.

### 3.8. Obsługa dat i czasu
#### 3.8.1. Moduł `datetime`
Do operacji na datach i czasach.

### 3.9. Moduł `abc`
Moduł `abc` (Abstract Base Classes) w Pythonie służy do tworzenia klas abstrakcyjnych. Klasy abstrakcyjne są klasami, których nie można instancjonować. Służą one jako szablony dla innych klas, definiując wspólny interfejs.

#### 3.9.1. Klasy abstrakcyjne

Klasę abstrakcyjną definiuje się przy użyciu `abc.ABC` oraz abstrakcyjne metody przy pomocy dekoratora `@abc.abstractmethod`. Podklasa klasy abstrakcyjnej musi zaimplementować wszystkie jej abstrakcyjne metody.

```python
import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius**2

class Rectangle(Shape):
     def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height

     def calculate_area(self) -> float:
        return self.width * self.height

# shape = Shape()  # Błąd: nie można utworzyć instancji klasy abstrakcyjnej
circle: Circle = Circle(5)
rectangle: Rectangle = Rectangle(4, 6)

print(f"Pole koła: {circle.calculate_area()}")
print(f"Pole prostokąta: {rectangle.calculate_area()}")
```

## Praca z danymi
### 4.1. Moduł `csv`
Do odczytu i zapisu plików CSV.

### 4.2. `NumPy` - Obliczenia numeryczne
#### 4.2.1. Tablice `NumPy`

```python
import numpy as np

arr: np.ndarray = np.array([1, 2, 3])
```

#### 4.2.2. Operacje na tablicach
Operacje matematyczne i manipulacje danymi.

### 4.3. `Pandas` - Analiza danych

Pandas to potężna biblioteka do analizy danych, oferująca struktury danych `DataFrame` i `Series`.

#### 4.3.1. `DataFrame`

`DataFrame` to struktura danych przypominająca tabelę, składająca się z wierszy i kolumn.

##### 4.3.1.1. Tworzenie `DataFrame`

```python
import pandas as pd
data: dict[str, list[any]] = {'name': ['Anna', 'Jan', 'Piotr'],
        'age': [25, 30, 28],
        'city': ['Warszawa', 'Kraków', 'Gdańsk']}
df: pd.DataFrame = pd.DataFrame(data)
print(df)
```

##### 4.3.1.2. Podstawowe informacje o `DataFrame`

```python
print(df.head())    # wyświetla kilka pierwszych wierszy
print(df.tail())    # wyświetla kilka ostatnich wierszy
print(df.info())    # wyświetla informacje o typach kolumn, ilości niepustych danych itp
print(df.describe()) # wyświetla statystyki dla kolumn numerycznych
```

#### 4.3.2. Manipulacja danymi

Pandas oferuje szeroką gamę metod do manipulacji danymi.
##### 4.3.2.1. Wybieranie kolumn i wierszy

```python
print(df['name'])        # wybierz kolumnę name
print(df[['name', 'age']]) # wybierz kolumny name i age
print(df.loc[0])         # wybierz wiersz o indeksie 0
print(df.loc[0:2])       # wybierz wiersze o indeksach od 0 do 2
```

##### 4.3.2.2. Filtrowanie danych

```python
print(df[df['age'] > 25]) #wybierz wiersze gdzie wiek jest większy niż 25
print(df[(df['age'] > 25) & (df['city'] == "Kraków")])#wybierz wiersze gdzie wiek jest większy niż 25 i miasto to Kraków
```

##### 4.3.2.3. Sortowanie danych

```python
print(df.sort_values(by='age')) #sortuj wiersze według wieku
print(df.sort_values(by='age', ascending=False)) #sortuj wiersze według wieku malejąco
```

##### 4.3.2.4. Dodawanie i usuwanie kolumn

```python
df['is_adult'] = df['age'] >= 18  #dodanie nowej kolumny
df.drop(columns=['is_adult'], inplace=True) #usuwanie kolumny
```

##### 4.3.2.5. Grupowanie danych

```python
grouped: pd.core.groupby.generic.DataFrameGroupBy = df.groupby('city') #grupuj dane po kolumnie city
print(grouped.size()) # wyświetl ilość w każdej grupie
```

##### 4.3.2.6. Agregacje danych

```python
print(df.groupby('city')['age'].mean()) # obliczenie średniego wieku dla każdej grupy
```

##### 4.3.2.7. Łączenie `DataFrame`

```python
data2: dict[str, list[str]] = {'city': ['Warszawa', 'Kraków', 'Poznań'],
          'country':['Polska', 'Polska', 'Polska']}

df2: pd.DataFrame = pd.DataFrame(data2)

merged_df: pd.DataFrame = pd.merge(df, df2, on="city", how="left") #łącz dane po kolumnie city
print(merged_df)
```

##### 4.3.2.8. Praca z brakującymi danymi

```python
df = df.fillna(0) # wypełnienie brakujących danych wartością 0
df = df.dropna() #usuwanie wierszy z brakującymi danymi
```

##### 4.3.2.9. Zapis i odczyt danych

```python
df.to_csv('data.csv', index=False) # zapisywanie do csv
df_from_csv: pd.DataFrame = pd.read_csv('data.csv') # odczyt danych z csv
```

## Programowanie współbieżne
### 5.1. Wątki
#### 5.1.1. Moduł `threading`
Do uruchamiania kodu w osobnych wątkach.

### 5.2. Procesy
#### 5.2.1. Moduł `multiprocessing`
Do uruchamiania kodu w osobnych procesach.

### 5.3. Asynchroniczność
#### 5.3.1. `asyncio` i `async`/`await`
Do programowania asynchronicznego.

## Wybrane biblioteki i frameworki
### 6.1. `Requests` - Obsługa HTTP
Ułatwia wysyłanie zapytań HTTP.

### 6.2. `Beautiful Soup` - Web scraping
Do parsowania stron HTML.

### 6.3. `Flask` - Mikroframework webowy
Do budowy prostych aplikacji webowych.

### 6.4. `Django` - Framework webowy
Do budowy bardziej zaawansowanych aplikacji.

### 6.5. `PyTest` - Testy jednostkowe
PyTest to rozbudowany framework do testowania kodu w Pythonie.

#### 6.5.1. Podstawy `PyTest`

*   Automatyczne wykrywanie testów.
*   Fixtures – definiowanie środowiska testowego.
*   Markery – tagowanie testów.
*   Szerokie możliwości konfiguracji.

#### 6.5.2. Pisanie testów
Testy piszemy w plikach zaczynających się od `test_` lub kończących się na `_test.py`. Funkcje testowe powinny zaczynać się od słowa `test_`.

```python
# test_utils.py
from typing import List

def add(a: int, b: int) -> int:
    return a + b

def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

#### 6.5.3. Uruchamianie testów
Testy uruchamiamy z terminala komendą `pytest`.

```bash
pytest
```

#### 6.5.4. Fixtures
Fixtures pozwalają na tworzenie powtarzalnych elementów testowego środowiska.

```python
import pytest
from typing import List

@pytest.fixture
def sample_list() -> List[int]:
    return [1, 2, 3]

def test_list_sum(sample_list: List[int]) -> None:
    assert sum(sample_list) == 6
```

#### 6.5.5. Markery
Markery pozwalają tagować testy, na przykład testy powolne.

```python
import pytest
@pytest.mark.slow
def test_slow_operation() -> None:
     # test slow
    pass
```

## Dobre praktyki
### 7.1. Styl kodu PEP 8
Zalecenia stylu kodowania Pythona.

*   Używaj 4 spacji dla wcięć.
*   Nazwy zmiennych i funkcji pisz małymi literami z podkreśleniami (`snake_case`).
*   Nazwy klas pisz `CamelCase`.
*   Używaj krótkich, ale opisowych nazw.
*   Długość linii nie powinna przekraczać 79 znaków.
*   Oddzielaj funkcje i klasy dwoma pustymi liniami, a metody w klasie jedną.

### 7.2. Testowanie kodu
Testowanie kodu, zwłaszcza testy jednostkowe, pomagają w identyfikowaniu i naprawianiu błędów. Testuj każdy element swojego kodu.

### 7.3. Dokumentacja kodu
Dokumentacja kodu ułatwia zrozumienie i korzystanie z Twojego kodu innym programistom.

*   Używaj docstringów dla dokumentowania funkcji i klas.
*   Dodawaj komentarze wyjaśniające skomplikowane fragmenty kodu.
*   Dokumentuj parametry funkcji, wartość zwracaną oraz działanie funkcji w docstringu.
