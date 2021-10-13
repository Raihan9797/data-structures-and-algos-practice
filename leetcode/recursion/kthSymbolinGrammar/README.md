# Link
https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/1675/

## Problem 
* (completed in 41 mins)
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

## Insight
1. At the start of every recursion problem, the main focus should be to find the recurrence relation. DO NOT START ASSUMING THAT YOU KNOW THE RECURRENCE RELATION, OR THAT YOUR FIRST TRY WILL BE PERFECT. Start by writing down more complex examples (the elements for the lower rows) and try to find patterns that you can mathematically express bit by bit.
- First started by comparing the first 2 rows and got:
    - if k is odd: `(n, k) = (n-1, k)`
    - else: `(n, k) = (n-1, k-1)`
    - eg `(2, 2) -> (2-1, 2-1) -> (1, 1)`

- then improved to include all rows
    - if k is odd: `(n, k) = (n-1, k - int(k/2))`
    - else: `(n, k) = (n-1, k - int(k/2))`
    - eg `(4, 7) -> (4-1, 7 - int(3/2)) -> (3, 4)`

- then merged them:
    - `(n, k) = (n-1, k - int(k/2))`

- now consider how the values switch:
    - if k is odd: switch the values ie `0 -> 1` and vice versa
    - else: dont change anything

- finally come up with the recurrence relation
    - if k is odd: `(n, k) = SWTICH(n-1, k - int(k/2))`
    - else: `(n, k) = (n-1, k - int(k/2))`



2. How the function is displayed can be a hint. The question parameters were `(int n, int k)`. Should have realised that the recurrence relation was relating to `(n, k)` instead of having to rely on the hint.
