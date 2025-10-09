class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = []
        q = deque()
        q.append((0, 0))
        
        while q:
            row, col = q.popleft()
            
            result.append(nums[row][col])
            
            # Add the cell below (only when at leftmost column)
            if col == 0 and row + 1 < len(nums):
                q.append((row + 1, col))
            
            # Add the cell to the right (if it exists in this row)
            if col + 1 < len(nums[row]):
                q.append((row, col + 1))
        
        return result
  #T O(N)
  #S O(sqrt(N))      