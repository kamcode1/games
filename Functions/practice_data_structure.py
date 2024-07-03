###### Lists
# kams_list = [5,"hello",7,10]
# kams_list_2 = [5,"hello",7,10]
# kams_list.append(24)
# del kams_list[2]
# print(kams_list)
# print(kams_list_2)
#
###### Tupels
# a = ("hi",0,"pass",1,2,5)
# print(a)
# print(type(a))
# a = list(a)
# print(a)
# print(a[2])
# a.append(1000)
# print(a)
# print(type(a))
# del a[2]
# print(a)
# b = {"Hello",5,6,2,5,5,5}
# print(b)
# print(type(b))
#
###### SETS
# a = {3,4,5}
# b={4,5,6,8,6,7,9,8,8}
# print(b)
# c= b.intersection(a)
# print(c)
# d = b.union(a)
# print (d)
# f = 3
# print(f in a)
# print(f in b)
# g = a.difference(b)
# print(g)
# h = b.difference(a)
# print(h)
#
###### Dictionaries....
#key value pairs
#the key gives the ability to index your sets
# ydict = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
# print(ydict)

# xdict = dict([('k1','v1'), ('k2','v2'), ('k3', 'v3'), ('k4', 'v4')])
# print(xdict)

# print(xdict['k3'])
# Methods in Dictonaries

# ydict = dict([(1,1), (2,3), (3,3)])
# print(ydict)

# xdict = dict([('k1', 'v1'), ('k2', 'v2'), ('k3','v3')])
# print(xdict)
# ydict.update(xdict)
# print(ydict)
# xdict.update(ydict)
# print(xdict)
#
# z = dict()
# z['a'] = 'alpha'
# z['g'] = 'gama'
# z['o'] = 'omega'

#{'a': 'alpha', 'g': 'gama', 'o': 'omega'}
# print(z)
# print(set(z))
##{'o', 'a', 'g'}
# When changed to a set it only prints the keys and not the values

# def funcd(d, v):
#     for key in d:
#         if d[key] == v:
#             return key
#     return dict()

# ydict = dict([('v1', 1), ('v2', 2), ('v3', 3)])
# print(ydict)


# print(funcd(ydict, 2))
# print(funcd(ydict, 7))

# Exercise 1: Create a list to store names of your favorite fruits. Write code to access the second element and print it.
# fav_fruit = ["Apple", "Orange", "Banana's"]
# print(fav_fruit[2])

# Exercise 2: Define a dictionary to store information about your favorite book, including title, author, and genre. Use the key to retrieve the genre.

# b_dict = dict([('title', 'Game of Thrones'), ('author', 'Kam N.'), ('gener', 'thriller')])
# print(b_dict['gener'])

# Exercise 3: Write a program to generate a random set of numbers between 1 and ten. Use set operations to remove duplicates and display the unique numbers.
import random
random_numbers = [random.randint(1, 10) for _ in range(20)]
print("Generate a list of random number:", random_numbers)

unique_numbers = set(random_numbers)
print("unique numbers:", unique_numbers)