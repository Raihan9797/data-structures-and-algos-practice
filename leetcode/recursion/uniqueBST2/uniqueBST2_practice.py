from typing import Optional
from typing import List

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        whole = []
        while not (self.left == None and self.right == None):
            self


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def helper(start: int, end: int):
            all_trees = []
            if start > end:
                return [None]
            
            for i in range(start, end + 1):
                left_trees = helper(start, i-1)
                right_trees = helper(i+1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        key = TreeNode(i)
                        key.left = l
                        key.right = r
                        all_trees.append(key)
            return all_trees
        return helper(1, n)

s = Solution()
print(s.generateTrees(3))