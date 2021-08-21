# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/

from typing import Optional # still doesnt work

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case: empty root -> return root
        if not root:
            return root
        
        # base case 2: we find the val at the root! -> return root
        elif val == root.val:
            return root
        else:
            
            # val is less than root -> check left side
            if val < root.val:
                left_tree = Solution().searchBST(root.left, val)
                return left_tree
            
            # val is more than root -> check right side
            else:
                right_tree = Solution().searchBST(root.right, val)
                return right_tree
