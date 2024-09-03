import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        result_list = []
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        # print(hash_map)
        return heapq.nlargest(k,hash_map.keys(), key=hash_map.get)