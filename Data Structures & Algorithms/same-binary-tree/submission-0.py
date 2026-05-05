# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root,arr):
            if not root:
                arr.append(None)
                return arr

            arr.append(root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)
            
        a1 = []
        a2 = []
        dfs(p, a1)
        dfs(q, a2)
        if a1 != a2:
            return False
        return True