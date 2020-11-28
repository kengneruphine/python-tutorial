a =[6, 4,1]

numSwaps = 0 

def countSwaps(a):
    global numSwaps
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]> a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]
                numSwaps +=1
            else:
                continue
    
    print('Array is sorted in {} swaps.'.format(numSwaps))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[len(a)-1]))
    return 'number of swaps is {}'.format(numSwaps)

print(countSwaps(a))