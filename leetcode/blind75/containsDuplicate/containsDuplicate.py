class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        #for idx, num in enumerate(nums):
        for num in nums:
            if num in hashtable:
                return True
            else:
                hashtable[num] = 1
        return False