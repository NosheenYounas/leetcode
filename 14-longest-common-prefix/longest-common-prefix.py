class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        l = min([len(x) for x in strs])
        res = ""
        for j in range(l):
            flag = 0
            for i in range(len(strs)):
                if strs[i][j] != strs[0][j]:
                    flag = 1
                    break
            if flag:
                break
            else:
                res += strs[i][j]
        
        return res