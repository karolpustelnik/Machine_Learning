# ASSIGNMENT CONFIG
colab: true
init_cell: false
export_cell: false
generate: true
test_files: true
check_all_cell: true

```python
import otter
grader = otter.Notebook()
```

# 1. Python i Data Science


W rozległej dziedzinie jaką jest Data Science Python jest jednym z najlepszych i najbardziej przydatnych narzędzi. Zaraz za nim jest język R, który od lat jest używany głównie przez statystyków. Wśród osób zajmujących się analizą danych od lat trwają spory, które narzędzie jest lepsze. Odpowiedź na to pytanie jest bardzo złożona i zależy m.in. od problemu jaki chcemy rozwiązać. Na tych zajęciach będziemy programowali w Pythonie, dlatego poniżej przedstawimy najważniejsze zalety tego języka programowania:

  1. **Python jest językiem bardzo uniwersalnym.**

    Możemy wykorzystywać go z powodzeniem jako pakiet statystyczny do przeprowadzania analiz statystycznych oraz tworzyć przejrzyste i interaktywne wykresy dzięki bibliotece Plotly. Ponadto w obszarze data science biblioteki NumPy oraz Pandas wykorzystywane są do przekształcania danych i szybkich obliczeń. Z drugiej strony korzystając z Pythona możemy napisać kompletną aplikację komputerową.

  2. **Łatwy do czytania, nauki i pisania**
  
  Python to język programowania wysokiego poziomu, który ma składnię zbliżoną do języka angielskiego. Ułatwia to czytanie i zrozumienie kodu.
  Python jest naprawdę łatwy do opanowania i nauczenia, dlatego wiele osób poleca Pythona początkującym. Do wykonania tego samego zadania potrzeba mniej linii kodu niż w przypadku innych głównych języków, takich jak C/C++ i Java.
  3. **Język interpretowany**
  
  Python jest językiem interpretowanym, co oznacza, że Python bezpośrednio wykonuje kod linia po linii. W przypadku jakiegokolwiek błędu zatrzymuje dalsze wykonywanie i zgłasza błąd, który wystąpił.
  Python pokazuje tylko jeden błąd, nawet jeśli program zawiera wiele błędów. Ułatwia to debugowanie.



# 2. Idea programowania

W dalszej części tego kursu postaramy się zmienić Cię w osobę biegłą w sztuce programowania. W końcu zostaniesz programistą – być może nie profesjonalnym programistą, ale przynajmniej będziesz miał umiejętności, aby spojrzeć na problem analizy danych/informacji i opracować program, który go rozwiąże.

W pewnym sensie, aby zostać programistą, potrzebujesz dwóch umiejętności:

1. Najpierw musisz znać język programowania (Python) - musisz znać słownictwo i gramatykę. Musisz być w stanie poprawnie przeliterować słowa w tym języku i umieć konstruować dobrze sformułowane „zdania” w tym języku.

2. Po drugie, musisz „opowiedzieć historię”. Pisząc historię, łączysz słowa i zdania, aby przekazać czytelnikowi pomysł. W konstruowaniu historii są umiejętności i sztuka, a umiejętność pisania opowieści jest ulepszana poprzez pisanie i uzyskiwanie informacji zwrotnych. W programowaniu nasz program to „historia”, a problem, który próbujesz rozwiązać, to „pomysł”.

Gdy nauczysz się jednego języka programowania, takiego jak Python, znacznie łatwiej będzie Ci nauczyć się drugiego języka programowania, takiego jak JavaScript lub C++. Nowy język programowania ma często inne słownictwo i gramatykę, **ale umiejętności rozwiązywania problemów będą takie same we wszystkich językach programowania.**

Dość szybko nauczysz się „słownictwa” i „zdań” Pythona. Napisanie spójnego programu rozwiązującego zupełnie nowy problem zajmie Ci więcej czasu. Uczymy się programowania podobnie jak uczymy się pisania. Zaczynamy czytać i wyjaśniać programy, potem piszemy proste programy, a potem z biegiem czasu piszemy coraz bardziej złożone programy. W pewnym momencie widzisz wzorce na własną rękę i możesz zobaczyć bardziej naturalnie, jak ugryźć problem i napisać program, który go rozwiąże. A kiedy dojdziesz do tego punktu, programowanie staje się bardzo przyjemnym i kreatywnym procesem.






# Zastrzeżone słowa kluczowe
Każdy język programowania ma określone reguły, których trzeba przestrzegać pisząc w tym języku. W każdym języku, jest też lista wyrazów, które dla tego języka mają szczególne znaczenie - są to tak zwane `zastrzeżone słowa kluczowe` (reserved keywords). Słowa te mają określone znaczenie i nie mogą go zmienić. W szczególności żadne ze słów kluczowych nie może być użyte do nazwania zmiennej (o czym później).


```python
help('keywords')
```

    
    Here is a list of the Python keywords.  Enter any keyword to get more help.
    
    False               class               from                or
    None                continue            global              pass
    True                def                 if                  raise
    and                 del                 import              return
    as                  elif                in                  try
    assert              else                is                  while
    async               except              lambda              with
    await               finally             nonlocal            yield
    break               for                 not                 
    


# Interpreter i kompilator

Python to język wysokiego poziomu, który ma być stosunkowo prosty do czytania i pisania dla ludzi. Inne języki wysokiego poziomu to Java, C++, PHP, Ruby, Basic, Perl, JavaScript. Rzeczywisty sprzęt wewnątrz jednostki centralnej (CPU) nie rozumie żadnego z tych języków wysokiego poziomu.

Procesor rozumie język, który nazywamy `językiem maszynowym`. Język maszynowy jest bardzo prosty i, szczerze mówiąc, bardzo męczący w pisaniu, ponieważ jest reprezentowany przez zera i jedynki:

001010001110100100101010000001111

11100110000011101010010101101101
...


Pomimo tego, że język maszynowy składa się tylko z zer i jedynek, to jego składnia jest bardziej złożona i znacznie bardziej zawiła niż Python. Bardzo niewielu programistów kiedykolwiek pisze program w języku maszynowym. Zamiast tego budujemy różne translatory, aby umożliwić programistom pisanie w językach wysokiego poziomu, takich jak Python lub JavaScript, a te translatory konwertują programy na język maszynowy w celu rzeczywistego wykonania przez procesor.

Te translatory języka programowania dzielą się na dwie ogólne kategorie:


*   interpretery,
*   kompilatory.

**Kompilator** to program komputerowy, który przekształca kod napisany w języku programowania wysokiego poziomu na kod maszynowy. Jest to program, który tłumaczy kod czytelny dla człowieka na język zrozumiały dla procesora komputera (bity binarne 1 i 0). Komputer przetwarza kod maszynowy w celu wykonania odpowiednich zadań.

Kompilator powinien być zgodny z regułą składni języka programowania, w którym jest napisany. Jednak kompilator jest tylko programem i nie może naprawić błędów znalezionych w tym programie. Tak więc, jeśli popełnisz błąd, musisz wprowadzić zmiany w składni swojego programu. W przeciwnym razie nie skompiluje się.

**Interpreter** to program komputerowy, który przekształca każdą instrukcję programu wysokiego poziomu na kod maszynowy. Obejmuje to kod źródłowy, wstępnie skompilowany kod i skrypty. Zarówno kompilator, jak i interpretery wykonują tę samą pracę, która polega na konwersji języka programowania wyższego poziomu na kod maszynowy. Jednak kompilator przekonwertuje kod na kod maszynowy (utworzy plik exe) przed uruchomieniem programu. Interpretery konwertują kod na kod maszynowy po uruchomieniu programu.

Python jest językiem interpretowanym. Interpreter Pythona jest napisany w języku wysokiego poziomu o nazwie „C”. Możesz spojrzeć na rzeczywisty kod źródłowy interpretera Pythona, przechodząc do www.python.org. Zatem Python sam w sobie jest programem i jest kompilowany do kodu maszynowego. 

Dla zainteresowanych dokładniejsze różnice pomiędzy interpreterem a kompilatorem można znaleźć w artykule: https://www.guru99.com/difference-compiler-vs-interpreter.html



# Program komputerowy

**Program komputerowy** to sekwencja instrukcji w języku programowania, którą komputer może wykonać lub zinterpretować. (https://en.wikipedia.org/wiki/Computer_program)

Poniżej znajdue się przykładowy program napisany w Pythonie, który wyświetla napis "Hello, World!"


```python
print("Hello, World!")
```

    Hello, World!



```python
print("Hello, World!" * 2)
```

    Hello, World!Hello, World!


Funkcja odpowiedzialna za wyświetlenie napisu na ekranie nazywa się *print()*. Możemy dowiedzieć się o niej więcej wpisując komendę:


```python
help('print')
```

    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    


Dowiadujemy się stąd, że funkcja `print()` w Pythonie, przyjmuje `value`, który później jest wyświetlany na ekranie. Oprócz tego ma jeszce parę innych argumentów. Interesujący jest argument `sep`, który decyduje o tym co rozdziela kolejne napisy (value) i domyślnie jest to spacja.

Notebooki google są na tyle inteligentne, że same wyświetlają kawałek dokumentacji funkcji, gdy zaczynamy ją wpisaywać. 

Poniżej znajduje się pare prostych przykładów z użyciem funkcji `*print()*`.


```python
print('Hello', 'World!', sep = ', ')  #efekt taki sam jak wyżej
```

    Hello, World!



```python
print('USA', 'Canada', 'Germany', 'France', 'Japan')
```

    USA Canada Germany France Japan



```python
print("USA")
print("Canada")
print("Germany")
print("France")
print("Japan")
```

    USA
    Canada
    Germany
    France
    Japan

# BEGIN QUESTION
name: Q1
points: 0# BEGIN SOLUTION
**Zadanie 1.** Napisz jednolinijkowy program, który wyświetla nazwy państw `USA`, `Canada`, `Germany`, `France` i `Japan` w osobnych linijkach tak jak wyżej (ale używając tylko raz funkcji *print()*).

*Wskazówka: '\n' tworzy nową linijkę.*


```python
print('USA', 'Canada', 'Germany', 'France', 'Japan', sep = '\n') # SOLUTION
```
# END SOLUTION# END QUESTION# BEGIN QUESTION
name: Q2
points: 0
**Zadanie 2.** Napisz jednolinikowy program, który `50 razy` wyświetla słowo `"Python"`, odzielone przecinkami.
# BEGIN SOLUTION

```python
print('Python, '*50) # SOLUTION
```
# END SOLUTION# END QUESTION
# Debugowanie

Podczas pisania programów w Pythonie bardzo często okazuję się, że po uruchomieniu instrukcji wyskakuje błąd.

Przykład:






```python
primt('Hello, World!')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [33], in <cell line: 1>()
    ----> 1 primt('Hello, World!')


    NameError: name 'primt' is not defined


Wyskoczył błąd z kategorii `"NameError"`. Sugeruje on, że instrukcja w naszym programie, zawiera nazwę `"primt"`, która nie jest zdefiniowana. Rzeczywiście, w powyższym programie nigdzie nie definiowaliśmy, czym jest `"primt"` a w szczególności, nie jest to wbudowana funkcja w Pythonie (w odróżnieniu od `print()`). Naturalne więc, że wyskakuje błąd.

Bardzo często pojawiają się również inne typy błędów np.:

* `SyntaxError`
* `LogicError`
* `SemanticError`

Podczas pisania programów, bardzo często najwięcej czasu poświęcamy właśnie na naprawianiu błędów, czyli `**debugowaniu**`. Umiejętność szybkiego debugowania kodu jest bardzo cenna w pracy informatyka.

# Zmienne

`Zmienne` służą do przechowywania informacji, do których można się odwoływać i manipulować nimi w programie komputerowym. Zapewniają również sposób oznaczania danych opisową nazwą, dzięki czemu nasze programy mogą być lepiej rozumiane przez czytelnika i nas samych. Pomocne jest myślenie o zmiennych jako o kontenerach przechowujących informacje. Ich jedynym celem jest etykietowanie i przechowywanie danych w pamięci. Te dane mogą być następnie wykorzystywane w całym programie.
Aby stworzyć zmienną, wystarczy nadać jej nazwę i przyrównać do wartości, jaką chcemy żeby przyjmowała. Wartością moze byc np. liczba lub tekst (string, w skócie str).

**Uwaga!** `Zastrzeżone słowa kluczowe` (reserved keywords) nie mogą być użyte do nazywania zmiennej.

Przykład:




```python
x = 6  ## przypisuję wartość 6 zmiennej x
y = "Programowanie jest super!"  ## przypisuję tekst zmiennej y
print(x)
print(y)

```

    6
    Programowanie jest super!


Zauważ, że chcąc wyświetlić wartość zmiennej funkcją `print()` w argumencie tej funkcji wpisliśmy nazwę tej zmiennej bez cudzysłowu. Gdybyśmy użyli cudzysłowu efekt byłby następujący:


```python
x = 6  ## przypisuję wartość 6 zmiennej x
y = "Programowanie jest super!"  ## przypisuję tekst zmiennej y
print('x')
print('y')
```

    x
    y


Na zmiennych możemy wykonywać różne działania, np. mnożenie, dzielenie, potęgowanie itd.



```python
x = 6
print(x*x)
```

    36


# Operacje arytmetyczne na zmiennych



*   '+' dodawanie
*   '-' odejmowanie
* '*' mnożenie
* '/' dzielenie
* '%' modulo (zwraca resztę z dzielenia)
* '**' potęgowanie



Zmienna `x` zadeklarowana powyżej, może zostać użyta później w programie i zmienić wartość:


```python
x = x+1
print(x)
```

    7



```python
x = (x+1)*2
print(x)
```

    16



```python
x = 4
x**2  #znak potęgowania to **, a nie ^
print(x)
```

    4



```python
x = 4
y = 5
print(x**y)
```

    1024


Komenda `%` służy do wykonania operacji `modulo`. Zwraca ona resztę z dzielenia.


```python
20%4  #zwraca resztę z dzielenie 20 przez 4
```




    0




```python
x = 11
y = 2
print(x%y)  #reszta z dzielenia 11 przez 2
```

    1


**Zadanie 3.** Znajdź błąd w poniższym programie:


```python
lambda = 6
print(lambda)
```


      Input In [41]
        lambda = 6
               ^
    SyntaxError: invalid syntax



# Funkcja *input()*

Funkcja `input()` umożliwia interakcję użytkownika z programem. Jako argument przyjmuje napis, który ma zostać wyświetlony użytkownikowi. 

Poniższy program zapyta Cię o imię, a po wpisaniu i naciśnięciu Enter wyświetli je na ekranie.



```python
x = input('Enter your name: ')   #program zapyta Cię o imię
print('Hello, ' + x)
```

Funkcja input() zawsze traktuje wpisany argument jako `str` (string, czyli tekst). Spróbuj to sprawdzić, tzn. wpisz dowolną liczbę po uruchomieniu poniższej komórki, i zobacz czy jej typ to `str`. 


```python
x = input("Wpisz jakąs liczbę")
print(type(x))
```

Aby przekształcić zmienną x na `liczbę całkowitą` (int), wystarczy poniższa komenda:


```python
x = int(x)
type(x)
```


```python
x = '5' # string
y = 5 # int
```

Więcej o typach zmiennych dowiesz się na późniejszych zajęciach.

**Zadanie 4.** Napisz program, który wyświetla tekst wpisany przez użytkownika, tyle razy ile określi. Program ma przyjmować dwie zmienne wpisywane przez użytkownika. Pierwsza z nich, `x` ma oznaczać tekst, który użytkownik chce żeby był wyświetlany, a druga, `y`, liczbę ile razy ten tekst ma pojawić się na ekranie. 
**Na przykład dla danych wejściowych:**
Nauczę się programować!

3


**Prawidłową odpowiedzią jest:**

Nauczę się programować! Nauczę się programować! Nauczę się programować!
# BEGIN QUESTION
name: Q4
points: 0# BEGIN SOLUTION

```python
### TO DO ###
x = int(input()) # int() zapewnia by input byl liczba, a nie stringiem, 
y = input() # SOLUTION
print(x*y) # SOLUTION
### END ###


```
# END SOLUTION# END QUESTION# BEGIN QUESTION
name: Q5
points: 0.5

# **Zadanie domowe**
Napisz program, który przyjmuje dowolną liczbę naturalną `x`, a następnie resztę z dzielenia tej liczby przez 5.



# BEGIN SOLUTION

```python
def reszta(x): # nie zmieniaj tej lini
    y = x%5 # SOLUTION
    return y # nie zmieniaj tej lini
print(reszta(x)) # pokazuje reszte z dzielenia przez 5
```
# END SOLUTION# BEGIN TESTS

```python
x = 7
assert reszta(x) == 2   
```


```python
x = 13
assert reszta(x) == 3
```


```python
x = 64
assert reszta(x) == 4, 
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [3], in <cell line: 2>()
          1 x = 64
    ----> 2 assert reszta(x) == 4


    NameError: name 'reszta' is not defined

# END TESTS# END QUESTION