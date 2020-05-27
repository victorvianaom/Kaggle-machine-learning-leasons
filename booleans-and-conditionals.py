x = True
print(x)
print(type(x))
print('3' == 3)
print(3.0000 == 3)

def is_odd(n):
    return (n % 2) == 1
print('is 80 odd? ', is_odd(80))
print(True or True and False) # `and` has a higher precedence than `or`

def inspect(x):
    if x > 0:
        print(x, "is greater zero")
    elif x < 0:
        print(x, 'is less than zero')
    elif x == 0:
        print(x, 'is zero')
    else:
        print('you`ve gotta be wrong...')
inspect(2)
inspect(-3)
#inspect('1')
print(bool('False'), bool('F'), bool(231234123), bool(1), bool(0))
print(bool('asfasdfas'), bool('a'), bool(' '), bool(''))
if 0:
    print('zero is converted to False')
else:
    print('so if zero is False, this code is executed')

a = 'abc' if 0 else 'cdf' #massa
print(a)

print(int(False), int(True))
print(False + True + True + False + True + 1 + 2) #True converts to integer 1 and False to 0