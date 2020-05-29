import math
import numpy as np
import sys
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