import time
t_start = time.perf_counter()

f1 = 1
f2 = 1
i = 0

n = int(open('input.txt').read())
if n == 0:
    open('output.txt', 'w').write(str(0))
    print(time.perf_counter() - t_start)
elif n == 1 or n == 2:
    open('output.txt', 'w').write(str(1))
    print(time.perf_counter() - t_start)
elif 0 <= n <= 45:
    while i < n - 2:
        f_s = f1+f2
        f1 = f2
        f2 = f_s
        i = i + 1

    open('output.txt', 'w').write(str(f_s))
    print(time.perf_counter() - t_start)
else:
    print('Error')





