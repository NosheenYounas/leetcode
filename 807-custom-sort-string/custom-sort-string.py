class Solution:
    def customSortString(self, order: str, s: str) -> str:
        Count = collections.Counter(s)
        res = []
        for char in order:

            if char in s:
                res.extend([char]*Count[char])
                del Count[char]
        for char,count in Count.items():
            res.extend(char*count)
        return ''.join(res)