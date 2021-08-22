# Link
https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/

# Insight
1. How to memoize in python function: create a cache and function inside a function!

Initially used `@functools.cache` but this is how to actually implement it yourself
```python
def fib(n):
    cache = {}
    def cached_fib(N):
        ....
    
    return cached_fib(n)
```

2. Using HashMap<Integer, Integer> in Java: containsKey(n), get(n) and put(n, ans)