import random
import sys
import os

alist = ['apple', 'bananas', 'cherries', 'tomatoes']

a = 5

print(5 + 5)

print(alist[3])

print(a)

print(a + 5)


def bar(x):
    if x == 4:
        print('ta da')
    else:
        print('nope')


def foo(x):
    while x >= 0:
        print(x)
        x = x - 1
        if x == 0:
            bar(x)
    print('done')



bar(4)
foo(5)

num = 10

print('I have just printed %s pages' % (num))

print(f'I am testing this cool thign {num}')

print("""Dear %(recipient)s,

I wish you to leave Sunnydale and never return.

Not Quite Love,
%(sender)s
""" % {'sender': 'Buffy the Vampire Slayer', 'recipient': 'Spike'})


