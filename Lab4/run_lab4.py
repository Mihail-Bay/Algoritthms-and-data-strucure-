from subprocess import *
green = '\033[92m'
end = '\033[0m'

files4 = [
    'task1/src/Stack.py',
    'task4/src/queue.py',
    'task6/src/bracket_sequence_1.py',
    'task9/src/stack_with_max.py',
    'task12/src/max_in_moving_sequence.py',



]

test_files4 = [
    'task1/tests/tests.py',
    'task4/tests/tests.py',
    'task6/tests/tests.py',
    'task9/tests/tests.py',
    'task12/tests/tests.py',



]

def run_tasks(files4):
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')

    for file in files4:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests(test_files4):
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')

    for test_file in test_files4:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    run_tasks(files4)
    run_tests(test_files4)

if __name__ == '__main__':
    main()

"""
    print()
    print()
"""