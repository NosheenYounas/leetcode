class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_prefix_sum = 0
        prefix_sum_to_freq = {0: 1}
        
        for num in nums:
            curr_prefix_sum += num
            
            if (curr_prefix_sum - k) in prefix_sum_to_freq:
                count += prefix_sum_to_freq[curr_prefix_sum - k]
            
            prefix_sum_to_freq[curr_prefix_sum] = prefix_sum_to_freq.get(curr_prefix_sum, 0) + 1
        
        return count