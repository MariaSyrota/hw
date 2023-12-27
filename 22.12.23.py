# "Підключення бібліотек"
# import random

# from random import randint, choice, choices

# from random import choice as che

# from random import *


# print(random.randint(0, 100))

# print(randint(34, 100))
# print(che(34, 100))

"""LIST"""
# list - генератор списків
# []- латентне створення

# list_1 = []
# list_1 = [99, 89, 98,788, 789]

# list_1 = list()
# str_1 ='qwertyuikol'
# list_1 = list(str_1)
# list_1 = [str_1]

# print(list_1)


"""#properties"""
list_1 = [99, 89, 98,788, 789]

#Index
#__getitem__() оператор для отримання елемента  за індексом
#[] - скорочене позначення
# list_1 = [99, 89, 98,788, 789]
# print(list_1[1])
# print(list_1[1])
# print(list_1[-1])

#Mutable type
#__setitem__() -оператор зміни елемента за індексом

#Iterable
# list_1[4] += '12344'
# list_1[4] = list_1[4].upper()

#Slice
# print(list_1[2:5])
# print(list_1[:5])
# print(list_1[2:])
# print(list_1[2:8:2])
# print(list_1[::])
# print(list_1[7:1:-2])

# list_1[1:4] = [111111111111, 33333333333333333,22222222222222]
# list_1[1:4] = [111111111111]
# list_1[1:4] = [111111111111, 'wertyui', '23456789']
# list_1[2:8:2] = ['rool', 'uwi', None]
# list_1[-1:-9:-2] = ['rool', 'uwi', None, 34567890]

#Iterable
# for el in list_1:
#      print(el)

# print(len(list_1)

#Concatinate
#+
#print(list_1 + ['sdfg', 'dfghu'])
# list_1 += ['sdfg', 'dfghu']

#Dublicate
# # *
# print(list_1 *3)

# list_1 = [0] * 10

#List comprehantion
# list_1 = []

# for i in range(10):
#     list_1.append(randint(0, 100))

# list_1 = [randint(0,100 for i in range(10)]

#list compr + filter
# list_even = [el for el in list_1 if el % 2 == 0]
# print(list_even)

#list compr + ternar operator
list_2 = []
for el in list_1:
    if el % 2:
        new_el = el ** 2
        list_2.append((new_el))
    else:
        new_el = el // 2
        list_2.append((new_el))


# list_2 = [el ** 2 if el % 2 else el // 2 for el in list_1]

print(list_2)
print(list_1)

"""basic fun"""
list_1 = [99, 89, 98,788, 789]

#.append() - один елемент в кінець списку
# list_1.append(12345678)
# list_1.append([12,23,34])

#.extend() -масовий допис в кінець списку
# list_1.extend('united')
# list_1.extend([32,34,456])

# insert(index, elem)-вставка елемента за зазначеним індексом
# list_1.insert((2, 1234))

# list_1.insert((-2, 1234))

#.pop()     
print(list_1)