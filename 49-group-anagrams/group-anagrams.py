class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_list = {}
        for string in strs:
            sorted_str = ''.join(sorted(list(string)))
            if sorted_str in result_list:
                result_list[sorted_str].append(string)
            else:
                result_list[sorted_str] = []
                result_list[sorted_str].append(string)
        # print(result_list.values())
        return result_list.values()
