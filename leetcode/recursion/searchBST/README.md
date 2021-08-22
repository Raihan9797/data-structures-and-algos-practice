# link
https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/

## Insight
1. 2 different recursive cases and how to get them to base case: don't forget the properties of data structure given. BST is sorted such that root.left.val < root.val < root.right.val. So if the value we are looking for is less than root, return root.left!