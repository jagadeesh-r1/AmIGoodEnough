import statistics


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = nums1 + nums2
        merged_list.sort()
        # print(merged_list)
        if len(merged_list)%2 == 0:
            print(merged_list[len(merged_list)//2])
            print(merged_list[(len(merged_list)//2) - 1])
            return (merged_list[len(merged_list)//2] + merged_list[(len(merged_list)//2) - 1]) / 2
        else:
            return merged_list[len(merged_list)//2]
            
        
        # return statistics.median(merged_list)
