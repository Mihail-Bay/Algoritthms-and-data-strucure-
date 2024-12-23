from subprocess import *
from Lab1.run_lab1 import *
from Lab2.run_lab2 import *
from Lab3.run_lab3 import *
from Lab4.run_lab4 import *
from Lab5.run_lab5 import *
from Lab6.run_lab6 import *
from Lab7.run_lab7 import *
green = '\033[92m'
end = '\033[0m'
files = []
test_files = []

[files.append(f'lab1/{i}') for i in files1]
[files.append(f'lab2/{i}') for i in files2]
[files.append(f'lab3/{i}') for i in files3]
[files.append(f'lab4/{i}') for i in files4]
[files.append(f'lab5/{i}') for i in files5]
[files.append(f'lab6/{i}') for i in files6]
[files.append(f'lab7/{i}') for i in files7]

[test_files.append(f'lab1/{i}') for i in test_files1]
[test_files.append(f'lab2/{i}') for i in test_files2]
[test_files.append(f'lab3/{i}') for i in test_files3]
[test_files.append(f'lab4/{i}') for i in test_files4]
[test_files.append(f'lab5/{i}') for i in test_files5]
[test_files.append(f'lab6/{i}') for i in test_files6]
[test_files.append(f'lab7/{i}') for i in test_files7]

def run_tasks(files):
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')

    for file in files:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests(test_files):
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')

    for test_file in test_files:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    run_tasks(files)
    run_tests(test_files)

if __name__ == '__main__':
    main()