class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) == len(set(nums)):
        #     return False
        # else:
        #     return True
        hash_map = {}
        for i in nums:
            if hash_map.get(i):
                return True
            hash_map[i] = 1
        return False