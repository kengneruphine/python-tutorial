#remove all unmatching characters so that the rest will form anagram
def makeAnagram(a, b):
    removed, dict_a, dict_b = 0, {}, {}
    for char in a:
        if char not in dict_b:
            dict_b[char] = 0

        if char in dict_a:
            dict_a[char] += 1
        else:
            dict_a[char] = 1

    for char in b:
        if char not in dict_a:
            dict_a[char] = 0
                
        if char in dict_b:
            dict_b[char] += 1
        else:
            dict_b[char] = 1

    for char, count in dict_a.items():
        difference = 0

        if dict_b[char] > count:
            difference = abs(dict_b[char] - count)
            removed += difference

        elif dict_b[char] < count:
            difference = abs(dict_b[char] - count)
            removed += difference
        else:
            pass
            
    return removed
    

        
a='cded'
b='abcd'

print(makeAnagram(a,b))
