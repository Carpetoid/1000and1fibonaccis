#CPS:
def fib_c(n, f):
    pass


#Tail recursion, polynomial complexity O(n^2):
def fib_a(n, a=[0, 0, 1]):
    
    if n == 0:
        return a[2]
       
    prev1 = a[2]
    prev2 = a[1]
    a = [prev2, prev1, prev1 + prev2]
    
    return fib_a(n-1, a)


#Traditional recursion, explonential complexity O(2^n) :
def fib_r(n):
    if n == 0 or n == 1:
        return 1
    return fib_r(n-1) + fib_r(n-2)


#Iterative, linear complexity O(n):
def fib_l(n):
    current = 1
    previous1 = 0
    previous2 = 0
   
    for i in range(n):
        previous2 = previous1
        previous1 = current
        current = previous1 +previous2
    return current


  