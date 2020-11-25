list1 =[1,2,3,4,5]

list2=['one', 'two', 'three', 'four','five']

#list must be of the same length
zipped = list(zip(list1, list2))
print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)

items = ['Apples','Banana','Oranges']
counts =[4, 8, 10]
prices = [89.0,90.0,34.99]

sentences=[]

for (item, count, price) in zip(items,counts,prices):
    sentence = 'I bought {} {}\'s at {} cents each'.format(count, item,price)
    sentences.append(sentence)

print(sentences)