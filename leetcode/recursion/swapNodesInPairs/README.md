# Link
https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/

# Insight
1. Wishful thinking: assuming you have done for the tail, what is it supposed to look like and how do you complete it?

head-> 1 -> 2 -> 3 -> 4

Wishful thinking
head -> 1 -> 2 -> (4 -> 3)

Then think about how to return the final list
newhead -> 2 -> 1 -> 4 -> 3