# Link
https://leetcode.com/problems/contains-duplicate-ii/submissions/


# Problem
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Solution
Similar to the idea of TwoSum ie. Use Hashmap. Iterate through the list `nums`.
1. if the element is in the table already
    1. check that abs(indexofnewelement - indexofduplicateelement) <=k
        - **if not, update the hashmap to use the new index. Because the other one will be to far for any other upcoming duplicates, and there is a possibility that there will be other duplicates.**
2. else: add to the table using table[value] = index
3. if the for loop has ended without returning True, return False

# Insight
1. Hashmap is powerful. The main idea is to store the previous elements (key) and something important about them (value). compared to the first case where we only care about the existence of duplicates, this takes into account the index of the element so we will store that as the value in the dictionary

2. Since the storing of new values, we also need to update the dictionary. The idea for this is discussed above. We update because we are sure that the old value will no longer be useful to us, and the new value might return us the possiblility of a new True case.