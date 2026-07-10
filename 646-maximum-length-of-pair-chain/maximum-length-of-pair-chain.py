class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])  # sort by end value
        cur_end = pairs[0][1]
        res = 1
        for i in range(1, len(pairs)):
            if pairs[i][0] > cur_end:
                res += 1
                cur_end = pairs[i][1]
        return res 