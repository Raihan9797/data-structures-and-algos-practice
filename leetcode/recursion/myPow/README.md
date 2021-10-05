# Link
https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2380/

## Problem
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

## Insight
1. Iterative doesnt always mean its faster than recursive. It just prevents memory limit exceeded. Prevent Time Limit Exceeded by optimising the code. In most cases, tail recursive (ie recursive with accumulator) == iterative (except in Java).
- As we can see below, the iterative solution is not "faster" than the recursive solution because its complexity is O(n). Whereas the recursive solution SPLITS the cases into 2 resulting in O(logn)!

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:

        ############################################
        ### OPTIMAL SOLUTION
        ############################################
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            positive_n = -1 * n
            reciprocal_x = 1/x
            return self.myPow(reciprocal_x, positive_n)
        else:
            if (n % 2 == 0) :
                half = self.myPow(x, int(n/2))
                return half * half
            else:
                return x * self.myPow(x, n - 1)
        
        ############################################
        ### NAIVE ITERATIVE SOLUTION: STILL TLE! ###
        ############################################
        # acc = 1.0
        # if n < 0:
        #     new_x = 1/x
        #     new_n = -n
        #     for i in range(0, new_n):
        #         acc *= new_x
                
        # else:
        #     for i in range(0, n):
        #         acc *= x
        # return acc
```