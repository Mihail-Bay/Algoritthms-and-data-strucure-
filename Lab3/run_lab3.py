from subprocess import *
green = '\033[92m'
end = '\033[0m'

files3 = [
    'task1/src/QuickSort.py',
    'task1/src/QuickSortPart3.py',
    'task2/src/AntiQuickSort.py',
    'task3/src/PugaloSort.py',
    'task4/src/SegmentsAndPonts.py',
    'task5/src/Hindex.py',


]

test_files3 = [
    'task1/tests/test_QuickSortPart3.py',
    'task2/tests/test_AntiQuickSort.py',
    'task3/tests/test_PugaloSort.py',
    'task4/tests/test_SegmentsAndPoints.py',
    'task5/tests/test_HIndex.py',



]

def run_tasks(files3):
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')

    for file in files3:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests(test_files3):
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')

    for test_file in test_files3:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    run_tasks(files3)
    run_tests(test_files3)

if __name__ == '__main__':
    main()