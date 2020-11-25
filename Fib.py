#CPS:
def fib_c(n, f):
    pass



#Tail recursion:
def fib_a(n, a=[0, 0, 1 ]):
    pass
    
    



#Traditional recursion:
def fib_r(n):
    if n == 0 or n == 1:
        return 1
    return fib_r(n-1) + fib_r(n-2)



#Iterative:
def fib_l(n):
    current = 1
    previous1 = 0
    previous2 = 0
   
    for i in range(n):
        previous2 = previous1
        previous1 = current
        current = previous1 +previous2
    
    return current
