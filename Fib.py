
#Tail recursion implementation:
def fib_a(n, a=[1, 1]):
    if n == 0 or n == 1:
        #return a =
        pass
    
    
    



#Traditional recursive implementation:
def fib_r(n):
    if n == 0 or n == 1:
        return 1
    return fib_r(n-1) + fib_r(n-2)



#Iterative implementation:
def fib_l(n):
    current = 1
    previous1 = 0
    previous2 = 0
   
    for i in range(n):
        previous2 = previous1
        previous1 = current
        current = previous1 +previous2
    
    return current
for i in range(10):
    print(fib_l(i))