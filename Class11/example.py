#Sorting with a list

list = ['a','c','b','d','g','f','h','x','u']
list.sort()
#print(list)

#Join method with strings
print('X'.join(['My','name','is','Miguel']))

list_one = ["dog", "cat", "lion"]
list_two = ['dog', 'cat', 'puma']

count = 0
for animal in list_one: #cat
    for other_animal in list_two: #dog, cat, puma
        if animal == other_animal:
            count += 1
print(count)

