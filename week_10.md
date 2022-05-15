# Słowniki w Pythonie
Poprzedni notebook (week 9) dotyczył `list` w Pythonie. W tym notebooku powiemy sobie coś o `słownikach`, czyli kolejnej strukturze danych.
Przypomnijmy najpierw czym były `listy`. 

`Lista` to struktura danych w Pythonie, która jest zmienną, uporządkowaną sekwencją elementów. Listy służą do przechowywania wielu elementów w jednej zmiennej. 

`Indeksowanie`

Listy są `uporządkowane`, można je zmieniać (są `edytowalne`) i zezwalają na `zduplikowane wartości`.

Elementy listy są indeksowane, pierwsza pozycja ma indeks `[0]`, druga pozycja ma indeks `[1]` itd.

Własności `List`:


1. Listy są `Uporządkowane`. Kiedy mówimy, że listy są uporządkowane, oznacza to, że pozycje mają określoną kolejność i ta kolejność się nie zmieni. Jeśli dodasz nowe pozycje do listy, nowe pozycje zostaną umieszczone na końcu listy.
2. Listy są `Edytowalne`. Lista jest edytowalna, co oznacza, że możemy zmieniać, dodawać i usuwać elementy na liście po jej utworzeniu.

3. Listy `zezwalają na duplikaty`. Ponieważ listy są indeksowane, listy mogą zawierać elementy o tej samej wartości.

Listę inicjalizujemy `kwadratowymi nawiasami`.




**Przykład**


```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
```

    ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


# Słownik (dictionary)

Teraz powiemy sobie czym są słowniki w Pythonie.

`Słowniki` służą do przechowywania wartości danych w parach `klucz:wartość`.

Słownik to zbiór `uporządkowany`, `zmienny` i `nie pozwalający na duplikaty`.

Słownik inicjalizujemy `klamrowymi nawiasami`.

# Tworzenie słownika w Pythonie

Tworzenie słownika jest tak proste, jak umieszczanie elementów w nawiasach klamrowych {} oddzielonych przecinkami.

Element ma `klucz` (key) i odpowiadającą mu `wartość` (value), która jest wyrażona jako para (key: value).

Chociaż `wartości` mogą być dowolnego typu danych i mogą się powtarzać, `klucze` muszą być typu `niezmiennego` i muszą być `unikatowe`.

# Przykład


```python
my_dict = {    # tworzenie słownika przy użyciu nawiasów klamrowych
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

W powyższym słowniku `my_dict` kluczami są: `brand`, `model` i `year`, a odpowiadającymi im wartościami są: `Ford`, `Mustang` i `1964`.
Zauważ, że po danym kluczu zawsze dajemy dwukropek, a dopiero potem wartość.

# Tworzenie słownika przy użyciu dict()

`Słownik` w Pythonie może zostać stworzony przy użytciu wbudowanej funkcji `dict()`. Funkcja ta jako argumenty przyjmuje pary `key`,`value`.

## Przykład


```python
x = dict(brand = "Ford", model = "Mustang", year = "1964") #tworzenie słownika przy użyciu dict()
```

Zauważ, że ten sposób inicjalizaji słownika ma pewne różnice:



*   kluczy (`keys`) nie przekazujemy jako stringi,
*   rolę dwukropka pełni znak równości,
*   funkcji `dict()` przekazujemy pary bez zamykania ich w nawias klamrowy.





# Dostęp do elementów ze słownika
Podczas gdy indeksowanie jest używane z innymi typami danych  (np. `listami`) w celu uzyskania dostępu do `wartości`, słownik używa `kluczy`. `Klucze` mogą być używane w nawiasach kwadratowych `[ ]` lub z metodą `get()`.
Jeśli np. chcielibyśmy w słowniku `my_dict` znaleźć `wartość` dla `klucza` `brand` możemy to zrobić tak:


```python
my_dict['brand'] # wartość pod kluczem 'brand'
```




    'Ford'



Lub przy użyciu metody `get()`:


```python
my_dict.get('brand')
```




    'Ford'



Jeśli użyjemy nawiasów kwadratowych `[ ]` dla klucza, którego nie ma słowniku, wyskoczy nam błąd `KeyError`. Metoda `get()` zwróciłaby `None`.


```python
my_dict['bwm']  #klucza 'bwm' nie ma w słowniku --> key error
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-13-04a0b9c4a66f> in <module>()
    ----> 1 my_dict['bwm']
    

    KeyError: 'bwm'



```python
print(my_dict.get('bmw'))   # klucza 'bwm' nie ma w słowniku --> get() zwraca None
```

    None


# Zmienianie i dodawanie elementów słownika

Słowniki są `zmienne` (edytowalne). Możemy dodawać nowe pozycje lub zmieniać wartość istniejących pozycji za pomocą operatora przypisania, czyli `=`.

Jeśli `klucz` jest już obecny, `aktualizowana` jest istniejąca `wartość`. W przypadku braku klucza do słownika dodawana jest nowa para (klucz: wartość).



```python
# Zmienianie i dodawanie elementów słownika
my_dict = {   
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# aktualizowanie wartości
my_dict['year'] = 1987

print(my_dict)
```

    {'brand': 'Ford', 'model': 'Mustang', 'year': 1987}


Zmieniliśmy wartość dla `klucza` `year` na 1987. Podobnie możemy zmienić pozostałe wartości kluczy.


```python
my_dict['brand'] = 'Audi' #aktualizujemy wartośc dla klucza "brand" na "Audi"

my_dict['model'] = 'RS3' #aktualizujemy wartośc dla klucza "model" na "RS3"

my_dict['year'] = 2019 #aktualizujemy wartośc dla klucza "year" na "2019"

print(my_dict)
```

    {'model': 'RS3', 'year': 2019, 'brand': 'Audi'}


# Usuwanie elementów ze słownika

Możemy usunąć konkretną pozycję ze słownika za pomocą metody `pop()`. Ta metoda usuwa element z podanym kluczem i zwraca wartość.


Możemy również użyć słowa kluczowego del, aby usunąć poszczególne pozycje lub cały słownik.


```python
my_dict.pop('brand') #usuwa klucz 'brand' wraz z jego wartością a na koniec printuję tę wartość
```




    'Audi'



Metoda `popitem()` usuwa element, który był ostatnio wstawiany do słownika.


```python
my_dict['color'] = 'red' #wstawmy nową parę: color: red
print(my_dict)
```

    {'model': 'RS3', 'color': 'red'}



```python
my_dict.popitem()  # metoda powinna usunąć ostnio wstawianą parę, czyli color: red. Na koniec wyprintuje usuniętą parę
```




    ('color', 'red')




```python
my_dict # ze słownika zniknęła para color: red
```




    {'model': 'RS3'}



W celu usunięcia wszystkich elementów ze słownika możemy użyc metody `clear()`.


```python
year_of_creation = {'Python': 1993, 'JavaScript': 1995, 'HTML': 1993}  # tworzymy jakiś słownik
print(year_of_creation)
```

    {'Python': 1993, 'JavaScript': 1995, 'HTML': 1993}



```python
year_of_creation.clear()  # metoda clear usunie wszystkie elementy (pary key:value)
print(year_of_creation)
```

    {}


# Metody słownika Pythona

Poniżej zestawione są metody dostępne ze słownikiem. Niektóre z nich zostały już wykorzystane w powyższych przykładach.

| **Metoda**  	| **Opis**                                      	|
|-------------	|-----------------------------------------------	|
| **clear()** 	| **Removes all items from the dictionary.**    	|
| **copy()**  	| **Returns a shallow copy of the dictionary.** 	|


```python

```


```python

```
