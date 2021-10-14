class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ### brute force solution
        # for i in range(0, len(nums)):
        #     check = target
        #     check -= nums[i]
        #     for j in range(0, len(nums)):
        #         if i == j:
        #             continue
        #         check2 = check - nums[j]
        #         if check2 == 0:
        #             print(target, nums[i], check, nums[j], check2)
        #             return [i, j]
        # return [-1, -1]
        
        ### optimal solution: use hashmap and you can one pass it!
        d = {}
        for index, value in enumerate(nums):
            ## minus off then check if the value is in the list
            check = target - value
            
            # if yes, return both keys. Because you have seen both value
            if check in d:
                return [d[check], index]
            
            # if not, add values to the list
            else:
                d[value] = index