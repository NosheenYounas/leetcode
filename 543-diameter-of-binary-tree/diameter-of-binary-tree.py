# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 
        def DFS(root):
            if not root:
                return 0
            l_dep = DFS(root.left)
            r_dep = DFS(root.right)
            self.diameter= max(self.diameter,l_dep+r_dep)
            return 1+ max(l_dep,r_dep)
        DFS(root)
        return self.diameter
    

        #Time complexity: O(n)
        #Space complexity: O(h)
        #Best Case (balanced tree): O(log(n))
        #Worst Case (degenerate tree): O(n)


            