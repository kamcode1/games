# def greet(name):
#     hello = f"Hello there {name}!"
#     print(hello)
# greet("kam")

# def area(width, length):
#     area = width * length
#     return area
   
# answer = area(5,6)
# print(answer)

# def odd_even(number):
#     if number % 2 == 0:
#         print(f"{number} is an even number!")
#     else:
#         print(f"{number} is an odd number!")
# odd_even(12)

# Practicing Namespace
# x = 'global x'
# def outer():
#     x = 'outer x'
#     def inner():
#         x = 'inner x'
#         print(x)
#     inner()     
#     print(x)

# outer()    # in the above function python follows the LEGB rule first, when the functions are executed first it looks for the variable x in the local scope then it looks for it in the Eclosing scope if it can't find it, finally it will look for it in the Global Scope.
# import math

# s = math.sqrt(4)
# print(s)