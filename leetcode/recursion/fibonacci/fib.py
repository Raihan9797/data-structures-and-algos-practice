def fib(n: int) -> int:
    cache = {}
    
    def cache_fib(N):
        print(cache)
        if N in cache:
            cache[N]
        
        if N <= 1:
            ans = N
        else:
            f1 = cache_fib(N-1)
            f2 = cache_fib(N-2)
            print("f1: ", f1, "f2: ", f2)
            ans = f1 + f2
        cache[N] = ans
        return ans
    return cache_fib(n)