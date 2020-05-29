import math
import numpy as np
import sys
import tensorflow as tf

print(type(math))
print(dir(math))
print('pi to 4 significant digits {:.4}'.format(math.pi))

print(sys.version)

rolls = np.random.randint(low=1, high=6, size=10)
print(type(rolls))
print(rolls)
print(type(rolls.tolist()), rolls.tolist())

xlist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = np.asarray(xlist)
print(xlist, x, sep='\n')
print(xlist[2][2])
print(x[2, 2], x[(2, 2)])

abc = [(1, 2, 3)]
print(abc, len(abc))

a = tf.constant(1)
b = tf.constant(2)

print(a + b)

# print(dir(list)) ->> TODOS ESSES __something__ estao relacionados
# com operator overloading
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
#  '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
#  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
#   '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
#   'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 
#   'reverse', 'sort']

# For Example:
print(1 in [1, 2, 3])
print([1, 2, 3].__contains__(1))