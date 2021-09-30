# Link
https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2375/

## Insight
1. Recognize what to count and not count. Looking at the base and edge cases will help.

- eg 1. when `root = []`. The depth should be 0. This means that one of the base case should be
```python
if root == None:
    return 0
```

- eg 2. when `root = [3, None, None]`, the depth should be 1. We need to see that both children nodes are `None`.
```python
if (root.left == None) and (root.right == None):
    return 1
```


2. For trees, you usually need to connect both branches in the recursive case. Helps to code it out or carefully looking through your code.

- Initially, you separated the branch traversal as you didn't know exactly what to do.
```python
elif (root.left =! None) and (root.right == None):
    return 1 + Solution().maxDepth(root.left)
else:
    return 1 + Solution().maxDepth(root.right)

```
Clearly, this will only traverse one 1 side all the way and return the result. We need to compare the 2 branches using `max()`. So:

```python
else:
    return 1 + max(Solution().maxDepth(root.left), Solution().maxDepth(root.right))
```