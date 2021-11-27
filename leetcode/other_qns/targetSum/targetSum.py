from typing import List

class Solution:
    def helper(self, summ, nums, target):
        """
        summ: current sum of the combinations
        nums: a list of the numbers that gets smaller over time
        target: the target value to reach using the nums

        similar to coin change idea
        - choice to plus or minus the element to the summ
        - however no need to choose min or max, just counting hence return 1 if correct
        - return 0 if target != sum ie this combination is invalid
        - the recursive case happens by reducing the amount of elements in the list
        - the idea is to pop the list
        """
        if len(nums) == 0 and summ == target:
            return 1
        elif len(nums) == 0 and summ != target:
            return 0
        else:
            #print(nums)
            plus = summ + nums[0]
            minus = summ - nums[0]
            new_nums = nums[1:]
            return self.helper(plus, new_nums, target) + self.helper(minus, new_nums, target)
        
    def helper2(self, summ, nums, idx, target):
        """
        summ: current sum of the combinations
        *nums: a list of the numbers used
        *idx: a int of which number we are choosing (increases over time)
        target: the target value to reach using the nums

        minor improvements to helper() as I thought i could reduce execution time by:
        - using index instead of creating a new smaller list everytime
        - using 
        """
        if len(nums) == idx and summ == target:
            return 1
        elif len(nums) == idx and summ != target:
            return 0
        else:
            #print(nums)
            plus = summ + nums[idx]
            minus = summ - nums[idx]
            return self.helper2(plus, nums, idx+1, target) + self.helper2(minus, nums, idx+1, target)


    def helper3(self, table, summ, nums, idx, target):
        """
        *table: cache of (idx, curr_summ) : sum
        summ: current sum of the combinations
        *nums: a list of the numbers used
        *idx: a int of which number we are choosing (increases over time)
        target: the target value to reach using the nums

        cached version of helper() and helper2()
        - the hashtable uses (idx, curr_summ) as key. This allows you to know which level in the recursive tree you are in, as well as which choice you made!

        """
        if (idx, summ) in table:
            print('i used the solution', (idx, summ), table[(idx, summ)])
            #print(table)
            return table[(idx, summ)]
        elif len(nums) == idx and summ == target:
            return 1
        elif len(nums) == idx and summ != target:
            return 0
        else:
            #print(nums)
            plus = self.helper3(table, summ+nums[idx], nums, idx+1, target)
            minus = self.helper3(table, summ-nums[idx], nums, idx+1, target)
            table[(idx, summ)] = plus + minus
            return plus + minus
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.helper3({}, 0, nums, 0, target)
        

s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))