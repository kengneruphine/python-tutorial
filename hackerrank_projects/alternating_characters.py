#You are given a string containing characters  A and B only. 
#Your task is to change it into a string such that there are no matching adjacent characters.
#To do this, you are allowed to delete zero or more characters in the string.
#Your task is to find the minimum number of required deletions.
#For example, given the string s= AABAAB, remove an A at positions 0 and 3 to make s=ABAB in 2  deletions

def alternating_chars(string):
    removed = 0
    
    index = 0
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            removed += 1
        
    return removed

a='AAABBB'
b='BBBBBABBAAB'

print(alternating_chars(b))