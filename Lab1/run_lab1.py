from subprocess import *
green = '\033[92m'
end = '\033[0m'

files1 = [
    'Task1/src/task1.py',
    'Task2/src/task2.py',
    'Task3/src/task3.py',
    'Task4/src/task4.py',
    'Task5/src/task5.py',
    'Task6/src/task6.py',

]

test_files1 = [
    'Task1/tests/tests.py',
    'Task2/tests/tests.py',
    'Task3/tests/tests.py',
    'Task4/tests/tests.py',
    'Task5/tests/tests.py',
    'Task6/tests/tests.py',


]

def run_tasks(files1):
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')

    for file in files1:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests(test_files1):
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')

    for test_file in test_files1:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    run_tasks(files1)
    run_tests(test_files1)

if __name__ == '__main__':
    main()