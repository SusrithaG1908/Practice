# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def getRoot(nums, l, r):
            if r < 0 or l > r or l >= len(nums):
                return None
            
            
            mid = (l + r) // 2
            n = TreeNode(nums[mid])
            
            
            n.left = getRoot(nums, l, mid - 1)
            n.right = getRoot(nums, mid + 1, r)
            
            
            return n
        return getRoot(nums,0,len(nums))
