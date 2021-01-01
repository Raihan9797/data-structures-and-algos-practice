## this memoized fib makes use of python decorators to run the code.
## have also included the timer functions so you can see that this runs a lot faster than in the vscode terminal which doesnt even run fib(50)
from functools import lru_cache
import timeit

@lru_cache(None)
def fib(n):
    if n in [0, 1]:
        return n
    else:
        return fib(n-2) + fib(n-1)

t = timeit.default_timer()
print(fib(50))
print(timeit.default_timer() - t)

t = timeit.default_timer()
print(fib(50))
print(timeit.default_timer() - t)