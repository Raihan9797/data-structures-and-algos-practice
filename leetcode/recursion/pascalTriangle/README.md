# Link
https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3234/

## Insight
1. Make sure to check the range of your for loops: kept getting recursion depth exceeded. Not because your recursion code was wrong, but because colj > rowi when you were trying to find the entire i^th row values in pascals triangle
2. The recursive solution got Time Limit Exceeded because of how it keeps repeating the same query. To fix, you either can do the iterative version or memoize.
    - Python allows you to immediately memoize a recursive function by adding decorators!
    ```python
    import functools
    
    @functools.cache
    def recursiveFunction():
        ...
    ```