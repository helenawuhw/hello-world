# p1.py
# Helena Wu
# 05/20

import random

print "Hello World!"

cache = dict()



def name(value):
    print "Hello " + value
    print random.randint(1,6)
    

    
def new_fibonacci(num):
    
    if cache.has_key(num):
        return cache[num]
    
    if num == 0:
        return 0
  
    if num == 1:
        return 1

    
    ans = new_fibonacci(num - 1) + new_fibonacci(num - 2)
    cache[num] = ans
    return ans

    
# Application code

if __name__ == "__main__":
    name("Helena")
    print "Working!"

    print "new_fibonacci(500) is " + `new_fibonacci(500)`
    print "computed fib"