#CPS:
def fib_c(n, f):
    pass

<<<<<<< HEAD
#Tail recursion implementation:
def fib_a(n, a=[1, 1]):
    if n == 0 or n == 1:
        #return a =
        pass
    
=======


#Tail recursion:
def fib_a(n, a=[0, 0, 1 ]):
    pass
>>>>>>> 0980321a7ebb18f480fc9d57c997242d508b61e7
    
    



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
for i in range(10):
    print(fib_l(i))