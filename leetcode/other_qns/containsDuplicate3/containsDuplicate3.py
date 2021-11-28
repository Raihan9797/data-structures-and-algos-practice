#from sortedcontainers import SortedList
from collections import OrderedDict
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets = OrderedDict()
        divisor = t + 1
        for idx, num in enumerate(nums):
            if len(buckets) > k:
                oldval = nums[idx-k-1] // divisor
                buckets.pop(oldval)
            newval = num // divisor
            if newval in buckets:
                return True
            elif newval + 1 in buckets and abs(buckets[newval+1]-num) <=t:
                #print('checktop')
                return True
            elif newval - 1 in buckets and abs(buckets[newval-1]-num) <=t:
                #print('check bottom')
                return True
            else:
                buckets[newval] = num
                #print(buckets)
        return False
                
        ### brute force..
        # for idx in range(len(nums)):
        #     for j in range(idx+1, idx+k+1):
        #         #print(j)
        #         if j >= len(nums): continue
        #         else:
        #             #print(nums[idx], nums[j])
        #             #print('numsi - numsj lt t:', nums[idx] - nums[j], t)
        #             if abs(nums[idx] - nums[j]) <= t:
        #                 return True
        #         #print(nums[idx], nums[j])
        # return False
                
s = Solution()
nums = [1,5,9,1,5,9], k = 2, t = 3
print(s.containsNearbyAlmostDuplicate(nums, k, t)) # false