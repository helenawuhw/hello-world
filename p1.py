# p1.py
# Helena Wu
# 05/20

import random

print "Hello World!"


def name(value):
    print "Hello " + value
    print random.randint(1,6)
    
def fib(num):
  if num == 0:
    return 0
  
  if num == 1:
    return 1

  return fib(num - 1) + fib(num - 2)    
    
# Application code

if __name__ == "__main__":
    name("Helena")
    print "Working!"

    print "fib(10) is " + `fib(10)`
