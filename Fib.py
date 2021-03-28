#CPS:
def fib_c(n, f):
    pass

#Memoization, linear complexity O(n):
def fib_m(n, memo_dict={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo_dict[n]
    except KeyError:
        memo = fib_m(n-1, memo_dict) + fib_m(n-2, memo_dict)
        memo_dict[n] = memo
        return memo
for i in range(30):
    print(fib_m(i))
#Tail recursion, linear complexity O(n):
def fib_t(n, a=[0, 0, 1]):
    
    if n == 0:
        return a[2]
       
    prev1 = a[2]
    prev2 = a[1]
    a = [prev2, prev1, prev1 + prev2]
    
    return fib_t(n-1, a)


#Traditional recursion, explonential complexity O(2^n) :
def fib_r(n):
    if n == 0 or n == 1:
        return 1
    return fib_r(n-1) + fib_r(n-2)

#Tabulation, linear complexity O(n):
def fib_i(n):
    current = 1
    previous1 = 0
    previous2 = 0
   
    for i in range(n):
        previous2 = previous1
        previous1 = current
        current = previous1 +previous2
    return current


  