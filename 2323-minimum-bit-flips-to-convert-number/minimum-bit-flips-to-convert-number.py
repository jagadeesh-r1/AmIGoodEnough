class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res=0
        while goal>0 or start>0:
            res+=((start & 1)^(goal & 1))
            start>>=1
            goal>>=1
        return res