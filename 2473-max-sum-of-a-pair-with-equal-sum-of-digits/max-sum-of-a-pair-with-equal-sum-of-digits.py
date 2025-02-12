# class Solution:
#     def maximumSum(self, nums: List[int]) -> int:
#         max_number = -1
#         sum_map = {}
#         for i in range(len(nums)):
#             temp = str(nums[i])
#             # print(temp)
#             int_sum = 0
#             for digit in temp:
#                 int_sum += int(digit)
#             # print(int_sum)
#             if sum_map.get(int_sum) != None:
#                 for x in sum_map[int_sum]:
#                     pair_sum = nums[i] + nums[x]
#                     # print(i, sum_map[int_sum])
#                     max_number = max(max_number, pair_sum)
#                     # print(max_number)
#                 sum_map[int_sum].append(i)
#             else:

#                 sum_map[int_sum] = [i]
#                 # print(sum_map)

#         return max_number

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_arr = [0] * 82
        ans = -1
        for x in nums:
            digit_sum = sum(int(d) for d in str(x))
            if max_arr[digit_sum] != 0:
                ans = max(ans, x + max_arr[digit_sum])
            max_arr[digit_sum] = max(max_arr[digit_sum], x)
        return ans