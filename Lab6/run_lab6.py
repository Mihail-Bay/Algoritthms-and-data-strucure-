from subprocess import *
green = '\033[92m'
end = '\033[0m'

files6 = [
    'task1/src/Array.py',
    'task2/src/phone_book.py',
    'task4/src/AssociativeArray.py',
    'task5/src/Process_elections.py',
    'task7/src/Count_beautiful_pairs.py',



]

test_files6 = [
    'task1/tests/tests.py',
    'task2/tests/tests.py',
    'task4/tests/tests.py',
    'task5/tests/tests.py',
    'task7/tests/tests.py',



]

def run_tasks(files6):
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')

    for file in files6:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests(test_files6):
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')

    for test_file in test_files6:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    run_tasks(files6)
    run_tests(test_files6)

if __name__ == '__main__':
    main()

"""
    print()
    print()
"""