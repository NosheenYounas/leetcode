class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counts=collections.Counter(s)

        res=[]
        for char in order :
            if char in s_counts:
                res.extend([char]*s_counts[char])
                del s_counts[char]
        for char,count in s_counts.items():
            res.extend([char]*count)
        return "".join(res)
        