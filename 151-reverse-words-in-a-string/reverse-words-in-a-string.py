class Solution:
    def reverseWords(self, s: str) -> str:
        while("  " in s):
            s = s.replace("  ", " ")
        s_list = s.split(" ")
        result = []
        for x in s_list[::-1]:
            if x!= '':
                result.append(x)
        return " ".join(result)
        