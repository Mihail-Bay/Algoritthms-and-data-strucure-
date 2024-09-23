num = open('input.txt').read()
splitnum = num.split()
if -10**9 <= int(splitnum[0]) <= 10**9+1:
    if -10**9 <= int(splitnum[1]) <= 10**9+1:
        a = (int(splitnum[0]) + int(splitnum[1])**2)
        open('output.txt', 'w').write(str(a))
    else:
        print('Error')
else:
    print('Error')