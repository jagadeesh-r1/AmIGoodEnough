class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_map = {}
        sorted_arr = sorted(set(arr))

        # print(sorted_arr)
        index = 0
        for i in sorted_arr:
            rank_map[i] = index + 1
            index = index + 1
        for idx in range(len(arr)):
            arr[idx] = rank_map[arr[idx]]

        return arr
