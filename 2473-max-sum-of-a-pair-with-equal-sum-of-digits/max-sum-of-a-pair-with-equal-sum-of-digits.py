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
        map=defaultdict(list)
        for num in nums:
            s=0
            tmp=num
            while tmp>0:
                s+=tmp%10
                tmp=tmp//10
            map[s].append(num)
        max_sum=-1
        for k in map.keys():
            l=map[k]
            if len(l)<2:
                continue
            m1,m2=0,0
            for num in l:
                if num>m1:
                    m2=m1
                    m1=num
                elif num>m2:
                    m2=num
            max_sum=max(max_sum,m1+m2)

        return max_sum