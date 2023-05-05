max_level=5
for level in range(1,max_level+1):
    for i in range(max_level-level):
        print(' ',end='')
    for j in range(2*level-1):
        print('*',end='')
    print()