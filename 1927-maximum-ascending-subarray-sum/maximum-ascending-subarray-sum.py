# class Solution:
#     def maxAscendingSum(self, nums: List[int]) -> int:
#         max_sum = -1
#         sum = 0
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) == 0:
#             return 0
#         for i in range(len(nums)):
#             if i < len(nums)-1:
#                 if nums[i] < nums[i+1]:
#                     print(nums[i], sum)
#                     sum += nums[i]
#                 elif nums[i] > nums[i+1]:
#                     print(nums[i], sum)
#                     sum += nums[i]
#                     print("local max", sum)

#                     if sum > max_sum:
#                         max_sum = sum
#                         sum = 0
#                     else:
#                         sum = 0
#                 elif nums[i] == nums[i+1]:
#                     print(nums[i], sum)
#                     sum += nums[i]
#                     print("local max", sum)

#                     if sum > max_sum:
#                         max_sum = sum
#                         sum = 0
#                     else:
#                         sum = 0
#             else:
#                 if nums[i] > nums[i-1]:
#                     print(nums[i], sum)
#                     sum += nums[i]
#                     if sum > max_sum:
#                         max_sum = sum
                    
#                 elif nums[i] < nums[i-1]:
#                     sum = nums[i]
#                     if sum > max_sum:
#                         max_sum = sum
#         return max_sum
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        cur = nums[0]

        for i in range(len(nums)-1):
            
            if nums[i] < nums[i+1]:
                cur += nums[i+1]
            else:
                result = max(cur, result)
                cur = nums[i+1]


        return max(cur, result)        