# Link
https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2382/

## Problem
Merge 2 sorted lists into one sorted list
***No Java code due to time constraint, and practicing for job interviews requiring use of Python***

**Time taken: ~20 mins**

## Insight
1. How to actually "concat" lists that have been implemented by leetcode.
- Unlike the regular python lists, we need to cant just use `+` operators. Look at the underlying data structure to understand how to append and access values.

- The problem needed me to make sure that the list i got back from the recursive calls were joined correctly.

```python
### recursive case
if h1.val <= h2.val:
    h1.next = self.mergeTwoLists(l1.next, l2)
    return h1
else:
    h2.next = self.mergeTwoLists(l1, l2.next)
    return h2
```

- Observe how the recursive case needs to be another `ListNode`, so I joined the recursive case using `h1.next`.


2. Problems when trying to convert to a tail recursive case or even iterative case. It seems like this problem does not lend itself well to tail recursive. I tried something like `helper(l1, l2, acc)` but the problem is that the accumulator needs to return the entire list, which means its the `head` of the result. But to keep adding more elements, a `tail` is needed to increment.

- also tried to do `helper(l1, l2, head, tail)`, but it got too complicated.

- the iterative case shown is quite understandable, but im guessing due to the many if else cases, it becomes hard to implement the tail recursive equivalent.


```