class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        # Create a 2D DP table initialized with zeros
        memo = [[0] * n for _ in range(n)]
        
        # Generate all combinations of `i` and `j` in the correct order.
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # Case 1: Character at `i` equals character at `j`
                if s[i] == s[j]:
                    memo[i][j] = memo[i + 1][j - 1]
                # Case 2: Character at `i` does not equal character at `j`.
                # Either delete character at `i` or delete character at `j`
                # and try to match the two pointers using recursion.
                # We need to take the minimum of the two results and add 1
                # representing the cost of deletion.
                else:
                    memo[i][j] = 1 + min(memo[i + 1][j], memo[i][j - 1])
        
        # Return true if the minimum cost to create a palindrome by only deleting the letters
        # is less than or equal to `k`.
        return memo[0][n - 1] <= k
#T  O(n) * O(n)
#S O(n)* O(n)