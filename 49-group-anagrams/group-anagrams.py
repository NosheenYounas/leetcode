class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)
        for str in strs:
            key = ''.join(sorted(str))
            dict[key].append(str)
        return list(dict.values())
        #res=collections.defaultdict(list)
        #for s in strs:
            #count=[0]*26  
            #for c in s:
               # count[ord(c)-ord("a")]+=1
                #res[tuple(count)].append(s)
        #return list(res.values())      