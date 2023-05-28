from random import *
import random as rd
import sys
import keyword
import math
from math import pi
import datetime
from datetime import *

# def func():
#     x = 0
    
#     while True:
#         yield x
#         x += 1


# y = func()

# print(next(y))
# print(next(y))
# print(next(y))

# print(rd.randint(5,12))
# print(rd.random())

# x = [0, 2, 4, 6, 8, 10]

# print(sample(x, 5))

# print(sample(range(0,9), 5))
# print(sys.version)
# print(sys.executable)
# print(keyword.kwlist)

# print(math.floor(100.2))
# print(math.ceil(49.5))
# print(math.sqrt(4200))
# print(math.pow(2,5))
# # print(datetime.datetime.today())
# print(getattr(datetime.today(),'hour'))
# print(datetime.today().strftime('%A'))
# print(datetime.today().strftime('%c'))
# print(datetime.today().strftime('%X'))

# x = 'python job ready'

# print(x.title())

# x = ' Python '

# y = ' job '

# z = ' Questions '

# print(x.strip()+y.strip()+z.strip())

# x = 'Python'
# print(x.center(10,'*'))

# b = [i**2 for i in range(4)]
# print(b)

b = [(x, y) for x in [0, 3, 5] for y in [5, 4, 0] if x!=y]
print(b)

x = [str(round(pi, i)) for i in range(0,5)]
print(x)

a = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

b = [[x[i] for x in a] for i in range(4)]

print(b)