# Problem: https://www.codewars.com/kata/529adbf7533b761c560004e5e

# Implement a memoized solution to the RECURSIVE FIBONACCI ALGORITHM.
# - this means not the bottom up iterative dynamic programming approach!
# ** Can you make it such that the memoization cache is PRIVATE TO THIS FUNCTION **

# Examples (none available, this is the code they want to optimize upon)
# def fibonacci(n):
#     if n in [0, 1]:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)


''' What i learned
## Technical ##
1. A different way of doing equality conditions:
if n == 0 or if n == 1: return n VS
if n in [0, 1]: return n

2. How to make a array / list of different sizes:
list_of_size_n = [None] * (n+1)

3. I should use a dictionary instead of array for memoization: We don't know the exact size required!! Using a dictionary allows us to keep adding on values easily!

4. What does it mean to keep the memoization cache private?: Won't this mean that the function has to keep remaking an array? 

5. Making use of helper functions: as the test cases has a fixed function fibonacci(n) so we can't add another argument inside without getting errors!!

6. Making use of decorators: Python 3 already has a functools.lru_cache which is basically a memoization decorator for any function!

7. The better solution using wrapping or lru cache does not seem to work on VSCode terminal
- we have to create a specific file and then run it using
$ python -m fib.py


## Non-technical ##
1. Did not really try and break down this question on paper first; really should do it especially considering it's difficult for me.

2. Looked at the solution as I really did not understand how to implement it -> means i will come back to redo this question tomorrow! I did try it today without looking at the solutions again.

3. Watching youtube videos about dynamic programming as well as stack overflow does help!

4. Reading the CodeWars comments is also very helpful: led me to a link on decorators!

'''

## My Solution ##
## this solution does not make the cache private!!
memo = {
    0: 0,
    1: 1
}
def fibonacci(n):
    if n in [0, 1]: # base cases
        return n
    if n in memo: # if already stored
        return memo[n]
    else: # else calulate and store
        ans = fibonacci(n-1) + fibonacci(n-2)
        memo[n] = ans
        return ans

fibonacci(100)



## Better Solution ##
def memoized(function):
    cache = {}

    def wrapper(key):
        val = cache.get(key)
        if val is None:
            val = cache[key] = function(key)
        return val
    return wrapper

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


## better solution 2 ##
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

## Testing ##
fibonacci(25)
fibonacci(40)