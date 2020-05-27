a = round(2.3332523, ndigits = 4)
print(a)
print("a b c", "d e f", sep="-")

def least_difference(a, b, c):
    """Returns the smallest difference between 
    any two numbers of the a, b and c numbers

    >>> least_difference(1, 4, 60)
    3
    """
    diff1 = abs(a - b)
    diff2 = abs(a - c)
    diff3 = abs(b - c)
    return min(diff1, diff2, diff3)
print(
    least_difference(1, 2, 2),
    least_difference(1, 2, 5),
    least_difference(4, 6, 90),
)
help(least_difference)

def function_none():
    abc = "abc"

print(function_none())

print(print(print())) # the function print() doesn't return anything

def greet(who="Victor"):
    print("Hello", who)

greet("Someone")
greet()

def mult_by_five(x):
    return 5 * x
def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)
def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))
print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5
print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

print(round(8.1234, ndigits=-1)) #round it to the nearest tenth