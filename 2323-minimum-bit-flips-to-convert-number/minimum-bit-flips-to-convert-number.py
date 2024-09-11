class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res=0
        for i in range(32):
            res+=((start>>i & 1)^(goal>>i & 1))
        return res