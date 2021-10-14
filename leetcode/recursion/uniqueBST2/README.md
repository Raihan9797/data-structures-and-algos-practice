# Link
https://leetcode.com/problems/unique-binary-search-trees-ii/

## Problem 
* (could not complete on my own)
Given a value `n`, generate all unique valid bsts of length `n`.

## Insight
1. Watching the videos, I do understand whats going on, but implementation wise, it was a lot harder than i thought. Also was able to visualize by drawing given the code. But not really able to brake it down code wise (ie writing in terms of arrays vs drawing trees)

2. Need to recall wishful thinking: Really assume that what you need is already there for you to use! The part of l_trees and r_trees made need to be "completed". You just need to understand whats the additional steps you need to build on the smaller subproblems.

3. Also had trouble understanding how to store the trees into a list: Use the key TreeNode

4. Also had trouble understanding why you need to return `[None]` vs `None`: It's because we need to remember that we are returning a list of TreeNodes. It just so happens there isn't a node there.

5. Also would be better if I can print out the Tree. But I'm not sure how to implement the `repr__` or create a `Tree` class.