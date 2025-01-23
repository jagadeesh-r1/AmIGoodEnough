class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)
        index = 0
        result = ""
        while(len_word1 and len_word2):
            print(index, len_word1, len_word2)
            result += word1[index]
            result += word2[index]

            index += 1
            len_word1 -= 1
            len_word2 -= 1
        print(index, len_word1, len_word2)
        
        if len_word1:
            while(len_word1):
                result += word1[index]
                index += 1
                len_word1 -= 1
        if len_word2:
            while(len_word2):
                result += word2[index]
                index += 1
                len_word2 -= 1
        return result

