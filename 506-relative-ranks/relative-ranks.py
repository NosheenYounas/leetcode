class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sor=sorted(score,reverse=True)
        rank={}
        for i,val in enumerate(sor):
            if i==0:
                rank[val]="Gold Medal"
            elif i==1:
                rank[val]="Silver Medal"
            elif i==2:
                rank[val]="Bronze Medal"
            else:
                rank[val]=str(i+1)
        res=[]
        for s in score:
            res.append(rank[s])
        return res
