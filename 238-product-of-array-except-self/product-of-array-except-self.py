class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # whole_product = 0
        # zero_flag = False
        # for num in nums:
        #     if num != 0:
        #         if whole_product == 0:
        #             whole_product = 1
        #         whole_product *= num
        #     else:
        #         zero_flag = True
        # result = []
        # for num in nums:
        #     if zero_flag:
        #         if num != 0:
        #             result.append(0)
        #         else:
        #             result.append(whole_product)
        #     else:
        #         result.append(whole_product // num)
        # return result
        whole_product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                whole_product *= num
            else:
                zero_count += 1
        result = []
        for num in nums:
            if num == 0 and zero_count == 1:
                result.append(whole_product)
            elif num == 0 and zero_count > 1:
                result.append(0)
            elif num != 0 and zero_count > 0:
                result.append(0)
            elif num != 0 and zero_count == 0:
                result.append(whole_product//num)
        return result