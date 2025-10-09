# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        rightSide  = None
        while q:
            size = len(q) 
            for i in range(size):
                node = q.popleft()
                rightSide = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if rightSide:
                    res.append(rightSide.val)
        return res


            
        