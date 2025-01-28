class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i in s:
            if i in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
                vowels.append(i)
        print(vowels)
        count = len(vowels)
        result = ''
        for i in s:
            if i in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
                result += vowels[count - 1]
                count -= 1
            else:
                result += i

        return result
        