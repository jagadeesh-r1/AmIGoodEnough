class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_list = s1.split(' ')
        s2_list = s2.split(' ')
        result = []
        for word in s1_list:
            if s1_list.count(word) > 1 or word in s2_list:
                continue
            else:
                result.append(word)
        for word in s2_list:
            if s2_list.count(word) > 1 or word in s1_list:
                continue
            else:
                result.append(word)
        return result
