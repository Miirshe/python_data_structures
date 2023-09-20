# created list of fruits in an arrays
fruits = ['apple','lemon','mongo']

#len() return fruit length
print(f'The fruit length : {len(fruits)}')
for fruit in fruits :
    print(f'Fruit : {fruit}')

# append() takes argument values and allows you to add element at the end of list fruits
fruits.append('avocado');
print(f'Fruits : {fruits}')

# insert() takes two arguments values and allows you to add spacific target index position and element values
fruits.insert(0,'papo')
fruits.insert(0,('panana',20))
print(f'Fruits : {fruits}')

# remove() takes argument value that is removed in a list of fruits
fruits.remove(('panana',20))
print(f'Fruits after removed : {fruits}')

# index() takes arguments value of integer that allows you to find list of fruits  by index positions
print(f'Fruit Find By Index Position: {fruits.index(fruits[0])}')

# delete values in a lists by using del keyword
del fruits[3:]
print(f'fruits : {fruits}')

# clear all fruits in a list by using clear() method
fruits.clear();
print(f'fruits : {fruits}')

# and now created fruits name and price by using tuple inside list of fruits
fruits = [
    ('apple',40),
    ('panana',10),
    ('mango',10),
    ('lemon', 15)
]
print(f'fruits : {fruits}')

# now using list unpacking instead of { for fruit in fruits : print(f' index : fruit[0] fruit : fruit[1')} in a fruits
for index, fruit in fruits:
    print(f'Index : {index}  Fruit : {fruit}')
fruits.insert(3,('pop',30))
print(f'Fruits : {fruits}')

#now using lambda expression or anonymous function and filters
filtered = list(filter(lambda fruits: fruits[0] != 'pop' ,fruits))
print(f'Filtered : { filtered }')

# now using lambda expression or anonymous function and map method
my_fruit = list(map(lambda fruits:fruits[0],fruits))
print(f'My_fruits : {my_fruit}')

# reversed fruits of lists
print(f'Reversed Fruit : {fruits[::-1]}')

numbers = [0] * 5
print(f'Numbers repeated : {numbers}')

#take from the user fruit name and price
name = input('Enter Fruit Name ? : ')
price = input('Enter Price Number ? : ')
fruits.insert(0,(name , int(price)))
print(f'successfully added : {fruits}')

