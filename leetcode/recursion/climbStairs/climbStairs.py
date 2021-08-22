def climbStairs(n: int) -> int:
    cache = {}
    
    def cached(n):
        if n in cache:
            return cache[n]
        if n == 0:
            ans = 1
        elif n < 0:
            ans = 0
        else:
            # if one step
            ans = cached(n-1) + cached(n-2)
        cache[n] = ans
        return ans
            
            # if 2 step
    return cached(n)