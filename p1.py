# p1.py
# Helena Wu
# 05/20

import random

print "Hello World!"


def name(value):
    print "Hello " + value
    print random.randint(1,6)
    
def fibonacci(num):
  if num == 0:
    return 0
  
  if num == 1:
    return 1

  return fibonacci(num - 1) + fibonacci(num - 2)    
    
# Application code

if __name__ == "__main__":
    name("Helena")
    print "Working!"

    print "fibonacci(10) is " + `fibonacci(10)`
