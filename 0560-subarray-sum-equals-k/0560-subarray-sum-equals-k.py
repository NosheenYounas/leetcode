class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0 
        cur_sum = 0
        freq ={0:1}
        for  n in nums:
            cur_sum += n
            if (cur_sum -k) in freq:
                count += freq[cur_sum -k]
            freq[cur_sum] = freq.get(cur_sum ,0)+1
        return count
       



