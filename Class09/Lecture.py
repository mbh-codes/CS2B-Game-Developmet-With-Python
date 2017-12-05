'''
CS2-B Game-Development with Python
November 11, 2017
Class 09
Lecture topics: Deleting Items from Lists & Multiple Assignment
'''

#Deleting Items from Lists

animals = ['aardvark', 'anteater', 'antelope', 'albert']

del animals[1]
print(animals) #list of length 3
#del animals[2]
#print(animals) # list of length 2
#del animals[3] #list of length 1
#print(animals)

presidential_candidates = ['max', 'tom', 'donald', 'bernie']
del presidential_candidates[2]
print(presidential_candidates)
del presidential_candidates[1]
print(presidential_candidates)


#Multiple Assignment
#Allows us to assign multiple variables in one line of code

x = 5
y = 10
#we want x = 10 and we want y = 5
#x = y #here we make x = 10
#y = x  #here y will equal to 10 since x was re-assigned to 10

#placeholder = x
#x = y
#y = placeholder

x , y = y , x

print(x)
print(y)


animals = {'dog': 'max', 'cat': 'maxine'}
dog_name , cat_name = animals['dog'], animals['cat']
print(dog_name)
print(cat_name)

word, category = ['cat', 'animal']
print("our word is", word)
print("our category is", category)


