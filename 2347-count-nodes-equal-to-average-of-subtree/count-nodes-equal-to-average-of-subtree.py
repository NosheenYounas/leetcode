# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0
        def dfs (curr):
            if not curr:
                return (0,0)
            leftSum , leftCount = dfs(curr.left)
            rightSum , rightCount = dfs (curr.right)
            summ = curr.val + leftSum + rightSum
            count = 1 + leftCount + rightCount
            if summ // count == curr.val:
                self.res += 1
            return (summ,count)
        dfs(root)
        return self.res
