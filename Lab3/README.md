# Лабораторная работа №3: Быстрая сортировка и сортировки за линейное время

## Описание

Данная лабораторная работа посвящена реализации и тестированию алгоритмов быстрой сортировки, а также алгоритмов сортировки, работающих за линейное время. Основные цели работы заключаются в изучении и сравнении различных подходов к сортировке, таких как рандомизированная быстрая сортировка и модификации, а также в освоении алгоритмов, позволяющих сортировать массивы за линейное время, таких как сортировка подсчетом.

## Структура проекта
```
Lab-3/
|-- Task-1/
|   |-- src/
|   |   |-- QuickSort.py
|   |-- tests/
|       |-- test_QuickSort.py
|   |-- txtf/
|   |   |-- input.txt
|   |   |-- output.txt
|
|-- Task-2/
|   |-- src/
|   |   |-- Counting_Sort.py
|   |-- tests/
|       |-- test_Counting_Sort.py
|   |-- txtf/
|   |   |-- input.txt
|   |   |-- output.txt
|
|-- Task-3/
|   |-- src/
|   |   |-- Radix_Sort.py
|   |-- tests/
|       |-- test_Radix_Sort.py
|   |-- txtf/
|   |   |-- input.txt
|   |   |-- output.txt
|
|-- Task-4/
|   |-- src/
|   |   |-- Hybrid_Sort.py
|   |-- tests/
|       |-- test_Hybrid_Sort.py
|   |-- txtf/
|   |   |-- input.txt
|   |   |-- output.txt
|
|-- Task-5/
|   |-- src/
|   |   |-- Optimized_QuickSort.py
|   |-- tests/
|       |-- test_Optimized_QuickSort.py
|   |-- txtf/
        |-- input.txt
        |-- output.txt
```

**Задачи**
Задача 1: Быстрая сортировка

Реализация алгоритма быстрой сортировки, использующего рандомизированный подход для повышения производительности. В данной задаче предусмотрены преимущества данного алгоритма и его сравнение с обычными методами сортировки.

Задача 2: Сортировка подсчетом

Реализация алгоритма сортировки подсчетом, который работает за линейное время при определенных условиях. В данной задаче реализуется алгоритм, подходящий для сортировки целых чисел, находящихся в ограниченном диапазоне.

Задача 3: Сортировка с помощью Radix

Реализация алгоритма сортировки с использованием Radix Sort, который позволяет сортировать целые числа путем обработки каждого разряда. Асимптотическая сложность данного алгоритма также является линейной.

Задача 4: Гибридная сортировка

Разработка гибридного алгоритма, который комбинирует разные методы сортировки. Например, используется быстрое или слияние для больших массивов и сортировка вставками на малых подмассивов.

Задача 5: Оптимизированная быстрая сортировка

Улучшенная версия быстрой сортировки, использующая трехстороннее разделение для эффективной обработки массивов с множеством одинаковых элементов.

Запуск проектов

Каждая из задач расположена в своей отдельной директории. В каждом каталоге содержатся исходные файлы, входные данные (input.txt), выходные данные (output.txt) и тесты для проверки правильности работы алгоритмов.

Для запуска каждой задачи:

  -Перейдите в директорию с задачей (например, Task-1/src).

  -Убедитесь, что файл input.txt содержит корректные данные в соответствии с форматом задачи.

  -Запустите соответствующий скрипт Python для выполнения задачи, например:

```bash
python QuickSort.py
```
  -Результат работы программы будет записан в файл output.txt.

Тестирование

Тесты разработаны для каждой задачи и включают проверку различных сценариев, таких как обычные массивы, пустые массивы, уже отсортированные массивы, массивы в обратном порядке, некорректные входные данные и прочие граничные случаи.

Тестирование позволяет убедиться в корректности работы каждого из реализованных алгоритмов и их устойчивости к различным типам входных данных. Лабораторная работа также включает сравнение производительности различных алгоритмов с целью определения их эффективности при обработке различных наборов данных.

  
