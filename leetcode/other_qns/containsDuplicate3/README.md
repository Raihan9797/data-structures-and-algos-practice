# Link
https://leetcode.com/problems/contains-duplicate-iii/


# Problem
Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

 
```
Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```

```
Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```

```
Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```

```
Constraints:
1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1
```

# Solution
1. Brute force solution O(n * k^2)
- This method is quite clear.
```
for idx, num in enumerate(nums):
    for j in range(idx + 1, idx +k+1):
        edge case: check if j exceeds n first -> continue if true

        if abs(nums[j] - nums[idx]) <= t: 
            return True
return False
```

2. The optimal solution: use sliding window and bucket sort O(n)

```
buckets = {}
width = t + 1
for idx, num in enum(nums):
    newval = num // width # integer division

    if newval in buckets:
        return True
    elif (check elements adjacent to the bucket (abv and below)). there is a possiblity the answer is in the adjacent bucket so we need to check this:
        return True
    else:
        buckets[newval] = num
return False
```
    


# Insight
Currently the most difficult problem i've done so far. Requires me to learn use a data structure (dict) in a more novel way. We use the dictionary to bucket the values. Looked at pseudocode from (https://stackoverflow.com/questions/31119971/leetcode-contains-duplicate-iii/48317895)[here] before i implemented it on my own

1. most solutions use Treeset or balanced binary search tree. This allows for O(nlogk). But Python doesnt have Treeset implemented like Java. Others reccomend using sortedcontainers.SortedList, but this may not be something we can use in actual interviews. So I ended up looking for a different solution.

2. We have to think about this problem from a completely different angle. The fact that `a - b <= t` also means that `a - b` can be thought of to lie within a range of `t+1`. eg.
```
t = 3
n1 = 5
n2 = 6
5 // (3 + 1) = 1
6 // (3 + 1) = 1
```
since they lie in the same bucket, they can be considered to be found!

* however, there are 2 similar edge cases: numbers above and below the buckets could actually be a valid answer. eg.
```
nums = [5, 2], t = 3
5 // (3+1) = 1
2 // (3+1) = 0

but abs(5-2) <= 3!!
```
so we need to check this condition for buckets directly above and below.


