from subprocess import *
green = '\033[92m'
end = '\033[0m'

files7 = [

    'task4/src/longest_common_subsequence.py',
    'task7/src/templates.py',




]

test_files7 = [

    'task4/tests/tests.py',
    'task7/tests/tests.py',




]

def run_tasks(files7):
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')

    for file in files7:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests(test_files7):
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')

    for test_file in test_files7:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    run_tasks(files7)
    run_tests(test_files7)

if __name__ == '__main__':
    main()

"""
    print()
    print()
"""