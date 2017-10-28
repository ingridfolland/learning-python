import random
import sys
import os

test_file = ("test.txt", "wb")

print(test_file.mode)

test_file.write(bytes("I am writing this to a file.\n", "UTF-8"))

test_file.close()