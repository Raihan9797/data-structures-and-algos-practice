# Link
https://leetcode.com/problems/target-sum/


# Problem
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

```
Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

# Solution
The basic idea is to use recursion. This is also similar to a coin change question. 
- base case 1: list is empty and the summ == target: return 1 (because this is 1 valid combination)
- base case 2: list is empty and the summ != target: return 0 (don't count this as a valid combination)
- recursive case: use the element, call the recursive function but now with a smaller list. There are 2 recursive cases: one where you choose to add the new element, the other when you minus off.
- to improve on this, instead of reducing a smaller list, just use an index to increment so that no new lists need to be made.

- **to make it faster, use caching. Store using (index, summ) : counts. This allows you to now only now which element is being used (index) and whether you plus or minus (summ).**




# Insight
Recall that for dp, we need to start from bottom up. Understand that even if you dont care about the other smaller subproblems, you need it so that you can use it later for your main problem.

- Also learnt how to use caching for python. Basically make a helper function with a table {} as the parameter.