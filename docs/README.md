# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Общее описания проекта:

Проект содержит библиотеку функций для нахождения площади и периметра различных геометрических фигур, написанную на языке Python.

# Описание каждой функции с примерами вызова:

## **Функция area

* **Круг** _(circle.py)_ функция принимает на вход значение радиуса круга (R) и возвращает площадь круга, найденную по формуле S = πR².

`Пример вызова функции:`

_входные значения:_ 3
_выходные значения:_ 9π

* **Прямоугольник** _(rectangle.py)_ функция принимает на вход значения длин соседних сторон прямоугольника (a, b) и возвращает площадь прямоугольника, найденную по формуле S = ab.

`Пример вызова функции:`

_входные значения:_ 8 9
_выходные значения:_ 72

* **Квадрат** _(square.py)_ функция принимает на вход значение длины стороны квадрата (a) и возвращает площадь квадрата, найденную по формуле S = a².

`Пример вызова функции:`

_входные значения:_ 4
_выходные значения:_ 16

* **Тругольник** _(triangle.py)_ функция принимает на вход значения длины стороны треугольника и высоты, проведенной к этой стороне (a, h) и возвращает площадь треугольника, найденную по формуле S = 0.5ah.

`Пример вызова функции:`

_входные значения:_ 7 6
_выходные значения:_ 21

## **Функция perimeter

* **Круг** _(circle.py)_ функция принимает на вход значение радиуса круга (R) и возвращает периметр круга, найденный по формуле P = 2πR.

`Пример вызова функции:`

_входные значения:_ 3
_выходные значения:_ 18π

* **Прямоугольник** _(rectangle.py)_ функция принимает на вход значения длин соседних сторон прямоугольника (a, b) и возвращает периметр прямоугольника, найденный по формуле P = 2a + 2b.

`Пример вызова функции:`

_входные значения:_ 6 5
_выходные значения:_ 22

* **Квадрат** _(square.py)_ функция принимает на вход значение длины стороны квадрата (a) и возвращает периметр квадрата, найденный по формуле P = 4a.

`Пример вызова функции:`

_входные значения:_ 11
_выходные значения:_ 44

* **Треугольник** _(triangle.py)_ функция принимает на вход значения длин сторон треугольника (a, b, c) и возвращает периметр треугольника, найденный по формуле P = abc.

`Пример вызова функции:`

_входные значения:_ 11
_выходные значения:_ 44

#Описание истории коммитов:

* **8ba9aeb:** были добавлены файлы square.py и circle.py с функциями area и perimeter для квадрата и треугольника соответственно

* **d078c8d:** был создан файл с документацией проекта

* **281d4fb:** был добавлен файл rectangle.py с функциями area и perimeter для прямоугольника

* **68825b2** был добавлен файл triangle.py с функциями area и perimeter для треугольника и исправлена формула периметра прямоугольника в файле rectangle.py (a + b -> 2(a + b))