class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        potential_first = float('inf')
        v2 = float('inf')
        for n in nums:
            if n <= potential_first:
                potential_first = n
            elif n <= v2:
                v2 = n
            else:
                return True
        return False