''' What i learned
1. Make sure you know what you are caching!
- you were storing memo[n] = ans when its only an intermediate solution! ie do this:
memo[i] = ans 

'''

## redo of day 3: memoize recursize fibonacci ##
cache = {
    0: 0,
    1: 1
}

def memo_fib(n):
    if n in cache:
        return cache[n]
    if n in [0,1]:
        return n
    else:
        ans = memo_fib(n-1) + memo_fib(n-2)
        cache[n] = ans
        return ans


memo_fib(5000) # recursion error!


## iterative version ##
## using for loops -> no recursionerror!
memo = {
    0: 0,
    1: 1
}
def iter_fib(n):
    if n in memo:
        return memo[n]
    else:
        for i in range(2, n+1):
            f1 = iter_fib(i -1)
            f2 = iter_fib(i -2)
            # print(f'i:{i}, f1, f2:{f1, f2}')
            ans = f1 + f2
            memo[i] = ans
        return memo[n]

memo
iter_fib(0)
iter_fib(1)
iter_fib(5)
iter_fib(5000)

## make the cache private ##
## when troubleshooting the iterative version, the wrong answers were stored inside the cache. Using a private memo allows us to reset the memo everytime we redefine the function !

def private_iter_fib(n):
    private_memo = {
        0: 0,
        1: 1
    }
    def iter_fib(n):
        if n in private_memo:
            return private_memo[n]
        else:
            for i in range(2, n+1):
                f1 = iter_fib(i -1)
                f2 = iter_fib(i -2)
                # print(f'i:{i}, f1, f2:{f1, f2}')
                ans = f1 + f2
                private_memo[i] = ans
            return private_memo[n]
    return iter_fib(n)

private_memo # cannot access!
private_iter_fib(0)
private_iter_fib(1)
private_iter_fib(5)
private_iter_fib(5000)