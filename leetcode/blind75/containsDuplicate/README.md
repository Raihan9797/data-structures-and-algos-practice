# Link
https://leetcode.com/problems/contains-duplicate/
* there are containsduplicate v2 and v3


# Problem
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Solution
Similar to the idea of TwoSum ie. Use Hashmap. Iterate through the list `nums`.
1. if the element is in the table already -> return True (duplicate found)
2. else: add the element into the dict
3. if the for loop has ended without returning True, return False

# Insight
1. Hashmap is powerful. The main idea is to store the previous elements (key) and something important about them (value). In this case, we just need to store the idea of its existence, so the value doesnt really matter.