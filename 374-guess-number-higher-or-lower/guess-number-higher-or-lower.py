# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        low = 1
        high = n
        
        while True:
            mid = low + (high - low) // 2
            myGuess = guess(mid)
            if myGuess == 1:
                low = mid + 1
            elif myGuess == -1:
                high = mid - 1
            else:
                return mid