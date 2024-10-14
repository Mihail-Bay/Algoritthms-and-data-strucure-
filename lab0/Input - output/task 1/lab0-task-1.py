num = input()
splitnum = num.split()
if -10**9 <= int(splitnum[0]) <= 10**9+1:
    if -10**9 <= int(splitnum[1]) <= 10**9+1:
        print(int(splitnum[0]) + int(splitnum[1]))
    else: print('Error')
else: print('Error')

