# Задача 7: Подсчет красивых пар

## Описание
Данная задача включает реализацию алгоритма для подсчета "красивых пар" камней, где каждая пара определяется заранее. Основной целью является подсчет всех возможных красивых пар в строке камней.

## Структура проекта
Lab6/
|-- src/
| |-- input.txt
| |-- Count_beautiful_pairs.py
| |-- output.txt
|-- tests/
| |-- test_Count_beautiful_pairs.py


### Описание файлов:
- `src/Count_beautiful_pairs.py`: Основной скрипт с реализацией функции подсчета красивых пар.
- `src/input.txt`: Входной файл, содержащий информацию о камнях и парах.
- `src/output.txt`: Выходной файл, содержащий количество красивых пар.
- `tests/test_Count_beautiful_pairs.py`: Модуль с тестами для проверки корректности работы алгоритма.

## Как запустить проект
1. **Установка зависимостей**: Проект не требует дополнительных зависимостей, кроме стандартной библиотеки Python.
2. **Запуск алгоритма подсчета красивых пар**:
   - Перейдите в директорию Lab6/src.
   - Убедитесь, что файл `input.txt` содержит корректные входные данные. Формат файла:
     - Первая строка содержит два целых числа n и k.
     - Вторая строка содержит строку S.
     - Следующие k строк содержат пары "a b".
   - Выполните команду:
     ```sh
     python Count_beautiful_pairs.py
     ```
   - Результат будет записан в файл `output.txt`.

3. **Запуск тестов**:
   - Перейдите в директорию Lab6/tests.
   - Выполните команду:
     ```sh
     python -m unittest test_Count_beautiful_pairs.py
     ```
   - Все тесты должны завершиться успешно, подтверждая корректность работы алгоритма.

## Формат входных и выходных данных
**Входной файл (`input.txt`)**:
- Первая строка: два целых числа n и k.
- Вторая строка: строка S.
- Следующие k строк содержат пары "a b".

**Выходной файл (`output.txt`)**:
- Содержит количество красивых пар.

## Описание алгоритма
Алгоритм подсчета красивых пар использует отображение для хранения пар и подсчитывает количество встречаемых камней. Он проходит по строке S и считает количество красивых пар.

1. **Создание отображения**: Создает отображение для красивых пар.
2. **Подсчет пар**: Проходит по каждому камню в строке S и подсчитывает количество красивых пар, используя информацию из отображения.

## Тестирование
Для проверки работоспособности алгоритма реализованы юнит-тесты в файле `test_Count_beautiful_pairs.py`. Тесты включают:
- Подсчет красивых пар для различных строк.
- Обработку случаев с повторяющимися камнями.
- Проверку на некорректные пары.

Запуск тестов позволяет убедиться в корректности работы функции для различных сценариев.