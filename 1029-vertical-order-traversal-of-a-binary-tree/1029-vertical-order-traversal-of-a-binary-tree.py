# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Store all nodes with their (col, row, val)
        nodes = []
        q = deque([(root, 0, 0)])  # (node, col, row)
        
        while q:
            node, col, row = q.popleft()
            nodes.append((col, row, node.val))
            
            if node.left:
                q.append((node.left, col - 1, row + 1))
            if node.right:
                q.append((node.right, col + 1, row + 1))
        
        # Sort by column first, then row, then value
        nodes.sort()
        
        # Group by column
        result = []
        current_col = nodes[0][0]
        current_list = []
        
        for col, row, val in nodes:
            if col != current_col:
                result.append(current_list)
                current_list = []
                current_col = col
            current_list.append(val)
        
        # Don't forget the last column
        result.append(current_list)
        
        return result
